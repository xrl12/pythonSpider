import logging
import os.path as op

from flask import url_for, redirect, request, flash
from flask_login.utils import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import expose
from flask_admin.helpers import (get_redirect_target)
from flask_admin.form import FormOpts
from flask_admin.babel import gettext
from wtforms import SelectField

from app.models.shop import Area
from app.models.shop import ShopCategory

file_path = op.join(op.dirname(__file__), '../static')  # 文件上传路径

log = logging.getLogger("flask-admin.sqla")


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.index', next=request.url))


class CatModelview(MyModelView):
    column_labels = {
        'id': '序号',
        'name': '分类名',
        'position': '排序',
        'show_page': '这个分类在哪里展示',
        'create_time': '创建时间',
        'update_time': '更新时间'
    }

    form_extra_fields = {
        'area_id': SelectField('区域：', choices=[]),
        'own': SelectField('商品分类：', choices=[])
    }

    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        """
            Create model view
        """
        return_url = get_redirect_target() or self.get_url('.index_view')
        if not self.can_create:
            return redirect(return_url)
        form = self.create_form()
        if not hasattr(form, '_validated_ruleset') or not form._validated_ruleset:
            self._validate_form_instance(ruleset=self._form_create_rules, form=form)
        if self.validate_form(form):
            # in versions 1.1.0 and before, this returns a boolean
            # in later versions, this is the model itself
            model = self.create_model(form)
            if model:
                flash(gettext('Record was successfully created.'), 'success')
                if '_add_another' in request.form:
                    return redirect(request.url)
                elif '_continue_editing' in request.form:
                    # if we have a valid model, try to go to the edit view
                    print('我在_continue_editing')

                    if model is not True:
                        url = self.get_url('.edit_view', id=self.get_pk_value(model), url=return_url)
                    else:
                        url = return_url
                    return redirect(url)
                else:
                    # save button
                    return redirect(self.get_save_return_url(model, is_created=True))

        form_opts = FormOpts(widget_args=self.form_widget_args,
                             form_rules=self._form_create_rules)

        if self.create_modal and request.args.get('modal'):
            template = self.create_modal_template
        else:
            template = self.create_template
        area_list = [(v.id, v.name) for v in Area.query.filter_by(status=1).all()]
        area = area_list.append((0, ''))
        own_list = [(v.id, v.name) for v in ShopCategory.query.filter_by(status=1).all()]
        own = own_list.append((0, ''))

        form.area_id.choices = area_list
        form.own.choices = own_list

        return self.render(template,
                           form=form,
                           form_opts=form_opts,
                           return_url=return_url)

import execjs

exj = execjs.get()
js_fils = open("zhilian.js",'r').read()
exj.compile(js_fils)
request_id  =  exj.eval("x-zp-page-request-id")
client_id = exj.eval("x-zp-client-id")
print(request_id,client_id)
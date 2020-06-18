function stringToHex(str) {
    var val = "";
    for (var i = 0; i < str.length; i++) {
        if (val == "") val = str.charCodeAt(i).toString(16); else val += str.charCodeAt(i).toString(16);
    }
    return val;
}


var width = 1536;
var height = 864;
var screendate = width + "," + height;
cookie = "srcurl=" + stringToHex("http://www.300600900.cn/");
url = "/?security_verify_data=" + stringToHex(screendate);

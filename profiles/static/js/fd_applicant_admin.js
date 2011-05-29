django.jQuery(document).ready(function() {
    django.jQuery(".vLargeTextField").each(function(){
	f = django.jQuery(this);
	val = f.val();
	if (val.substring(0, 1) != '[') {
		// Not json, leave it alone
		return;
	}
	try { 
	   text = eval(val);
	} catch(e) {
           // something went wrong decoding the json, leave it alone
	   return;
	}
	out = '<div style="float: left; padding-left: 5px">';
	if (f.attr("name") == "recommend_json") {
		for (var i = 0; i < text.length; i++){ 
			out += '<a href="mailto:' + text[i].email + '">' + text[i].name + '</a><br />';
		}
	} else {
		out += text.join(", ");
	}
	f.hide();
	f.after(out + "</div>");
    });
});

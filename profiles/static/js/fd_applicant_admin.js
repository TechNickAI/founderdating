// Let's go ahead and use the default namespace for jquery, so that jquery UI works.
(function($){jQuery = $.noConflict(true);})(django.jQuery);

// Handles 'json' fields 
jQuery(document).ready(function() {
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


// Handles bulk actions for emailing applicants by displaying an intermediary form
jQuery(document).ready(function(){
    jQuery("select[name=action]").change(function (){
        var dd = jQuery(this);
        var selected = dd.val();
        if (selected == "email_declination" ||
            selected == "email_applicant" ||
            selected == "email_references" ||
            selected == "invite_to_event") {
    
                // Create a div for holding the email temlate
                if (jQuery("#" + selected).length === 0) {
                    jQuery("body").prepend('<div id="' + selected + '"></div>');
                }
                // Pull in the template via ajax and display it as a dialog
                jQuery("#" + selected).load("/email_form?email_template=" + selected).dialog({
                    "width": 440,
                    "position": "top",
                    "modal": true,
                    "title": dd.find(":selected").text(),
                });
        }
    });
});

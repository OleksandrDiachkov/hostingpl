$(document).ready(function(){

$.validator.setDefaults({
	submitHandler: function() { 
		$.ajax({
		  type: "POST",
		  url: "server.php",
		  data: $("#promo-form").serialize()
		}).done(function( msg ) {
		    $(".modal .ajax_data").html("<pre>"+msg+"</pre>");
		    $(".modal").modal("show");
		});
	}
 });

$('#promo-form input').hover(function()
	{
	$(this).popover('show')
	});

$('#promo-form').validate({

	rules:{
		name: {
			required: true
		},
		email: {
			required: true,
			email: true
		},
		password: {
			required: true,
			minlength: 10 
		}
	},
	messages:{
		name:"Enter your first and last name",
		email:{
			required:"Enter your email address",
			email:"Enter valid email address"},
		password:{
			required:"Enter your password",
			minlength:"Password must be minimum 6 characters"},
		},
		showErrors: function(errorMap, errorList) {
    $.each(this.successList, function(index, value) {
      return $(value).popover("hide");
    });
    return $.each(errorList, function(index, value) {
      var _popover;
      _popover = $(value.element).popover({
        trigger: "manual",
        placement: "top",
        content: value.message,
        template: "<div class=\"popover\"><div class=\"arrow\"></div><div class=\"popover-inner\"><div class=\"popover-content\"><p></p></div></div></div>"
      });
      // Bootstrap 3.x :      
      //_popover.data("bs.popover").options.content = value.message;
      // Bootstrap 2.x :
      _popover.data("popover").options.content = value.message;
      return $(value.element).popover("show");
    });
  }
	});
});
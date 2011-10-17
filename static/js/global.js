$(document).ready(function(){
	// Efeito active do menu
	$("nav ul li a").each(function(){
	    if($(this).attr('href').split('/')[1] == location.pathname.split('/')[1]){
	        $(this).parent().addClass('active')
	        return false;
	    }
	});
	// Efeito cursor nos links
	cursor = '<span class="element-mouse-over-effect"> |</span>';
	interval = null;
	$('h3 a').hover(
		function(){
			link = $(this);
			link.after(cursor);
			i = 1;
			interval = setInterval(function(){
			    i++;
			    if(i%2 == 0){
			        link.parent().find('span.element-mouse-over-effect').css('color', '#fff');
			    }else{
			        link.parent().find('.element-mouse-over-effect').css('color', '#000');
			    }
			}, 500)
		},
		function(){
			clearInterval(interval)
			$(this).parent().find('span.element-mouse-over-effect').remove();
		}
	);

	// search box
	input_text = "#search-form input[type=text]"
	input_submit = "#search-form input[type=submit]"
	$(input_submit).hover(
		function(){
			$(this).addClass("hover");
		},
		function(){
			$(this).removeClass("hover");
		}
	);
	$(input_text).focus(function(){
		$(this).addClass("active");
		$(input_submit).stop().animate({
			right: -95
		}, 500, function() {
			$(this).css('z-index', '1');
		});
	});
	$(input_text).blur(function(){
		$(this).removeClass("active");
		if(!$(input_submit).hasClass("hover")){
			$(input_submit).stop().css('z-index', '-1').animate({
				right: '95'
			}, 500);
		}
	});

	// Placeholder
	$('[placeholder]').focus(function() {
	  var input = $(this);
	  if (input.val() == input.attr('placeholder')) {
		input.val('');
		input.removeClass('placeholder');
	  }
	}).blur(function() {
	  var input = $(this);
	  if (input.val() == '' || input.val() == input.attr('placeholder')) {
		input.addClass('placeholder');
		input.val(input.attr('placeholder'));
	  }
	}).blur();
	$('[placeholder]').parents('form').submit(function() {
	  $(this).find('[placeholder]').each(function() {
		var input = $(this);
		if (input.val() == input.attr('placeholder')) {
		  input.val('');
		}
	  })
	});
});
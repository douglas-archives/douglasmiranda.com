$(document).ready(function(){
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
});
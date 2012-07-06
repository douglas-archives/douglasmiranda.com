$(document).ready(function(){
	$('#ultimos-projetos li').hover(
		function(){
			$(this).addClass('active');
		},
		function(){
			$(this).removeClass('active');
		}
	);
});
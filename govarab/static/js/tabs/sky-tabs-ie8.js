$(function()
{
	$('.sky-tabs > input:checked').each(function()
	{
		$(this).next().addClass('active');
		$(this).siblings('ul').find('.' + $(this).attr('class')).show();
	});
	
	$('.sky-tabs > label').on('click', function()
	{
		$(this).addClass('active').siblings().removeClass('active');
		$(this).siblings('ul').find('.' + $(this).prev().attr('class')).show().siblings().hide();
	});
});

/* share URL: http://www.20script.ir */
$(function () {
    $('.contact').on('click', function () {
        if ($(this).hasClass('active')) {
            $('.contact-content').hide();
            $(this).find('span').text('+');
            $(this).removeClass('active');
        } else {
            $('.contact-content').show();
            $(this).find('span').text('-');
            $(this).addClass('active');
        }
    });
});
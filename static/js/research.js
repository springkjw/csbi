$(function () {
    $('.na').on('click', function () {
        $('.na').removeClass('active');
        $(this).addClass('active');

        var step = $(this).attr('data-id');
        var class_name = '.' + step;

        $('.item').hide();
        $(class_name).show();
    })
});
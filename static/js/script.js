$(document).ready(function() {

    var myFooter = $('#footer');
    var docHeight = $(window).height();
    var footerHeight = myFooter.height();
    var footerTop = myFooter.position().top + footerHeight;

    if (footerTop < docHeight) {
        myFooter.css('margin-top', 10 + (docHeight - footerTop) + 'px');
    }
});
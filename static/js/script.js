$(document).ready(function() {

    var myFooter = $('#footer');
    var docHeight = $(window).height();
    var footerHeight = myFooter.height();
    var footerTop = myFooter.position().top + footerHeight;

    if (footerTop < docHeight) {
        myFooter.css('margin-top', 10 + (docHeight - footerTop) + 'px');
    }


    $("flights-item").isotope({
        itemSelector: ".item",
        layoutMode: "fitRows"
    });


    var li = $('.flights-menu ul li');
    li.click(function () {
        li.removeClass("btn-success");
        $(this).siblings().addClass("btn-outline-success");
        $(this).removeClass("btn-outline-success");
        $(this).addClass("btn-success");

        var selector = $(this).attr("data-filter");
        $('.flights-item').isotope({
            filter: selector
        });
        return false;
    });

});
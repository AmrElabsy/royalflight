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
        li.removeClass("btn-primary");
        $(this).siblings().addClass("btn-outline-primary");
        $(this).removeClass("btn-outline-primary");
        $(this).addClass("btn-primary");

        var selector = $(this).attr("data-filter");
        $('.flights-item').isotope({
            filter: selector
        });
        return false;
    });

    //switch between login \ sign up
    $('h1 span').click(function(){
        $(this).addClass('selected').siblings().removeClass('selected');
        $('.login-page form').hide();
        $('.'+$(this).data('class')).show(100);
    });


    var classA = $('#radioClassA');
    var classB = $('#radioClassB');
    var classC = $('#radioClassC');

    var priceA = $('#priceA');
    var priceB = $('#priceB');
    var priceC = $('#priceC');


    classA.change(function () {
        if (classA.is(':checked'))
        {
            priceA.show();
            priceB.hide();
            priceC.hide();
        }
    });

    classB.change(function () {
        if (classB.is(':checked'))
        {
            priceA.hide();
            priceB.show();
            priceC.hide();
        }
    });

    classC.change(function () {
        if (classC.is(':checked'))
        {
            priceA.hide();
            priceB.hide();
            priceC.show();
        }
    });

});
// Animate nav dropdown on menu btn click
$("svg").click(toggleMenu);

function toggleMenu() {

    $(".menu-btn").css("pointer-events", "none")
    let timeframe;

    if ($("nav").height() < 250) {
        $("nav").animate({
            height: "281px"
        }, 500);
        timeframe = 10;
    } else {
        $("nav").animate({
            height: "155px"
        }, 300);
        timeframe = 300;
    }

    setTimeout(function () {
        $(".main-links").toggleClass("first");
        $("#initial").toggleClass("order");
        $(".login").toggleClass("second");
        $(".cart").toggleClass("third");
    }, timeframe)

    setTimeout(function () {
        $(".menu-btn").css("pointer-events", "initial")
    }, 500)

}

// $(".product").hasClass()

$($(".rating-filter label")).click(toggleRating);

function toggleRating(event) {
    event.preventDefault()
    let currentInput = $($(this).children()[0]);
    currentInput.prop('checked', (!currentInput.is(':checked')));
    $(this).toggleClass("checked-rating");
}
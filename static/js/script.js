// Animate nav dropdown on menu btn click
$("svg").click(toggleMenu);

function toggleMenu() {

    let timeframe;

    if ($("nav").height() < 250) {
        $("nav").animate({
            height: "250px"
        }, 500);
        timeframe = 10;
    } else {
        $("nav").animate({
            height: "120px"
        }, 300);
        timeframe = 300;
    }

    setTimeout(function () {
        $(".main-links").toggleClass("first");
        $(".login").toggleClass("second");
        $(".cart").toggleClass("third");
    }, timeframe)

}
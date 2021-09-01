// Animate nav dropdown on menu btn click
$("svg").click(toggleMenu);

function toggleMenu() {

    $(".menu-btn").css("pointer-events", "none")
    let timeframe;

    if ($("nav").height() < 250) {
        console.log(4)

        $("nav").animate({
            height: "281px"
        }, 500);
        timeframe = 10;
    } else {
        console.log(5)
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
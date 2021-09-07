$(document).ready(function () {

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

    /* Filtering */

    // Toggle rating checkbox on label click
    $($(".rating-filter label")).click(toggleRating);

    function toggleRating(event) {
        event.preventDefault()
        let currentInput = $($(this).children()[0]);
        currentInput.prop('checked', (!currentInput.is(':checked')));
        $(this).toggleClass("checked-rating");
        filterRating()
    }

    // If filter off show all products, else show selected
    function filterRating() {
        let inputs = $(".rating-filter input");
        checked = [];
        for (i = 0; i < inputs.length; i++) {
            if ($(inputs[i]).is(':checked')) {
                checked.push(parseInt($(inputs[i]).val()));
            }
        }
        let products = $(".product");
        for (i = 0; i < products.length; i++) {

            let productRating = parseInt($(products[i]).find(".rating").text())
            if (checked.length === 0) {
                $(".product").css("display", "block");
            } else if (!(checked.includes(productRating))) {
                $(products[i]).css("display", "none");
            } else {
                $(products[i]).css("display", "block");
            }
        }
    }
});
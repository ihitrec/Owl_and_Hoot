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

    // Toggle brand filter
    $(".brand-filter input").click(filter);

    // Toggle rating filter
    $($(".rating-filter label")).click(toggleRating);

    function toggleRating(event) {
        event.preventDefault()
        let currentInput = $($(this).children()[0]);
        currentInput.prop('checked', (!currentInput.is(':checked')));
        $(this).toggleClass("checked-rating");
        filter()
    }

    // Hide products not matching single or both filters
    function filter() {

        let inputs = $(".filter input");
        let checked = [];
        for (i = 0; i < inputs.length; i++) {
            if ($(inputs[i]).is(':checked')) {
                checked.push($(inputs[i]).val());
            }
        }

        let products = $(".product");
        for (i = 0; i < products.length; i++) {

            let productRating = parseInt($(products[i]).find(".rating").text()).toString();
            let productBrand = $(products[i]).attr("id");
            if (checked.length === 0) {
                $(".product").css("display", "block");
                break;
            } else if (!$(".brand-filter input").is(':checked') || !$(".rating-filter input").is(':checked')) {
                if (checked.includes(productRating) || checked.includes(productBrand)) {
                    $(products[i]).css("display", "block");
                } else {
                    $(products[i]).css("display", "none");
                }
            } else {
                if (checked.includes(productRating) && checked.includes(productBrand)) {
                    $(products[i]).css("display", "block");
                } else {
                    $(products[i]).css("display", "none");
                }
            }
        }
    }

    /*  Sort  */

    $('#sort').on('change', sorted);

    // Sort products by date or price
    function sorted() {

        let newOrder;
        let products = $("#product-list a")

        if ($(this).val() === "newest") {
            newOrder = $(products.toArray().sort(function (a, b) {
                aVal = Date.parse(a.getAttribute("data-date"));
                bVal = Date.parse(b.getAttribute("data-date"));
                return aVal - bVal;
            }));
        } else if ($(this).val() === "low") {
            newOrder = $(products.toArray().sort(function (a, b) {
                aVal = parseInt(a.getAttribute("data-price"));
                bVal = parseInt(b.getAttribute("data-price"));
                return aVal - bVal;
            }));
        } else if ($(this).val() === "high") {
            newOrder = $(products.toArray().sort(function (a, b) {
                aVal = parseInt(a.getAttribute("data-price"));
                bVal = parseInt(b.getAttribute("data-price"));
                return bVal - aVal;
            }));
        }

        // Replace old order of links with the new one
        $("#product-list").find('a').remove();
        $("#product-list").append(newOrder);
    }

});
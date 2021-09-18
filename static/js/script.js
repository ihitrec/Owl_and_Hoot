/* Search by section:
   Nav menu
   Skip nav
   Search
   Filtering
   Sorting
   Product
*/

$(document).ready(function () {

    /* Nav menu */

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

    /* Skip nav */

    // Focus after nav, skip reading all content
    $("#skip-nav").click(function () {
        $("header").next().attr("tabindex", "0");
        $("header").next().attr("aria-label", "skipped")
        $("header").next().focus();
        setTimeout(function () {
            $("header").next().removeAttr("aria-label")
            $("header").next().removeAttr("tabindex");
        }, 2000)
    })

    /* Search */

    $(".search input").click(expandSearch);
    // Search open animation depending on screen size
    function expandSearch() {
        if ($(window).width() < 750) {
            $(".search").addClass("wide-search");
            $(".logo, .menu-btn").css("opacity", "0");
            $(".search").animate({
                width: "100%",
            });
        } else {
            $(".search").animate({
                paddingRight: "0%"
            });
        }
        $(".search").find("input").animate({
            width: "70%",
        });
    }

    $(".search input").focusout(collapseSearch);
    // Close animation depending on scr size, prevent multiple clicks
    function collapseSearch() {
        $(".search input").css("pointer-events", "none")
        if ($(window).width() < 750) {
            $(".search").animate({
                    width: "33%",
                },
                function () {
                    $(".search").removeClass("wide-search");
                    $(".logo, .menu-btn").css("opacity", "1");
                });
        } else {
            $(".search ").animate({
                paddingRight: "8%"
            });
        }
        $(".search input").animate({
            width: "20px"
        }, function () {
            $(".search input").val("");
            highlight();
            $(".search input").css("pointer-events", "auto")
        });
    }

    $(".search input").on("input", highlight);
    // Indicate form submit btn
    function highlight() {
        if ($(".search input").val().length > 0) {
            $(".search img").addClass("highlight-search")
        } else {
            $(".search img").removeClass("highlight-search")
        }
    }

    $(".search img").click(submitSearch)
    // Submit form
    function submitSearch() {
        if ($(".search img").hasClass("highlight-search")) {
            $("#search").submit();
        }
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

        if (!$(".product").is(":visible")) {
            $(".no-products").css('display', 'block');
            $(".sort-container").css('display', 'none');
        } else {
            $(".no-products").css('display', 'none');
            $(".sort-container").css('display', 'block');
        }
    }

    // Turn on the filter when brand link is clicked
    if ($(".brand-filter").length === 1) {
        let link = window.location.href.split("/");
        $(`#${link[link.length - 2]}`).prop('checked', true);
    }

    // Remember last filter when using back btn in browser
    if ($(".filter input").is(':checked')) {
        let ratingInput = $(".rating-filter input")
        for (i = 0; i < ratingInput.length; i++) {
            if ($(ratingInput[i]).is(':checked')) {
                $(ratingInput[i]).parent().toggleClass("checked-rating");
            }
        }
        filter()
    }

    /*  Sorting  */

    $('#sort').on('change', sorted);

    // Sort products by date or price
    function sorted() {

        let newOrder;
        let products = $("#product-list a")

        if ($('#sort').val() === "newest") {
            newOrder = $(products.toArray().sort(function (a, b) {
                aVal = Date.parse(a.getAttribute("data-date"));
                bVal = Date.parse(b.getAttribute("data-date"));
                return bVal - aVal;
            }));
        } else if ($('#sort').val() === "low") {
            newOrder = $(products.toArray().sort(function (a, b) {
                aVal = parseInt(a.getAttribute("data-price"));
                bVal = parseInt(b.getAttribute("data-price"));
                return aVal - bVal;
            }));
        } else if ($('#sort').val() === "high") {
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

    // Remember last sort when using back btn in browser
    if ($('#sort').val()) {
        sorted()
    }

    /*  Product */

    // Add border on chosen size
    $(':radio[name="size"]').change(function () {
        $(".sizes label").removeClass("selected-size");
        $(this).parent().toggleClass("selected-size");
    });

    // Increase or decrease product count on symbol click
    $(".plus-minus").click(updateQuantity)

    function updateQuantity() {
        let currentVal = $(".add-to-cart input").val();
        let operation = $(this).attr("data-operation");
        let newVal = eval(`${currentVal}${operation}1`)
        if (newVal < 1) {
            newVal = 1;
        }
        $(".add-to-cart input").val(newVal);
    }

    /* Cart */

    $(".cart img, .overlay").click(showCart)
    // Open/close cart and overlay
    function showCart() {
        $("#cart").toggleClass("opened-cart");
        $(".cart").toggleClass("opened-cart-icon");
        $(".overlay").toggleClass("opened-cart");
    }
});
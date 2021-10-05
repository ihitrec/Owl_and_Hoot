$(document).ready(function () {
    // Loop trough ratings and add star imgs if rating exists 
    let ratings = $(".rating");
    for (let i = 0; i < ratings.length; i++) {
        let ratingParsed = parseFloat(ratings[i].innerHTML);
        if (ratingParsed > 0) {
            generateImages(ratingParsed, i);
        } else {
            ratings[i].innerHTML = '';
        }
    }

    // Generate stars, half star if rating over .5
    function generateImages(rating, target) {
        let ratingNum = ratings[target].innerHTML;
        ratings[target].innerHTML = '';
        let roundedRating = Math.round(rating);
        if (roundedRating <= rating) {
            for (let x = 0; x < roundedRating; x++) {
                fullStar(target);
            }
        } else if (roundedRating > rating) {
            let x = 0;
            for (x; x < roundedRating - 1; x++) {
                fullStar(target);
            }
            $($(".rating")[target]).append("<img src='https://owl-and-hoot.s3.amazonaws.com/static/images/star-half-full.png'></img>");
        }
        $($(".rating")[target]).append(`<p>${ratingNum}</p>`);
    }

    function fullStar(target) {
        $($(".rating")[target]).append("<img src='https://owl-and-hoot.s3.amazonaws.com/static/images/star-full.png'></img>");
    }
});
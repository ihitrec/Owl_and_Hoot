// Loop trough ratings and add star imgs if rating exists 
let ratings = $(".rating")
for (i = 0; i < ratings.length; i++) {
    let ratingParsed = parseFloat(ratings[i].innerHTML)
    if (ratingParsed > 0) {
        generateImages(ratingParsed, i)
    } else {
        ratings[i].innerHTML = ''
    }
}

// Generate stars, half star if rating over .5
function generateImages(rating, target) {
    let ratingNum = ratings[i].innerHTML;
    ratings[i].innerHTML = '';
    let roundedRating = Math.round(rating);
    if (roundedRating <= rating) {
        for (i = 0; i < roundedRating; i++) {
            fullStar(target);
        }
    } else if (roundedRating > rating) {
        let i = 0;
        for (i; i < roundedRating - 1; i++) {
            fullStar(target);
        }
        $($(".rating")[target]).append("<img src='https://owl-and-hoot.s3.amazonaws.com/static/images/star-half-full.png'></img>");
    }
    $($(".rating")[target]).append(`<p>${ratingNum}</p>`);
}

function fullStar(target) {
    $($(".rating")[target]).append("<img src='https://owl-and-hoot.s3.amazonaws.com/static/images/star-full.png'></img>");
}
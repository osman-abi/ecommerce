$(document).ready(function () {
    $('#owl-carousel-item-same').owlCarousel({
        loop: false,
        margin: 9,
        nav: false,
        autoplay: false,
        dots: true,
        responsive: {
            0: {
                items: 1,
            },
            536: {
                items: 2,
            },
            794: {
                nav: true,
            },
            800: {
                nav: true,
                items: 3,
            },
            1120: {
                nav: true,
                items: 4,
            }

        }
    });

    document.querySelectorAll('.product-features-questions').forEach(function (element) {
        element.addEventListener('click', function () {
            let product_features_question_answer = element.closest('.product-features-question-answer')
            let product_features_answer = product_features_question_answer.querySelector('.product-features-answers')
            if (product_features_answer.style.maxHeight) {
                product_features_answer.style.maxHeight = null;
                product_features_question_answer.querySelector('i').style.transform = "rotate(90deg)"
            } else {
                product_features_answer.style.maxHeight = product_features_answer.scrollHeight + "px";
                product_features_question_answer.querySelector('i').style.transform = "rotate(-90deg)"
                product_features_question_answer.querySelector('i').style.transition = "transform 0.5s"
            }
        })
    })
});
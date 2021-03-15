$(document).ready(function () {

    $('#owl-carousel-first').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        items: 1,
        autoplay: true,
        responsive: {
            769: {
                nav: true,
            },
        }
    });

    $('#owl-carousel-blog').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        items: 4,
        autoplay: true,
        responsive: {
            0: {
                items: 1,
            },
            500: {
                items: 2,
            },
            700: {
                items: 3,
            },
            769: {
                nav: true,
                items: 3,
            },
            1000: {
                nav: true,
                items: 4,
            }

        }
    });

    $('#owl-carousel-partner').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        items: 8,
        autoplay: true,
        responsive: {
            0: {
                items: 3,
            },
            361: {
                items: 3,
            },
            470: {
                items: 4,
            },
            644: {
                items: 5,
            },
            769: {
                nav: true,
            },
            800: {
                nav: true,
                items: 6,
            },
            1120: {
                nav: true,
                items: 7,
            }

        }
    });

    $('#owl-carousel-last-viewed-item').owlCarousel({
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

    $('#owl-carousel-category').owlCarousel({
        loop: false,
        margin: 20,
        nav: false,
        items: 6,
        // autoplay:true,
        responsive: {
            0: {
                items: 2,
            },
            361: {
                items: 2,
            },
            550: {
                items: 3,
            },
            720: {
                items: 4,
            },
            950: {
                nav: true,
                dots: true,
                items: 5,
            },
            1120: {
                nav: true,
                dots: false,
                items: 6,
            }

        }
    });

    $('#owl-carousel-quick-view').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        items: 1,
        autoplay: false,
        dots: false,
    });

    $(window).scroll(function () {
        if ($(this).scrollTop() >= 400) {
            $('#scroll_top').fadeIn("fast");
        } else {
            $('#scroll_top').fadeOut("fast");
        }
    });

    $('#scroll_top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 500);
    });

    $('.linkjoin').click(function (click) {
        click.preventDefault();
        $('.joinj').val('');
        $('#form-join2,#form-join').toggle();
        $('.input-signup,.signup2,.welcome,.text-secondary,.text-secondary2,.q1-modal,.q2-modal,.reset-modal').toggle();

        if ($('.linkjoin').text() == 'Daxil ol') {
            $('.linkjoin').text('Qeydiyyat');
        }
        else {
            $('.linkjoin').text('Daxil ol');
        }

    })
    var menu_button = document.querySelector('.menu-button')
    var menu_content = document.querySelector('.menu-content')
    var main_header_wrapper = document.querySelector('.main_header_wrapper')
    var body = document.querySelector('body')
    menu_button.addEventListener('click', function () {
        if (menu_button.classList.contains('is-active')) {
            menu_button.classList.remove('is-active');
            menu_content.classList.add('close');
            menu_content.classList.remove('open');
            main_header_wrapper.classList.remove('fix_position');
            body.classList.remove('overflow_hidden');
        }
        else {
            menu_button.classList.add('is-active');
            menu_content.classList.remove('close');
            menu_content.classList.add('open');
            main_header_wrapper.classList.add('fix_position');
            body.classList.add('overflow_hidden');
        }
    })

    document.querySelectorAll('.arrow').forEach(function (e) {
        e.querySelector('i').addEventListener('click', function () {
            event.preventDefault()
            if (e.querySelector('i').classList.contains('fa-plus')) {
                e.classList.add('open');
                e.closest('.menu__link').classList.add('active-parent');
                e.closest('.menu__item').querySelector('.menu__sub-menu').classList.add('open');
                // e.closest('.menu__item').querySelector('.menu__sub-menu').style.display='block';
                e.querySelector('i').classList.remove('fa-plus');
                e.querySelector('i').classList.add('fa-minus');
            }
            else {
                e.classList.remove('open');
                e.closest('.menu__link').classList.remove('active-parent');
                e.closest('.menu__item').querySelector('.menu__sub-menu').classList.remove('open');
                // e.closest('.menu__item').querySelector('.menu__sub-menu').style.display='none';
                e.querySelector('i').classList.add('fa-plus');
                e.querySelector('i').classList.remove('fa-minus');
            }

        })

    })
    if (document.querySelector('.all-popular-categories-view')) {
        document.querySelector('.all-popular-categories-view').addEventListener('click', function () {
            document.querySelector('.popular_categories_widget_ul').style.maxHeight = "100%";
            document.querySelector('.all-popular-categories-view').style.display = "none"
            document.querySelector('.not-all-popular-categories-view').style.display = "block"
        })
    }

    if (document.querySelector('.not-all-popular-categories-view')) {
        document.querySelector('.not-all-popular-categories-view').addEventListener('click', function () {
            document.querySelector('.popular_categories_widget_ul').style.maxHeight = "640px";
            document.querySelector('.not-all-popular-categories-view').style.display = "none"
            document.querySelector('.all-popular-categories-view').style.display = "block"
        })
    }


    var alphabet_dropdown = document.querySelector('.alphabet-dropdown');
    var price_dropdown = document.querySelector('.price-dropdown')
    var new_or_old_dropdown = document.querySelector('.new-or-old-dropdown')
    var queue_dropdown = document.querySelector('.queue-dropdown')
    var queue_dropdown_mobile = document.querySelector('.queue-dropdown-mobile')

    document.onclick = function (e) {
        if (alphabet_dropdown) {
            if (!e.target.closest('.alphabet-dropdown')) {
                document.querySelector('.alphabet-dropdown-list').classList.remove('d-block')
                document.querySelector('.alphabet-dropdown-list').classList.add('d-none')
                document.querySelector('.alphabet-dropdown-list').closest('.header-tag-filter').querySelector('i').classList.add('fa-caret-down')
                document.querySelector('.alphabet-dropdown-list').closest('.header-tag-filter').querySelector('i').classList.remove('fa-caret-up')
            }
        }

        if (price_dropdown) {
            if (!e.target.closest('.price-dropdown')) {
                document.querySelector('.price-dropdown-list').classList.remove('d-block')
                document.querySelector('.price-dropdown-list').classList.add('d-none')
                document.querySelector('.price-dropdown-list').closest('.header-tag-filter').querySelector('i').classList.add('fa-caret-down')
                document.querySelector('.price-dropdown-list').closest('.header-tag-filter').querySelector('i').classList.remove('fa-caret-up')
            }
        }

        if (new_or_old_dropdown) {
            if (!e.target.closest('.new-or-old-dropdown')) {
                document.querySelector('.new-or-old-dropdown-list').classList.remove('d-block')
                document.querySelector('.new-or-old-dropdown-list').classList.add('d-none')
                document.querySelector('.new-or-old-dropdown-list').closest('.header-tag-filter').querySelector('i').classList.add('fa-caret-down')
                document.querySelector('.new-or-old-dropdown-list').closest('.header-tag-filter').querySelector('i').classList.remove('fa-caret-up')
            }
        }

        if (queue_dropdown) {
            if (!e.target.closest('.queue-dropdown')) {
                document.querySelector('.queue-dropdown-list').classList.remove('d-block')
                document.querySelector('.queue-dropdown-list').classList.add('d-none')
            }
        }

        if (queue_dropdown_mobile) {
            if (!e.target.closest('.queue-dropdown-mobile')) {
                document.querySelector('.queue-dropdown-list-mobile').classList.remove('d-block')
                document.querySelector('.queue-dropdown-list-mobile').classList.add('d-none')
            }
        }

        if (!e.target.closest('.favorite-icon-header') && !e.target.closest('.shopping-icon-header')) {
            if (!e.target.closest('.right-side-line')) {
                document.querySelector('.line-side').classList.remove('line-side-openn')
                document.querySelector('.line-side').classList.add('line-side-closee');
            }
        }

    }

    document.querySelector('.favorite-icon-header').addEventListener('click', function () {
        console.log('bb')
        document.querySelector('.line-side').classList.add('line-side-openn')
        document.querySelector('.line-side').classList.remove('line-side-closee');
        document.querySelector('#v-pills-favorite-tab').click();
    })
    document.querySelector('.shopping-icon-header').addEventListener('click', function () {
        document.querySelector('.line-side').classList.add('line-side-openn')
        document.querySelector('.line-side').classList.remove('line-side-closee');
        document.querySelector('#v-pills-heart-tab').click();
    })

    document.querySelectorAll('.dropdownn-filter').forEach(function (e) {
        e.addEventListener('click', function () {
            if (e.closest('.header-tag-filter').querySelector('.dropdownn-filter-list').classList.contains('d-none')) {
                e.closest('.header-tag-filter').querySelector('.dropdownn-filter-list').classList.remove('d-none')
                e.closest('.header-tag-filter').querySelector('.dropdownn-filter-list').classList.add('d-block')
                if (e.closest('.header-tag-filter').querySelector('i').classList.contains('fa')) {
                    e.closest('.header-tag-filter').querySelector('i').classList.remove('fa-caret-down')
                    e.closest('.header-tag-filter').querySelector('i').classList.add('fa-caret-up')
                }

            }
            else {
                e.closest('.header-tag-filter').querySelector('.dropdownn-filter-list').classList.remove('d-block')
                e.closest('.header-tag-filter').querySelector('.dropdownn-filter-list').classList.add('d-none')
                if (e.closest('.header-tag-filter').querySelector('i').classList.contains('fa')) {
                    e.closest('.header-tag-filter').querySelector('i').classList.add('fa-caret-down')
                    e.closest('.header-tag-filter').querySelector('i').classList.remove('fa-caret-up')
                }
            }
        })
    })

    document.querySelectorAll('.alphabet-type-list').forEach(function (element) {
        element.addEventListener('click', function () {
            let list_option = element.innerText
            document.querySelector('.alphabet-dropdown-featured').innerText = list_option
        })
    })

    document.querySelectorAll('.price-type-list').forEach(function (element) {
        element.addEventListener('click', function () {
            let list_option = element.innerText
            document.querySelector('.price-dropdown-featured').innerText = list_option
        })
    })

    document.querySelectorAll('.new-or-old-type-list').forEach(function (element) {
        element.addEventListener('click', function () {
            let list_option = element.innerText
            document.querySelector('.new-or-old-dropdown-featured').innerText = list_option
        })
    })

    document.querySelectorAll('.queue-type-list').forEach(function (element) {
        element.addEventListener('click', function () {
            let list_option = element.innerText
            document.querySelector('.queue-dropdown-featured').innerText = list_option
        })
    })

    document.querySelectorAll('.queue-type-list-mobile').forEach(function (element) {
        element.addEventListener('click', function () {
            let list_option = element.innerText
            document.querySelector('.queue-dropdown-featured-mobile').innerHTML = `<i
          class="material-icons">swap_vert</i>` + list_option
        })
    })



    document.querySelectorAll('.filter-name').forEach(function (e) {
        e.addEventListener('click', function () {
            let subfilter_name = e.getAttribute('name');
            if (!e.classList.contains('open_filter')) {
                document.querySelectorAll('.filter-name').forEach(function (elem) {
                    elem.classList.remove('open_filter');
                    elem.querySelector('i').classList.add('fa-caret-down')
                    elem.querySelector('i').classList.remove('fa-caret-up')
                })
                document.querySelector('.filters_inner_wrapper').querySelectorAll('.filters_inner_list').forEach(function (filter_el) {
                    filter_el.classList.remove('active_filter')
                })
                e.classList.add('open_filter');
                e.querySelector('i').classList.remove('fa-caret-down')
                e.querySelector('i').classList.add('fa-caret-up')
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.visibility = 'visible'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.padding = '30px 0px'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.opacity = '1'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.maxHeight = '2000px'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.transition = 'max-height 0.8s ease 0s, opacity 0.1s ease 0s, visibility 0.3s ease 0s'
                e.closest('.product_filters_container').querySelectorAll(`[name=${subfilter_name}]`)[1].classList.add('active_filter')

            }
            else {
                e.querySelector('i').classList.add('fa-caret-down')
                e.querySelector('i').classList.remove('fa-caret-up')
                e.classList.remove('open_filter');
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.visibility = 'hidden'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.padding = '0px 0px'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.opacity = '0'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.maxHeight = '0px'
                e.closest('.product_filters_container').querySelector('.filters_inner_wrapper').style.transition = '0s ease all'
                e.closest('.product_filters_container').querySelectorAll(`[name=${subfilter_name}]`)[1].classList.remove('active_filter')
            }

        })
    })


    let all_slider_range = document.querySelectorAll('.slider-rangee')
    all_slider_range.forEach(function (elem) {
        $(elem).slider({
            range: true,
            orientation: "horizontal",
            min: 0,
            max: 10000,
            values: [0, 10000],
            step: 100,

            slide: function (event, ui) {
                if (ui.values[0] == ui.values[1]) {
                    return false;
                }
                let filterr_range_container = elem.closest('.for-js-range')
                let min_filter = filterr_range_container.querySelector('.min_filterr')
                let max_filter = filterr_range_container.querySelector('.max_filterr')
                $(min_filter).val(ui.values[0]);
                $(max_filter).val(ui.values[1]);
            }
        });
    })



    var filter_panel = document.querySelector('.filter-panel-opener')
    if (filter_panel) {
        filter_panel.addEventListener('click', function () {
            document.querySelector('.mobile-filter-menu-wrapper').classList.add('open_menu')
            document.querySelector('.mobile_layout_wrapper').classList.add('open-filter-layout-wrapper')
            document.querySelector('html').classList.add('overflow_hidden')
        })
    }


    var mobile_filter_menu_left_side = document.querySelector('.mobile-filter-menu-left-side')
    if (mobile_filter_menu_left_side) {
        mobile_filter_menu_left_side.addEventListener('click', function () {
            document.querySelector('.mobile-filter-menu-wrapper').classList.remove('open_menu')
            document.querySelector('.mobile_layout_wrapper').classList.remove('open-filter-layout-wrapper')
            document.querySelector('html').classList.remove('overflow_hidden')
        })
    }


    document.querySelectorAll('.toggle-icon-div').forEach(function (e) {
        e.querySelector('i').addEventListener('click', function () {
            event.preventDefault()
            if (e.querySelector('i').classList.contains('fa-plus')) {
                e.closest('.mobile-filter').classList.add('open-filter-li');
                e.closest('.mobile-filter').querySelector('.mobile-filter-option-list').classList.add('open');
                e.querySelector('i').classList.remove('fa-plus');
                e.querySelector('i').classList.add('fa-minus');
            }
            else {
                e.closest('.mobile-filter').classList.remove('open-filter-li');
                e.closest('.mobile-filter').querySelector('.mobile-filter-option-list').classList.remove('open');
                e.querySelector('i').classList.add('fa-plus');
                e.querySelector('i').classList.remove('fa-minus');
            }

        })

    });

    var icon_list_view = document.querySelector('.list-view-icon');
    if (icon_list_view) {
        document.querySelector('.list-view-icon').addEventListener('click', function () {
            this.querySelector('i').classList.add('active-view');
            let table_view_icon = document.querySelector('.table-view-icon');
            table_view_icon.querySelector('i').classList.remove('active-view');
            document.querySelector('.list-view-item-all').style.maxHeight = "10000px";
            document.querySelector('.list-view-item-all').style.opacity = "1"
            document.querySelector('.list-view-item-all').style.transition = "opacity 0.5s";
            document.querySelector('.all-items-view-table').style.maxHeight = "0px";
            document.querySelector('.all-items-view-table').style.opacity = "0"
            document.querySelector('.all-items-view-table').style.transition = "opacity 0s";
        })
    }


    var icon_table_view = document.querySelector('.table-view-icon');
    if (icon_table_view) {
        document.querySelector('.table-view-icon').addEventListener('click', function () {
            this.querySelector('i').classList.add('active-view');
            let list_view_icon = document.querySelector('.list-view-icon');
            list_view_icon.querySelector('i').classList.remove('active-view');
            document.querySelector('.all-items-view-table').style.maxHeight = "10000px";
            document.querySelector('.all-items-view-table').style.opacity = "1";
            document.querySelector('.all-items-view-table').style.transition = "opacity 0.5s";
            document.querySelector('.list-view-item-all').style.maxHeight = "0px";
            document.querySelector('.list-view-item-all').style.opacity = "0";
            document.querySelector('.list-view-item-all').style.transition = "opacity 0s";
        })
    }



    //   .........................................basket.............................................
    document.querySelectorAll('.right-side-opener').forEach(function (e) {
        e.addEventListener('click', function () {
            document.querySelector('.line-side').classList.add('line-side-openn')
            document.querySelector('.line-side').classList.remove('line-side-closee');
        })
    })
    document.querySelectorAll('.exit-svg-right-side').forEach(function (e) {
        e.addEventListener('click', function () {
            document.querySelector('.line-side').classList.remove('line-side-openn')
            document.querySelector('.line-side').classList.add('line-side-closee');
        })
    })




    document.querySelectorAll('.exit-svg-right-side-item').forEach(function (elem) {
        elem.addEventListener('click', function () {
            updateCartTotal(elem)
            elem.closest('.inside-right-side-item').remove();

        })
    })


    function updateCartTotal(x) {
        var sum = x.closest('.inside-right-side-item').querySelector('.price-right-side-item').innerText;
        sum = parseInt(sum.split(" ")[0])
        console.log(sum)
    }




    // ..................when scroll up > menu Show.............................
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function () {
        var currentScrollPos = window.pageYOffset;
        if (currentScrollPos < 240) {
            document.querySelector(".middle_header_wrapper").style.opacity = "1";
            document.querySelector(".middle_header_wrapper").classList.remove('scroll-fixed');

            // for-mobile
            document.querySelector(".main_header_wrapper").style.opacity = "1";
            document.querySelector(".main_header_wrapper").classList.remove('scroll-fixed');

        }
        else if (prevScrollpos > currentScrollPos) {
            document.querySelector(".middle_header_wrapper").classList.add('scroll-fixed');
            document.querySelector(".middle_header_wrapper").style.opacity = "1";
            document.querySelector(".middle_header_wrapper").maxHeight = "10000px !important";

            // for-mobile
            document.querySelector(".main_header_wrapper").classList.add('scroll-fixed');
            document.querySelector(".main_header_wrapper").style.opacity = "1";
            document.querySelector(".main_header_wrapper").maxHeight = "10000px !important";
        }
        else {
            if (document.querySelector('.scroll-fixed')){
                document.querySelector(".scroll-fixed").style.opacity = "0 !important";
                document.querySelector(".scroll-fixed").maxHeight = "0";
                document.querySelector(".middle_header_wrapper").style.opacity = "0";

                // for-mobile
                document.querySelector(".main_header_wrapper").style.opacity = "0";
            }else{
                document.querySelector(".middle_header_wrapper").style.opacity = "0";
                
                // for-mobile
                document.querySelector(".main_header_wrapper").style.opacity = "0";
            }
        }
        prevScrollpos = currentScrollPos;
    }

    document.querySelectorAll('.product-features-questions-quick-view').forEach(function (element) {
        element.addEventListener('click', function () {
            let product_features_question_answer = element.closest('.product-features-question-answer-quick-view')
            let product_features_answer = product_features_question_answer.querySelector('.product-features-answers-quick-view')
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
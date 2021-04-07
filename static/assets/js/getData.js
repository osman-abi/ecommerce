const data_url = '/get_data/'
const element = document.querySelectorAll(".category")
for (const i of element) {
    i.addEventListener("click", checkElement)
    function checkElement(e) {
        if (e.target.checked) {
            fetch(data_url).then(res => res.json()).then(data => {
                console.log(data)
                data.sort((a, b) => {
                    console.log(a,'-->',b)
                })
            for (const j of data) {
                for (const z of j.fields.colors) {

                    if (i.dataset.category == z) {
                        let filtered_data = document.getElementById("filtered_data");
                        document.getElementById("table").style.display = 'none';

                        filtered_data.innerHTML=
                            `<div class="each-items col-lg-3 rt-item" product_slug="slug1">
                    <div class="items-height" style="padding: 25px 30px 0px 30px ">
                        <div style="padding-top: 100%" class="position-relative">
                            <a class="position-absolute h-100 w-100" style="top:0" href="">
                                <img class="all-images w-100 h-100 item-images" src="{{${j.fields.thumbnail}}}"
                                    alt="">
                            </a>
                            <div class="credit-duration">0₼ 0% 12 ay</div>
                            <div class="items-svg position-absolute">
                                <div title="Seçilmiş et" class="svg-filess">
                                    <i style="color: white" class="fa fa-heart" id="fav" data-product="{{ ${j.fields.slug} }}" data-action="add"
                                 onclick="addToFavourite()" aria-hidden="true"></i>
                                </div>
                                <div title="Müqayisə et" class="svg-filess">
                                    <i style="color: white" class="fas fa-balance-scale-right" aria-hidden="true"></i>
                                </div>
                                <div data-toggle="modal" data-target="#oneClickModal" title="1 kliklə alma" class="svg-filess">
                                    <i style="color: white" class="fas fa-hand-point-up" aria-hidden="true"></i>
                                </div>
                                <div data-toggle="modal" data-target="#quickViewModal" title="Sürətli baxış" class="svg-files-quick svg-filess">
                                    <i style="color: white" class="fas fa-clock" aria-hidden="true"></i>
                                </div>
                            </div>
                        </div>
                        <div class="item-info">
                            <div class="rating">
                                <div class="votes_block nstar">
                                    <div class="ratings">
                                        <div class="inner_rating">
                                            <div class="item-rating" title="1">
                                                <i class="fas fa-star"></i></div>
                                            <div class="item-rating " title="2"><i class="fas fa-star"></i></div>
                                            <div class="item-rating " title="3"><i class="fas fa-star"></i></div>
                                            <div class="item-rating " title="4"><i class="fas fa-star"></i></div>
                                            <div class="item-rating" title="5"><i class="fas fa-star"></i></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="item-title" style="height: 44px;">
                                <a href="{% url 'product_detail' ${j.fields.slug} %}"
                                    class="dark_link option-font-bold font_sm" id="category_product" ><span>${j.fields.name}</span></a>
                            </div>
                            <div class="sa_block" data-fields="null" data-stores="[]" data-user-fields="null"
                                style="height: 44px;">
                                <div class="cost prices clearfix" style="height: 167px;">
                                    <div class="icons-basket-wrapper offer_buy_block ce_cmp_hidden">
                                        <div class="button_block">
                                            <span title="Səbətə əlavə et" style="width: 38px;height:38px"
                                                class="insert-basket d-flex justify-content-center align-items-center btn-exlg to-cart btn btn-default transition_bg animate-load has-ripple">
                                                <i style="color: #999" data-product="{{ ${j.fields.slug} }}" data-action="add" id="add" onclick="addToCart()" class="fas fa-shopping-cart"
                                                    aria-hidden="true"></i></span>
                                          
                                        </div>
                                    </div>
                                    <div class="price_matrix_wrapper ">
                                        <div class="d-flex for-credit">
                                            <div>Kreditle:</div>
                                            <div class="ml-1 credit-price align-items-center">2865 ₼</div>
                                        </div>
                                        <div class="d-flex cash-price align-items-center">
                                            <div>Nağd:</div>
                                            <div class="cash-price-percent">-{{${j.fields.sale}}}%</div>
                                            <div class="ml-1 cash-pricee">{{${j.fields.rest_price}}} ₼</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>`
                        
                    } else {
                        document.getElementById("filtered_data").style.display = 'none'
                        document.getElementById("table").style.display = 'none'
                    }
                }
            }
        })
        } else {
            document.getElementById("table").style.display = 'block'
            document.getElementById("filtered_data").style.display = 'none'
        }
    }
}


function filterData() {
    const filtered_data = document.getElementById("filtered_data")
    
    const minGenVal = document.getElementById("min_filterr").valueAsNumber
    const maxGenVal = document.getElementById("max_filterr").valueAsNumber
    const minDerVal = document.getElementById("min_filterr2").valueAsNumber
    const maxDerVal = document.getElementById("max_filterr2").valueAsNumber
    const minUznVal = document.getElementById("min_filterr3").valueAsNumber
    const maxUznVal = document.getElementById("max_filterr3").valueAsNumber
    fetch(data_url).then(res => res.json()).then(data => {
        for (const i of data) {
            if (i.fields.genislik > minGenVal && i.fields.genislik < maxGenVal || i.fields.derinlik>minDerVal && i.fields.derinlik < maxDerVal || i.fields.uzunluq > minUznVal && i.fields.uzunluq < maxUznVal) {
                document.getElementById("table").style.display = 'none'
                filtered_data.innerHTML =
                    `<div class="each-items col-lg-3 rt-item" product_slug="slug1">
                    <div class="items-height" style="padding: 25px 30px 0px 30px ">
                        <div style="padding-top: 100%" class="position-relative">
                            <a class="position-absolute h-100 w-100" style="top:0" href="">
                                <img class="all-images w-100 h-100 item-images" src="{{}}"
                                    alt="">
                            </a>
                            <div class="credit-duration">0₼ 0% 12 ay</div>
                            <div class="items-svg position-absolute">
                                <div title="Seçilmiş et" class="svg-filess">
                                    <i style="color: white" class="fa fa-heart" id="fav" data-product="{{ ${i.fields.slug} }}" data-action="add"
                                 onclick="addToFavourite()" aria-hidden="true"></i>
                                </div>
                                <div title="Müqayisə et" class="svg-filess">
                                    <i style="color: white" class="fas fa-balance-scale-right" aria-hidden="true"></i>
                                </div>
                                <div data-toggle="modal" data-target="#oneClickModal" title="1 kliklə alma" class="svg-filess">
                                    <i style="color: white" class="fas fa-hand-point-up" aria-hidden="true"></i>
                                </div>
                                <div data-toggle="modal" data-target="#quickViewModal" title="Sürətli baxış" class="svg-files-quick svg-filess">
                                    <i style="color: white" class="fas fa-clock" aria-hidden="true"></i>
                                </div>
                            </div>
                        </div>
                        <div class="item-info">
                            <div class="rating">
                                <div class="votes_block nstar">
                                    <div class="ratings">
                                        <div class="inner_rating">
                                            <div class="item-rating" title="1">
                                                <i class="fas fa-star"></i></div>
                                            <div class="item-rating " title="2"><i class="fas fa-star"></i></div>
                                            <div class="item-rating " title="3"><i class="fas fa-star"></i></div>
                                            <div class="item-rating " title="4"><i class="fas fa-star"></i></div>
                                            <div class="item-rating" title="5"><i class="fas fa-star"></i></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="item-title" style="height: 44px;">
                                <a href="{% url 'product_detail' ${i.fields.slug} %}"
                                    class="dark_link option-font-bold font_sm" id="category_product" ><span>${i.fields.name}</span></a>
                            </div>
                            <div class="sa_block" data-fields="null" data-stores="[]" data-user-fields="null"
                                style="height: 44px;">
                                <div class="cost prices clearfix" style="height: 167px;">
                                    <div class="icons-basket-wrapper offer_buy_block ce_cmp_hidden">
                                        <div class="button_block">
                                            <span title="Səbətə əlavə et" style="width: 38px;height:38px"
                                                class="insert-basket d-flex justify-content-center align-items-center btn-exlg to-cart btn btn-default transition_bg animate-load has-ripple">
                                                <i style="color: #999" data-product="{{ ${i.fields.slug} }}" data-action="add" id="add" onclick="addToCart()" class="fas fa-shopping-cart"
                                                    aria-hidden="true"></i></span>
                                          
                                        </div>
                                    </div>
                                    <div class="price_matrix_wrapper ">
                                        <div class="d-flex for-credit">
                                            <div>Kreditle:</div>
                                            <div class="ml-1 credit-price align-items-center">2865 ₼</div>
                                        </div>
                                        <div class="d-flex cash-price align-items-center">
                                            <div>Nağd:</div>
                                            <div class="cash-price-percent">-{{${i.fields.sale}}}%</div>
                                            <div class="ml-1 cash-pricee">{{${i.fields.rest_price}}} ₼</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>`
            } else {
                document.getElementById("table").style.display = 'block'
            }
        }
    })
}

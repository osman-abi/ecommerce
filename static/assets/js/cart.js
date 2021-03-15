var addCart = document.getElementById('add');

function addToCart(){
    let productSlug = addCart.dataset.product
    let action = addCart.dataset.action
    if (user == 'AnonymousUser') {
        addCookieCart(productSlug,action)
    } else {
        addAuthenticatedCart(productSlug, action)
    }
};

function addAuthenticatedCart(productSlug, action) {
    var url = '/sebet/add_to_cart/';
    var data = {
        'productSlug': productSlug,
        'action':action
    }
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify(data)
    })
        .then(response => {
            console.log(response.status)
            location.reload()
        })
};

function addCookieCart(productSlug, action) {
    console.log('user not found')
    if (action =='add') {
        if (cart[productSlug] == undefined) {
            cart[productSlug] = {
                'quantity': 1
            }
        } else {
        cart[productSlug]['quantity'] ++
        };
    };
    
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
    location.reload()
}


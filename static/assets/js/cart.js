var addCart = document.getElementById('add');

function addToCart(){
    let productSlug = addCart.dataset.product
    let action = addCart.dataset.action
    console.log('slug',productSlug)
    if (user == 'AnonymousUser') {
        addCookieCart(productSlug,action)
    } else {
        addAuthenticatedCart(productSlug, action)
    }
};

function updateCart() {
    let productSlug = addCart.dataset.product
    let action = addCart.dataset.action
    // console.log('action -->', action)
    if (user == 'AnonymousUser') {
        updateCookieCart(productSlug,action)
    } else {
        updatedCart(productSlug,action)
        
    }
}

updateCookieCart = (productSlug,action)=>{
    var arr = document.cookie.split(";")
    // console.log(arr)
    for (const i of arr) {
        var name = i.split("=")[0]
        var value = i.split("=")[1]
        // console.log(name)
        if (name == ' cart') {
            // console.log(name)
            var cartItem = JSON.parse(value)
            if (action == 'minus') {
                cartItem[productSlug]['quantity']--
                
            }
            document.cookie = 'cart=' + JSON.stringify(cartItem) + ';domain=;path=/'
        }
    }
}

function removeFromCart() {
    let removeBtn = document.getElementById("remove")
    let productSlug = removeBtn.dataset.product
    let action = removeBtn.dataset.action
    updatedCart(productSlug,action)
}
function updatedCart(productSlug, action) {
    var url = '/sebet/update_cart/'
    var data = {
        'productSlug': productSlug,
        'action':action
    }
    fetch(url, {
        method: "POST",
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify(data)
    })
        .then(response => {
            console.log(response.status)
            // location.reload()
        })
        
    
}

function addAuthenticatedCart(productSlug, action) {
    var url = '/sebet/add_to_cart/';
    var data = {
        'productSlug': productSlug,
        'action':action
    }
    console.log(productSlug)
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
            // location.reload()
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
    // location.reload()
}


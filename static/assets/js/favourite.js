var fav = document.getElementById('fav')
function addToFavourite() {
    let productSlug = fav.dataset.product
    let action = fav.dataset.action
    addCookieFavourite(productSlug,action)
}

function addCookieFavourite(productSlug, action) {
    if (action == 'add') {
        if (favourite[productSlug] == undefined) {
            favourite[productSlug] = {
                'quantity': 1
            }
        } else {
            favourite[productSlug]['quantity'] ++
        }
    }
    document.cookie = 'favourite=' + JSON.stringify(favourite) + ';domain=;path=/'
    location.reload()
    console.log('favourite', favourite)
}

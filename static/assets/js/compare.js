const compareButton = document.getElementById("com")

function addToCompare() {
    var data = compareButton.dataset.product
    var action = compareButton.dataset.action
    console.log(`true`)
    addCookieCompare(data,action)
}

function addCookieCompare(data, action) {
    
    if (action == 'add') {
        if (compare[data] == undefined) {
            compare[data] = {
                'quantity': 1
            }
        } else {
            compare[data]['quantity'] ++
        }
    }
    document.cookie = 'compare=' + JSON.stringify(compare) + ';domain=;path=/'
    location.reload()
    // console.log('favourite', favourite)
}
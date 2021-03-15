$(document).ready(function () {





  var insert_basket_icon = document.querySelectorAll('.insert-basket');
  insert_basket_icon.forEach(function (e) {
    e.addEventListener('click', function () {
      e.style.borderColor = "#49bd68";
      e.querySelector('i').style.color = "#49bd68";
      let rt_item = e.closest('.rt-item');
      let product_slug = rt_item.getAttribute('product_slug');
      insert_basket_icon.forEach(function (elem) {
        let rt_item_2 = elem.closest('.rt-item');
        let product_slug_2 = rt_item_2.getAttribute('product_slug');
          if (product_slug==product_slug_2){
            elem.style.borderColor = "#49bd68";
            elem.querySelector('i').style.color = "#49bd68";
          }
      })
    })
  })

  


})
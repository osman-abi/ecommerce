// $('#timer1').syotimer({
//     year: 2021,
//     month: 1,
//     day: 6,
//     hour: 20,
//     minute: 30
//   });
$(document).ready(function() {
let timer_time = document.querySelectorAll('.countdown');
timer_time.forEach(function(e){
    let class_timer = e.getAttribute('class')
    let data_count = e.getAttribute('data-count');

    $('.'+class_timer).countdown({
    date: data_count,
    });
})
})

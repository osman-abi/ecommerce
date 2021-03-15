$(document).ready(function() {
    let timer_time = document.querySelectorAll('.countdown-campaign-detail');
    timer_time.forEach(function(e){
        let class_timer = e.getAttribute('class')
        let data_count = e.getAttribute('data-count');
    
        $('.'+class_timer).countdown({
        date: data_count,
        });
    })
    })
$(document).ready(function() {

    document.querySelectorAll('.most-asked-questions').forEach(function(element){
        element.addEventListener('click',function(){
            let most_asked_question_answer = element.closest('.most-asked-question-answer')
            let most_asked_answer = most_asked_question_answer.querySelector('.most-asked-answers')
            if (most_asked_answer.style.maxHeight){
                most_asked_answer.style.maxHeight = null;
                most_asked_question_answer.querySelector('i').style.transform="rotate(90deg)"
              } else {
                most_asked_answer.style.maxHeight = most_asked_answer.scrollHeight + "px";
                most_asked_question_answer.querySelector('i').style.transform="rotate(-90deg)"
                most_asked_question_answer.querySelector('i').style.transition="transform 0.5s"
              } 
        })
    })

})
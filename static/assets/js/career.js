$(document).ready(function() {

    document.querySelectorAll('.career-questions').forEach(function(element){
        element.addEventListener('click',function(){
            let career_question_answer = element.closest('.career-question-answer')
            let career_answer = career_question_answer.querySelector('.career-answers')
            if (career_answer.style.maxHeight){
                career_answer.style.maxHeight = null;
                career_question_answer.querySelector('i').style.transform="rotate(90deg)"
              } else {
                career_answer.style.maxHeight = career_answer.scrollHeight + "px";
                career_question_answer.querySelector('i').style.transform="rotate(-90deg)"
                career_question_answer.querySelector('i').style.transition="transform 0.5s"
              } 
        })
    })

})
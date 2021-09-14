function fetchAndApply() {

    const API_KEY = "API_KEY_HERE"

    fetch(`https://degerlendirenzeka-deploy.herokuapp.com/api/database/getAllQuestions?apikey=${API_KEY}`)
        .then(response => response.json())
        .then(jsonData => {
            renderElements(jsonData);

        })
}


function renderElements(data) {

    let questionVal = 1;
    data.forEach(element => {

       

        let id = element.id;
        let questionText = element["question_text"];


        /*
        Question 1 was our question that we've used to create the prototype. Because of
        some confusions that people has experienced when they use the website, we've decided to remove it from the "help us!" page. Instead, we're
        going to collect the data that people write in the prototype page.
        */
        if (id == 1) {
            return;
        }

        let questionContainerElement = document.createElement("div");
        questionContainerElement.setAttribute("class", "question-container");
        questionContainerElement.setAttribute("id", id)

        let questionTextElement = document.createElement("p");
        questionTextElement.setAttribute("class", "question-text");
        questionTextElement.innerHTML = `SORU ${questionVal}: <br>${questionText}`;

        let textAreaElement = document.createElement("textarea");
        textAreaElement.setAttribute("class", "question-textarea");
        textAreaElement.setAttribute("placeholder","Cevabınızı buraya giriniz.");

        let pushButtonElement = document.createElement("button");
        pushButtonElement.setAttribute("class", "question-button");
        pushButtonElement.innerHTML = "Gönder!";

        pushButtonElement.onclick = function () {

            let questionsId = pushButtonElement.parentElement.getAttribute("id");
            let answerText = textAreaElement.value;
            textAreaElement.value = "";

            let postdata = JSON.stringify({
                answer: answerText,
                question_id: questionsId
            })

            const options = {
                method: 'POST',
                headers: {
                    'Accept': 'application / json',
                    'Content-Type': 'application/json'
                },
                body: postdata
            };

            fetch('https://degerlendirenzeka-deploy.herokuapp.com/api/database/addAnswer', options)
                .then(response => response.json())
                .then(response => {
                   if(response.result == "Successful") {
                       alert("Katkınız için teşekkür ederiz!")

                   }
                   else if(response.result == "Failed") {
                        alert("Sunucularımızda bir problem var gibi görünüyor, verdiğimiz rahatsızlık sebebiyle özür dileriz.")
                   }

                });

        }

        questionContainerElement.appendChild(questionTextElement);
        questionContainerElement.appendChild(textAreaElement);
        questionContainerElement.appendChild(document.createElement("br"));
        questionContainerElement.appendChild(document.createElement("br"));
        questionContainerElement.appendChild(pushButtonElement);

        let mainQuestionContainer = document.getElementById("main-question-container");
        mainQuestionContainer.appendChild(questionContainerElement);

        questionVal = questionVal + 1;

    });
}


window.onload = function () {


    fetchAndApply()

}
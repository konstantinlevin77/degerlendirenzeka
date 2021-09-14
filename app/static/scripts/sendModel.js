window.onload = function () {

    const API_KEY = "YOUR_API_KEY_HERE";

    let button = document.getElementById("send-button");

    button.onclick = function () {

        console.log("Button clicked!!!!");
        let jsonData = JSON.stringify({
            answer: document.getElementById("answer-area").value
        })

        console.log(jsonData)



        let options = {
            method: 'POST',
            headers: {
                'Accept': 'application / json',
                'Content-Type': 'application/json'
            },
            body: jsonData
        };
        fetch('https://degerlendirenzeka-deploy.herokuapp.com/api/model/predict', options)
            .then(response => response.json())
            .then(response => {
                document.getElementById("rcontainer-result-text").innerText = "Değerlendiren Zeka'nın tahminine göre bu cevap"
                document.getElementById("rcontainer-result-percentage").innerText = ` %${response.result} doğru`;

            });

        let postData = JSON.stringify({
            question_id: 1,
            answer: document.getElementById("answer-area").value
        });

        options = {
            method: 'POST',
            headers: {
                'Accept': 'application / json',
                'Content-Type': 'application/json'
            },
            body: postData
        };

        fetch('https://degerlendirenzeka-deploy.herokuapp.com/api/database/addAnswer', options)
            .then(response => response.json())
            .then(response => {

            });
    }





}
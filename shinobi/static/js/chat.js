function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let chatBot = document.querySelector('#chatBot');
chatBot.onsubmit = e => {
    e.preventDefault();
    grabFormData();
};
function grabFormData(){
    let userResposta = document.querySelector('input[name="userResposta"]').value;
    console.log(userResposta);
    let debug = {
      texto: userResposta
    };
    let data = new FormData();
    data.append( "json", JSON.stringify( debug ) );
    return submitForm(data);
}




function submitForm(data){
    let csrftoken = getCookie('csrftoken');
    fetch("/chat",
    {
        headers: {"X-CSRFToken": csrftoken},
        method: "POST",
        body: data
    })
    .then(function(res){ 
        return res.json(); 
    })
    .then(function(data){
       let respostaBot_json = JSON.stringify( data )
       let respostaBot = JSON.parse(respostaBot_json)
       document.querySelector('#conversa').value += respostaBot.texto;
    })
}
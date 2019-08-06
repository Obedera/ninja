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
function chatBot(){
    let chatBot = document.querySelector('#chatBot');
    chatBot.onsubmit = e => {
        e.preventDefault();
    };
    grabFormDataChat();
}
function grabFormDataChat(){
    let userResposta = document.querySelector('input[name="userResposta"]').value;
    document.querySelector('#conversa').value += '\nUser: '+userResposta;
    let debug = {
      texto: userResposta
    };
    let data = new FormData();
    data.append( "json", JSON.stringify( debug ) );
    return submitFormChat(data);
}




function submitFormChat(data){
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
       document.querySelector('#conversa').value += '\nBot: '+respostaBot.texto;
       document.querySelector('input[name="userResposta"]').value = '';
    })
}
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

let form = document.querySelector('form');
form.onsubmit = e => {
    e.preventDefault();
    grabFormData();
};
function grabFormData(){
    let areatexto = document.querySelector('textarea[name="debugtexto"]').value;
    let debug = {
      texto: areatexto
    };
    let data = new FormData();
    data.append( "json", JSON.stringify( debug ) );
    return submitForm(data);
}




function submitForm(data){
    let csrftoken = getCookie('csrftoken');
    fetch("/console",
    {
        headers: {"X-CSRFToken": csrftoken},
        method: "POST",
        body: data
    })
    .then(function(res){ 
        return res.json(); 
    })
    .then(function(data){ 
       document.querySelector('#debug_resposta').value = JSON.stringify( data )  
    })
}
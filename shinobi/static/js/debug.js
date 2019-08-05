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
    let opcao = document.querySelector('select').value;
    if (areatexto == 'html:5'){
        document.querySelector('textarea[name="debugtexto"]').value = '<!DOCTYPE html>\n<html lang="pt-br">\n<head>\n   <meta charset="UTF-8">\n   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n   <meta http-equiv="X-UA-Compatible" content="ie=edge">\n    <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>';       
    }
    else{
        let debug = {
          linguagem: opcao,
          texto: areatexto
        };
        let data = new FormData();
        data.append( "json", JSON.stringify( debug ) );
        return submitForm(data);
    }
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
       let erros_json = JSON.stringify( data )
       let erros = JSON.parse(erros_json)
       document.querySelector('#debug_resposta').value = erros.texto;
    })
}
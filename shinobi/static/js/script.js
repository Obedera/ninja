alert('ok')
function exibirChat(){
    document.querySelector('.chat textarea').classList.toggle('invisivel');
    document.querySelector('.chat div input').classList.toggle('invisivel');
    document.querySelector('.chat div button').classList.toggle('invisivel');   
}
function mostrarCadastro(){
    document.querySelector('#login').classList.toggle('invisivel');
    document.querySelector('#cadastro').classList.toggle('invisivel');
}

function mostrarLogin(){
    document.querySelector('#cadastro').classList.toggle('invisivel');
    document.querySelector('#login').classList.toggle('invisivel');
}
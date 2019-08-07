alert('ok')
function exibirChat(){
    document.querySelector('.chat textarea').classList.toggle('invisivel');
    document.querySelector('.chat div input').classList.toggle('invisivel');
    document.querySelector('.chat div button').classList.toggle('invisivel');   
}
exibirChat()
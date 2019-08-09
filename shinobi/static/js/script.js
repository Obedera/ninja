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

function aumentarFonteConsole(){
    let tamanhoFonte = Number(document.querySelector('textarea[name="debugtexto"]').style.fontSize.split('pt')[0]);
    tamanhoFonte += 1;
    document.querySelector('textarea[name="debugtexto"]').style.fontSize = tamanhoFonte+'pt';
}

function diminuirFonteConsole(){
    let tamanhoFonte = Number(document.querySelector('textarea[name="debugtexto"]').style.fontSize.split('pt')[0]);
    tamanhoFonte -= 1;
    document.querySelector('textarea[name="debugtexto"]').style.fontSize = tamanhoFonte+'pt';
}
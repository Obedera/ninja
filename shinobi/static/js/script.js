function exibirChat(){
    if (document.querySelector('.chat form').style.opacity == 0){
        document.querySelector('.chat form').classList.toggle('invisivel');
        setTimeout(function(){
            document.querySelector('.chat form').style.opacity =1;
        }, 10);
    }
    else{
        document.querySelector('.chat form').style.opacity = 0;
        setTimeout(function(){
            document.querySelector('.chat form').classList.toggle('invisivel');
        }, 600);
    }



    
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
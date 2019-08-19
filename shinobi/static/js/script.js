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

// mover fundo

let fundo = document.querySelector('.ajuste');
let fundoX;
let fundoY;


function moverFundo(e){
    fundoX = (e.pageX * -1 / 15);
    fundoY = (e.pageY * -1 / 15);
    fundo.style.backgroundPosition = fundoX+'px '+fundoY+'px';

}
if (document.querySelector('.login') != null){
    fundo.addEventListener("mousemove",moverFundo);
}

//-----------login
let login = document.getElementById('login');
let cadastro = document.getElementById('cadastro');
let x = document.getElementById('btn');
let image = document.getElementById('shinobi');
if (x != null){
    x.addEventListener('click', function(){
      login.style.display = 'block';
      cadastro.style.display = 'block';
      x.style.display = 'none';
    //   image.style.display = 'none';
    }); 
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

// rolagem automatica


function descer(){
    let i = document.querySelector('html').scrollTop;
    let intervalo = setInterval(() => {
        document.querySelector('html').scrollTop = i+=2;
        if (i >= 800){
            clearInterval(intervalo);
        }
    }, 0.5); 
    document.querySelector('footer').classList.remove('invisivel');
    document.querySelector('.content-main').classList.remove('invisivel');   
}

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

//function mostrarCadastro(){
//   document.querySelector('#login').classList.toggle('invisivel');
//   document.querySelector('#cadastro').classList.toggle('invisivel');
//}

//function mostrarLogin(){
//    document.querySelector('#cadastro').classList.toggle('invisivel');
//    document.querySelector('#login').classList.toggle('invisivel');
//}
//-----------login
let login = document.getElementById('login');
let cadastro = document.getElementById('cadastro');
let x = document.getElementById('btn');
let image = document.getElementById('shinobi');

x.addEventListener('click', function(){
  login.style.display = 'block';
  cadastro.style.display = 'block';
  x.style.display = 'none';
  image.style.display = 'none';
}); 

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
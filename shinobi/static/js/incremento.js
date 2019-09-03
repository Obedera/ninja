let areatexto = document.querySelector('textarea[name="debugtexto"]');
let posicaoFinal
let posicaoUser


function substituir(texto, tamanho){
    posicaoUser = areatexto.selectionStart;
    areatexto = areatexto.value.substring(0,posicaoUser-tamanho)+texto+areatexto.value.substring(posicaoUser);
    console.log((posicaoUser-3)+texto.length);
    posicaoFinal = (posicaoUser-3)+texto.length;
    return areatexto;
}

function pegarTecla(event){
    if (event.keyCode == 13){
        areatexto = document.querySelector('textarea[name="debugtexto"]');
        posicaoUser = areatexto.selectionStart;
        if(areatexto.value.substring(posicaoUser-3,posicaoUser) == 'div'){
            areatexto.value = substituir('<div></div>',3);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
    }
}
areatexto.addEventListener('keydown', pegarTecla);
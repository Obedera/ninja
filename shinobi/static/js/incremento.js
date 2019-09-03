let areatexto = document.querySelector('textarea[name="debugtexto"]');
let posicaoFinal
let posicaoUser


function substituir(texto, tamanho){
    posicaoUser = areatexto.selectionStart;
    areatexto = areatexto.value.substring(0,posicaoUser-tamanho)+texto+areatexto.value.substring(posicaoUser);
    posicaoFinal = (posicaoUser-tamanho)+texto.length;
    console.log(posicaoFinal);
    return areatexto;
}

function pegarTecla(event){
    if (event.keyCode == 13){
        areatexto = document.querySelector('textarea[name="debugtexto"]');
        posicaoUser = areatexto.selectionStart;

        if(areatexto.value.substring(posicaoUser-5,posicaoUser) == 'aside'){
            areatexto.value = substituir('<aside></aside>',5);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
        if(areatexto.value.substring(posicaoUser-3,posicaoUser) == 'div'){
            areatexto.value = substituir('<div></div>',3);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
        if(areatexto.value.substring(posicaoUser-4,posicaoUser) == 'form'){
            areatexto.value = substituir('<form></form>',4);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
        if(areatexto.value.substring(posicaoUser-3,posicaoUser) == 'img'){
            areatexto.value = substituir('<img alt="" src="">',3);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
        if(areatexto.value.substring(posicaoUser-4,posicaoUser) == 'main'){
            areatexto.value = substituir('<main></main>',4);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
        if(areatexto.value.substring(posicaoUser-7,posicaoUser) == 'section'){
            areatexto.value = substituir('<section></section>',7);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
        if(areatexto.value.substring(posicaoUser-6,posicaoUser) == 'select'){
            areatexto.value = substituir('<select></select>',6);
            document.querySelector('textarea[name="debugtexto"]').selectionEnd = posicaoFinal;
        }
    }
}
areatexto.addEventListener('keydown', pegarTecla);
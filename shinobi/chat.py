def analizar_resposta(resposta):
    import random
    div = ['como abre uma div', 'como abrir uma div', 'abrir div','como se abre uma div', 'como abrir div']

    afirmacoes = ['Bom dia','bom dia', 'boa noite', 'Boa noite']

    conte_piada = ['conte uma piada', 'piada', 'conte piada', 'piadas', 'conte umas piadas', 'diga alguma piada','fale uma piada','diga piada','diga uma piada da mastertech']

    piadas_Renan = ['Na mastertech  não se pode usar null, pq tem menor de idade', 'Oi pra quem me conhece eu sou o renan, pra quem não me conhece eu sou o renan']
    piadas_Joao = ['Existe uma grande diferença entre models e top models','Fabio se você tivesse uma fabrica de lapis, ela se chamaria Fabio Castell?']
    piadas_Groger = ['Imagina pensar como um humano normal, igual esses que você vê na rua','Porque a vaca na argentina fica olhando pra cima? Porque é Bois-Nos-Ares','O madara morreu agora é o obede obito','No back tem varios backs','Oq importa é oq importa','sgbd não é rgbd jo soy rebelde','cara esse cara é o cara','Nas-Views, aviões. barcos','a diferença entre lt e gt é que lt tem l e gt tem g e não é g de dragon ball','Pra esse erro é só lê','Só o python é pai','Obede você é ruim porque você é o bad','Chega na sua casa e fala path']
    piadas = [piadas_Renan,piadas_Joao,piadas_Groger]

    mente = ['', afirmacoes, div,conte_piada]
    texto_resposta = resposta
    if mente[1].count(texto_resposta)==0 and mente[0].count(texto_resposta) == 0 and mente[2].count(texto_resposta) == 0 and mente[3].count(texto_resposta)==0:
        
        return str('Não sei mas isso pode te ajudar:\nhttps://pt.lmgtfy.com/?q='+texto_resposta)
    
    if texto_resposta == '':
        return 'Digite alguma coisa'
    
    if mente[1].count(texto_resposta)==1:
        return 'Obrigado'
    if mente[2].count(texto_resposta)==1:
        return 'Se abre uma div assim "<div>" e se fecha assim "</div>"'
    if mente[3].count(texto_resposta)==1:
        autor = random.randint(0,(len(piadas)-1))
        print(autor)
        if autor == 0:
            piada_selecionada = piadas[autor][random.randint(0,len(piadas[autor])-1)]
            return str('Autor Renan: '+piada_selecionada)
        if autor == 1:
            piada_selecionada = piadas[autor][random.randint(0,len(piadas[autor])-1)]
            return str('Autor João: '+piada_selecionada)
        if autor == 2:
            piada_selecionada = piadas[autor][random.randint(0,len(piadas[autor])-1)]
            return str('Autor Groger: '+piada_selecionada)
    
        
    return 'Algo errado não está certo'
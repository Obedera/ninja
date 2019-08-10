import random
import re
def analizar_resposta(resposta):
    
    links_ajuda = '\nAlguns links de ajuda:\nhttps://www.w3schools.com/\nhttps://stackoverflow.com/\nhttps://www.devmedia.com.br/'
    
    
    oque = ['oq','são', 'pra', 'que', 'serve', 'pq']

    
    afirmacoes = ['bom dia', 'boa noite', 'boa tarde','te amo', 'seu lindo', 'amor']
    
    conte_piada = ['conte uma piada', 'piada', 'conte piada', 'piadas', 'conte umas piadas', 'diga alguma piada','fale uma piada','diga piada','diga uma piada da mastertech']
    
    piadas_Renan = ['Na mastertech  não se pode usar null, pq tem menor de idade', 'Oi pra quem me conhece eu sou o renan, pra quem não me conhece eu sou o renan']
    piadas_Joao = ['Existe uma grande diferença entre models e top models','Fabio se você tivesse uma fabrica de lapis, ela se chamaria Fabio Castell?','Perguntaram se alguém tem nome composto, sim meu nome tem ipiranga']
    piadas_Groger = ['Imagina pensar como um humano normal, igual esses que você vê na rua','Porque a vaca na argentina fica olhando pra cima? Porque é Bois-Nos-Ares','O madara morreu agora é o obede obito','No back tem varios backs','Oq importa é oq importa','sgbd não é rgbd jo soy rebelde','cara esse cara é o cara','Nas-Views, aviões. barcos','a diferença entre lt e gt é que lt tem l e gt tem g e não é g de dragon ball','Pra esse erro é só lê','Só o python é pai','Obede você é ruim porque você é o bad','Chega na sua casa e fala path']
    piadas = [piadas_Renan,piadas_Joao,piadas_Groger]

    olas = ['oi','ola','olá','eae','oh','hello','oie']

    sim = ['sim','pode','s','yes','ss','ok','bom']

    nao = ['não','nao','n']

    mente = [afirmacoes,conte_piada,oque,olas,sim,nao]
    texto_resposta = resposta.lower()
    resposta_palavras = texto_resposta.split()
    contador = []
    sem_resposta = str('Não sei mas isso pode te ajudar:\nhttps://pt.lmgtfy.com/?q='+texto_resposta+'\nhttps://stackoverflow.com/search?q='+texto_resposta)
    if texto_resposta == '':
        return 'Digite alguma coisa'
    

    for i in resposta_palavras:
        if mente[0].count(i) != 0 or mente[0].count(texto_resposta) != 0:
            contador.append('afirmacao')
        if mente[1].count(i) != 0 or mente[1].count(texto_resposta) != 0:
            contador.append('piada')
        if mente[2].count(i) != 0 or mente[2].count(texto_resposta) != 0:
            contador.append('oque')
        if mente[3].count(i) != 0 or mente[3].count(texto_resposta) != 0:
            contador.append('olas')
        if mente[4].count(i) != 0 or mente[4].count(texto_resposta) != 0:
            contador.append('sim')
        if mente[5].count(i) != 0 or mente[5].count(texto_resposta) != 0:
            contador.append('nao')
        
        
    if contador.count('piada') != 0:
        autor = random.randint(0,(len(piadas)-1))
        if autor == 0:
            piada_selecionada = piadas[autor][random.randint(0,len(piadas[autor])-1)]
            return str('Autor Renan: '+piada_selecionada)
        if autor == 1:
            piada_selecionada = piadas[autor][random.randint(0,len(piadas[autor])-1)]
            return str('Autor João: '+piada_selecionada)
        if autor == 2:
            piada_selecionada = piadas[autor][random.randint(0,len(piadas[autor])-1)]
            return str('Autor Groger: '+piada_selecionada)
    
    if contador.count('oque') != 0 and re.search('div',resposta) != None:
        return str('A tag <div> define uma divisão ou uma seção em um documento HTML. É usada geralmente para fazer blocos de elementos, dispondo organizadamente as informações dentro do layout, que são formatadas com CSS. A tag <div> é controlada pela CSS através de um ID, Class ou pela própria tag.'+links_ajuda)
    if contador.count('oque') != 0 and re.search('css',resposta) != None:
        return str('O Cascading Style Sheets (CSS) é uma "folha de estilo" composta por “camadas” e utilizada para definir a apresentação (aparência) em páginas da internet que adotam para o seu desenvolvimento linguagens de marcação (como XML, HTML e XHTML).'+links_ajuda)
    if contador.count('oque') != 0 and re.search('html',resposta) != None:
        return str('HTML é uma das linguagens que utilizamos para desenvolver websites. O acrônimo HTML vem do inglês e significa Hypertext Markup Language ou em português Linguagem de Marcação de Hipertexto.'+links_ajuda)
    if contador.count('oque') != 0 and (re.search('js',resposta) != None or re.search('javascript',resposta) != None):
        return str('JavaScript, frequentemente abreviado como JS, é uma linguagem de programação interpretada de alto nível, caracterizada também, como dinâmica, fracamente tipificada, prototype-based e multi-paradigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.'+links_ajuda)
    
    if contador.count('afirmacao')!= 0:
        return 'Obrigado'

    if contador.count('olas')!= 0:
        return 'Olá pergunta logo'

    if contador.count('nao')!= 0:
        return 'Tá bom então'

    if contador.count('sim')!= 0:
        return 'Faça sua pergunta'

    return sem_resposta
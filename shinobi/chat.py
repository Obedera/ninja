def analizar_resposta(resposta):
    div = ['como abre uma div', 'como abrir uma div', 'abrir div',]
    afirmacoes = ['Bom dia','bom dia', 'boa noite', 'Boa noite']
    mente = ['', afirmacoes, div]
    texto_resposta = resposta
    if mente[1].count(texto_resposta)==0 and mente[0].count(texto_resposta) == 0 and mente[2].count(texto_resposta) == 0:
        
        return str('Não sei mas isso pode te ajudar:\nhttps://pt.lmgtfy.com/?q='+texto_resposta)
    
    if texto_resposta == '':
        return 'Digite alguma coisa'
    
        
    return 'Olá'
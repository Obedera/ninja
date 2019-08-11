def analizar_css(css):
    texto_css = css
    if texto_css == '':
        return 'Digite alguma coisa'
    linha_css = texto_css.splitlines()
    Erros = ''

    if linha_css[0] != 'body{':
        Erros += '\nVocê colocou  ' + linha_css[0] +', o correto é body{'
    if linha_css[1] != 'margin:':
        Erros += '\nVocê colocou  ' + linha_css[1] +', o correto é margin:'
    if linha_css[2] != 'back-ground:':
        Erros += '\nVocê colocou  ' + linha_css[2] +', o correto é back-ground:'
    if linha_css[3] != 'display:':
        Erros += '\nVocê colocou  ' + linha_css[3] +', o correto é display:'
    if linha_css[4] != 'padding:':
        Erros += '\nVocê colocou  ' + linha_css[4] +', o correto é padding:'

    return Erros
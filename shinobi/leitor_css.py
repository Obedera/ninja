import re
def analizar_css(css):
    texto_css = css
    if texto_css == '':
        return 'Digite alguma coisa'
    linha_css = texto_css.splitlines()
    Erros = ''
    lista_tags = ['body','aside','header','main','html','head','div','nav','section','p','h1','h2','h3','h4','h5','h6','span','img','button','input','form','select','ul','li','ol','option','textarea','hr','table','a','label','*',''] 

    def quebrar_por_palavra(linha):
        contador_linha_css = 0
        palavras = []
        while contador_linha_css<len(linha):
            palavra = linha[contador_linha_css].split()
            for i in palavra:
                palavras.append(i)  
            contador_linha_css += 1
        return palavras
    
    lista_palavras = quebrar_por_palavra(linha_css)

    def quebrar_por_letra(lista_palavras):
        contador_letra_css = 0
        letras = []
        while contador_letra_css<len(lista_palavras):
            letra = lista_palavras[contador_letra_css]
            for i in letra:
                letras.append(i)
            contador_letra_css += 1
        return letras

    lista_letras = quebrar_por_letra(lista_palavras)

    def pegar_selectors(texto):
        texto = texto.replace(',','')
        lista = texto.split('{')
        contador = 0
        lista_selectors = []
        lista_separada = []
        while contador<len(lista):
            lista_aux = lista[contador].split('}')
            lista_separada.extend(lista_aux)
            contador += 1

        i = 0
        while i<len(lista_separada):
            lista_selectors.append(lista_separada[i].replace('\n',''))
            i += 2 
            
        print(lista_selectors)
        return lista_selectors
 
    
    lista_selectors = pegar_selectors(texto_css)
    
    def checar_selectors(lista):
        erros = ''
        palavras_selectors = []
        contador = 0
        while contador<len(lista):
            palavras_selectors.extend(re.split('\s',lista[contador]))
            contador += 1
        
        for i in palavras_selectors:
            if lista_tags.count(i) != 0 or i[0:1] == '.':
                pass
            else:
                erros += f'O selector {i} não existe'
        
        return erros
    
    Erros += checar_selectors(lista_selectors) 

    if lista_letras.count('{') > lista_letras.count('}'):
        Erros += 'Você esqueceu de colocar "}"\n'
    if lista_letras.count('{') < lista_letras.count('}'):
        Erros += 'Você esqueceu de colocar "{"\n'
    
    
    
    if Erros == '':
        return 'Não detectei nenhum erro'
        
    return Erros
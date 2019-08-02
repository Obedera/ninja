def analizar_js(js):
    texto_js = js.read()
    linha_js = texto_js.splitlines()
    Erros = ''

    def quebrar_por_palavra(linha):
        contador_linha_js = 0
        palavras = []
        while contador_linha_js<len(linha):
            palavra = linha[contador_linha_js].split()
            for i in palavra:
                palavras.append(i)  
            contador_linha_js += 1
        return palavras
    
    lista_palavras = quebrar_por_palavra(linha_js)


    def quebrar_por_letra(lista_palavras):
        contador_letra_js = 0
        letras = []
        while contador_letra_js<len(lista_palavras):
            letra = lista_palavras[contador_letra_js]
            for i in letra:
                letras.append(i)
            contador_letra_js += 1
        return letras

    lista_letras = quebrar_por_letra(lista_palavras)
    
    if lista_letras.count('{') > lista_letras.count('}'):
        Erros += 'Você esqueceu de colocar "}"\n'
    if lista_letras.count('{') < lista_letras.count('}'):
        Erros += 'Você esqueceu de colocar "{"\n'

    if lista_letras.count('(') > lista_letras.count(')'):
        Erros += 'Você esqueceu de colocar ")"\n'
    if lista_letras.count('(') < lista_letras.count(')'):
        Erros += 'Você esqueceu de colocar "("\n'

    if (lista_letras.count('"')%2) != 0:
        Erros += 'Você esqueceu de colocar " \n'
    
    if (lista_letras.count("'")%2) != 0:
        Erros += "Você esqueceu de colocar ' \n"


    def checar_erros_palavra(lista_palavras):
        contador = 0
        erros = ''
        for j in lista_palavras:
            if j[:3] == 'ale':
                if j[3:6] != 'rt(':
                    erros += f'Tem erro na linha "{contador+1}" o "{j}" está escrito errado\n'
                if j.count(';') == 0:
                    erros += f'Não se esqueça de colocar o ";"\n'

            contador += 1
        return erros

    Erros += checar_erros_palavra(lista_palavras)

    return Erros
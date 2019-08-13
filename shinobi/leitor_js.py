def analizar_js(js):
    texto_js = js
    linha_js = texto_js.splitlines()
    Erros = ''
    if texto_js == '':
        Erros = 'Digite alguma coisa' 
    numero_erros = 0  

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
        numero_erros += 1

    if lista_letras.count('{') < lista_letras.count('}'):
        Erros += 'Você esqueceu de colocar "{"\n'
        numero_erros += 1


    if lista_letras.count('(') > lista_letras.count(')'):
        Erros += 'Você esqueceu de colocar ")"\n'
        numero_erros += 1

    if lista_letras.count('(') < lista_letras.count(')'):
        Erros += 'Você esqueceu de colocar "("\n'
        numero_erros += 1
    
    if lista_letras.count('[') > lista_letras.count(']'):
        Erros += 'Você esqueceu de colocar "]"\n'
        numero_erros += 1

    if lista_letras.count('[') < lista_letras.count(']'):
        Erros += 'Você esqueceu de colocar "["\n'   
        numero_erros += 1

    if (lista_letras.count('"')%2) != 0:
        Erros += 'Você esqueceu de colocar " \n'
        numero_erros += 1
    
    if (lista_letras.count("'")%2) != 0:
        Erros += "Você esqueceu de colocar ' \n"
        numero_erros += 1
    


    def checar_erros_palavra(lista_palavras):
        contador = 0
        erros = ''
        numero_erro = 0
        for j in lista_palavras:
            if j[:3] == 'ale':
                if j[3:6] != 'rt(':
                    erros += f'Tem erro na linha "{contador+1}" o "{j}" está escrito errado\n'
                    numero_erro += 1
                    
                    
            if j[:3] == 'pro':
                if j[3:7] != 'mpt(':
                    erros += f'Tem erro na linha "{contador+1}" o "{j}" está escrito errado\n'
                    numero_erro += 1


            if j[:3] == 'fun':
                if j[3:] != 'ction':
                    erros += f'Tem erro na linha "{contador+1}" o "{j}" está escrito errado\n'
                    numero_erro += 1
                
            contador += 1
        dado = [erros,numero_erro]
        return dado

    erros_palavras = checar_erros_palavra(lista_palavras)
    Erros += erros_palavras[0]
    numero_erros += erros_palavras[1]
    if Erros == '':
        Erros = 'Não detectei nenhum erro'
    dados = [Erros,numero_erros]
    return dados
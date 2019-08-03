def analizar_html(html):
    texto_html = html
    linha_html = texto_html.splitlines()
    Erros = ''

    def quebrar_por_palavra(linha):
        contador_linha_html = 0
        palavras = []
        while contador_linha_html<len(linha):
            linha_palavras = linha[contador_linha_html].split()
            for palavra in linha_palavras:
                palavras.append(palavra)  
            contador_linha_html += 1
        return palavras

    lista_palavras = quebrar_por_palavra(linha_html)

    def quebrar_por_letra(lista_palavras):
        contador_letra_html = 0
        letras = []
        while contador_letra_html<len(lista_palavras):
            palavra = lista_palavras[contador_letra_html]
            for letra in palavra:
                letras.append(letra)
            contador_letra_html += 1
        return letras
    
    lista_letras = quebrar_por_letra(lista_palavras)

    def itens_necessarios():
        erros = ''
        #itens por linha
        

        # itens por palavra
        if lista_palavras.count('<script') == 1 and lista_palavras.count('defer') == 0:
            erros += 'Coloque o defer depois do script\n'

        if lista_palavras.count('<body>') == 1 or lista_palavras.count('<body') == 1:
            pass
        else:
            erros += 'Você não colocou o body corretamente\n'

        if lista_palavras.count('<head>') == 1 or lista_palavras.count('<head') == 1:
            pass
        else:
            erros += 'Você não colocou o head corretamente\n'
            


        # itens por letra
        if lista_letras.count('<') > lista_letras.count('>'):
            erros += 'Você esqueceu de colocar ">"\n'
        if lista_letras.count('<') < lista_letras.count('>'):
            erros += 'Você esqueceu de colocar "<"\n'
        return erros
    

    def checar_erros_palavra(lista_palavras):
        contador = 0
        erros = ''
        while contador<len(lista_palavras):
            if lista_palavras[contador] == '<':
                erros += f'Tem erro na linha {contador+1} tire o espaçamento do "<" entre o "{lista_palavras[contador+1]}"\n'
            
            if lista_palavras[contador][0:7] == 'class="':
                letras = quebrar_por_letra(lista_palavras[contador])
                if letras.count('.') == 1:
                    erros += f'Tem erro na linha {contador+1} tire o "." da classe'

            if lista_palavras[contador] == '<bodyy>' or lista_palavras[contador] == '<bodyy':
                erros += f'Tem erro na linha {contador+1} o "{lista_palavras[contador]}" está escrito errado\n'
                   
            if lista_palavras[contador] == '<scripts':
                erros += f'Tem erro na linha {contador+1} o "{lista_palavras[contador]}" está escrito errado\n'
            
            contador += 1

        return erros

    Erros += itens_necessarios()
    Erros += checar_erros_palavra(lista_palavras)

    return Erros
    
    
    




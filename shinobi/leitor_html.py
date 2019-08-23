def analizar_html(html):
    texto_html = ' <'.join(html.split('<'))
    linha_html = texto_html.splitlines()
    Erros = ''
    if texto_html == '':
        Erros = 'Digite alguma coisa'
    numero_erros = 0  


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
        numero_erro = 0
        #itens por linha
        

        # itens por palavra
        if lista_palavras.count('<script') == 1:
            if lista_palavras.count('defer') != 0 or lista_palavras.count('defer>') != 0:
                pass
            else:
                erros += 'Coloque o defer depois do script\n'
                numero_erro += 1


        # itens por letra
        if lista_letras.count('<') > lista_letras.count('>'):
            erros += 'Você esqueceu de colocar ">"\n'
            numero_erro += 1

        if lista_letras.count('<') < lista_letras.count('>'):
            erros += 'Você esqueceu de colocar "<"\n'
            numero_erro += 1
        
        dado = [erros,numero_erro]
        return dado
    

    def fechamento(tag, lista_palavras):
        erro = ''
        numero = 0
        i = 0
        quantidade_aberta = 0
        quantidade_fechada = 0
        while i<len(lista_palavras):
            if lista_palavras[i][0:(1+len(tag))] == str('<'+tag): 
                quantidade_aberta += 1
            if lista_palavras[i][0:(2+len(tag))] == str('</'+tag) and lista_palavras[i][(2+len(tag)):(3+len(tag))] == '>': 
                quantidade_fechada += 1
            i += 1

        if quantidade_aberta != quantidade_fechada:
            erro += f'A tag {tag} precisa ser fechada\n'
            numero += 1
        dado = [erro, numero]
        return dado

    def checar_erros_palavra(lista_palavras):
        contador = 0
        divs_abertas = 0
        divs_fechadas = 0
        erros = ''
        numero_erro = 0

        while contador<len(lista_palavras):
            if lista_palavras[contador] == '<':
                erros += f'Tem erro na linha {contador+1} tire o espaçamento do "<" entre o "{lista_palavras[contador+1]}"\n'
                numero_erro += 1

            
            if lista_palavras[contador][0:7] == 'class="':
                letras = quebrar_por_letra(lista_palavras[contador])
                if letras.count('.') == 1:
                    erros += f'Tem erro tire o "." da classe\n'
                    numero_erro += 1


            if lista_palavras[contador][0:3] == '<bo':
                if lista_palavras[contador][3:6] == 'dy' or lista_palavras[contador][3:6]== 'dy>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1] 
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<he':
                if lista_palavras[contador][3:6] == 'ad' or lista_palavras[contador][3:6]== 'ad>' or lista_palavras[contador][3:9]== 'ader>' or lista_palavras[contador][3:9]== 'ader':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1] 
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<sc':
                if lista_palavras[contador][3:8] == 'ript' or lista_palavras[contador][3:8]== 'ript>':
                    pass
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<na':
                if lista_palavras[contador][3:5] == 'v' or lista_palavras[contador][3:5]== 'v>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<bu':
                if lista_palavras[contador][3:8] == 'tton' or lista_palavras[contador][3:8]== 'tton>':
                    pass
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<im':
                if lista_palavras[contador][3:5] == 'g' or lista_palavras[contador][3:5]== 'g>':
                    pass
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<di':
                if lista_palavras[contador][3:5] == 'v' or lista_palavras[contador][3:5]== 'v>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            
            if lista_palavras[contador][0:4] == '<mai':
                if lista_palavras[contador][4:6] == 'n' or lista_palavras[contador][4:6]== 'n>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:4] == '<sec':
                if lista_palavras[contador][4:9] == 'tion' or lista_palavras[contador][4:9]== 'tion>': 
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<in':
                if lista_palavras[contador][3:7] == 'put' or lista_palavras[contador][3:7]== 'put>': 
                    pass
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<for':
                if lista_palavras[contador][4:6] == 'm' or lista_palavras[contador][4:6]== 'm>': 
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:4] == '<foo':
                if lista_palavras[contador][4:8] == 'ter' or lista_palavras[contador][4:8]== 'ter>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
                
            if lista_palavras[contador][0:4] == '<sel':
                if lista_palavras[contador][4:8] == 'ect' or lista_palavras[contador][4:8]== 'ect>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:4] == '<opt':
                if lista_palavras[contador][4:8] == 'ion' or lista_palavras[contador][4:8]== 'ion>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:4] == '<tex':
                if lista_palavras[contador][4:10] == 'tarea' or lista_palavras[contador][4:10]== 'tarea>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<la':
                if lista_palavras[contador][3:7] == 'bel' or lista_palavras[contador][3:7]== 'bel>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<sp':
                if lista_palavras[contador][3:6] == 'an' or lista_palavras[contador][3:6]== 'an>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<ta':
                if lista_palavras[contador][3:7] == 'ble' or lista_palavras[contador][3:7]== 'ble>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    dado_fechamento = fechamento(tag,lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
         
            contador += 1


        dado = [erros,numero_erro]
        return dado

    itens = itens_necessarios()
    Erros += itens[0]
    numero_erros += itens[1]

    erros_palavra = checar_erros_palavra(lista_palavras)
    Erros += erros_palavra[0]
    numero_erros += erros_palavra[1]

    if Erros == '':
        Erros = 'Não detectei nenhum erro'
    
    dados = [Erros,numero_erros]
    return dados
    
    
    




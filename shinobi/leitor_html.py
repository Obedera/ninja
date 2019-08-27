def analizar_html(html):
    def remover_comentario(texto):
        i = 0
        aux = ''
        while i<len(texto):
            if texto[i:(i+4)] == '<!--':
                while texto[(i-3):i] != '-->':
                    i += 1

            aux += texto[i:(i+1)]
            i += 1
        return aux

    texto_html = remover_comentario(html)
    texto_html = ' <'.join(texto_html.split('<'))
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
            letras.append('$')
            contador_letra_html += 1
        return letras
    
    lista_letras = quebrar_por_letra(lista_palavras)

    def pegar_conteudo_tags(lista_letras):
        lista = []
        aux = ''
        i = 0
        while i<len(lista_letras):
            if lista_letras[i] == '<':
                while lista_letras[i] != '>':

                    if lista_letras[i] == '=':
                        i += 2
                        while lista_letras[i] != '"':
                            i += 1

                    aux += lista_letras[i]
                    i += 1
                aux = ''.join(aux.split('"'))                
                aux = ' '.join(aux.split('$'))
                lista.append(aux[1:])
                aux = ''
            i += 1
        
        return lista

    atributos_tags = ['','accept', 'accept-charset', 'action', 'alt', 'autobuffer', 'autocomplete', 'autofocus', 'autoplay', 'async', 'charset', 'checked', 'cite', 'class', 'cols', 'colspan', 'content', 'coords', 'controls', 'data', 'datetime', 'default', 'defer', 'dir', 'disable', 'enctype', 'for', 'form', 'formaction', 'formentype', 'formmethod', 'formnovalidate', 'formtarget', 'headers', 'height', 'hidden', 'high', 'href', 'hreflang', 'html', 'http-equiv', 'icon', 'id', 'initial-scale', 'ismap', 'label', 'lang', 'list', 'loop', 'low', 'manifest', 'max', 'maxlength', 'min', 'media', 'method', 'multiple', 'name', 'object', 'onabort', 'onanimationcancel', 'onanimationend', 'onanimationiteration', 'onanimationstart', 'onauxclick', 'onblur', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'onclose', 'oncontextmenu', 'oncopy', 'oncuechange', 'oncut', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragexit', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onfullscreenchange', 'onfullscreenerror', 'ongotpointercapture', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadend', 'onloadstart', 'onlostpointercapture', 'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmozfullscreenchange', 'onmozfullscreenerror', 'onpaste', 'onpause', 'onplay', 'onplaying', 'onpointercancel', 'onpointerdown', 'onpointerenter', 'onpointerleave', 'onpointermove', 'onpointerout', 'onpointerover', 'onpointerup', 'onprogress', 'onratechange', 'onreset', 'onresize', 'onscroll', 'onseeked', 'onseeking', 'onselect', 'onselectstart', 'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'ontoggle', 'ontransitioncancel', 'ontransitionend', 'ontransitionrun', 'ontransitionstart', 'onvolumechange', 'onwaiting', 'onwebkitanimationend', 'onwebkitanimationiteration', 'onwebkitanimationstart', 'onwebkittransitionend', 'open', 'optimum', 'pattern', 'ping', 'placeholder', 'poster', 'radiogroup', 'readonly', 'rel', 'replace', 'required', 'reversed', 'rows', 'rowspan', 'sandbox', 'scope', 'scoped', 'seamless', 'selected', 'shape', 'sizes', 'sizr', 'span', 'src', 'start', 'step', 'style', 'target', 'title', 'type', 'usempa', 'value', 'wrap', 'width']

    def analizar_conteudo_tags(lista):
        atributos = []
        aux = []
        erro = ''
        numero_erro = 0
        i = 0
        while i<len(lista):
            aux = lista[i].split(' ')
            aux.remove(aux[0])
            atributos.extend(aux)
            i += 1

        for j in atributos:
            if atributos_tags.count(j) == 0:
                erro += f'O atributo "{j}" não existe\n'
                numero_erro += 1 
        
        return [erro,numero_erro]
    

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
        if lista_letras.count('<') == lista_letras.count('>'):
            dados_tags = analizar_conteudo_tags(pegar_conteudo_tags(lista_letras))
            erros += dados_tags[0]
            numero_erro += dados_tags[1]

        dado = [erros,numero_erro]
        return dado
        
    tags = []

    def set_tags(tag,tags):
        tags.append(tag)

    def get_tags():
        return tags

    def fechamento(tag, lista_palavras):
        tags = get_tags()
        erro = ''
        numero = 0
        if tags.count(tag) != 0:
            return [erro, numero]
        i = 0
        quantidade_aberta = 0
        quantidade_fechada = 0
        while i<len(lista_palavras):
            if lista_palavras[i][0:(2+len(tag))] == str('<'+tag) or lista_palavras[i][0:(2+len(tag))] == str('<'+tag)+'>': 
                quantidade_aberta += 1
            if lista_palavras[i][0:(3+len(tag))] == str('</'+tag) or lista_palavras[i][0:(3+len(tag))] == str('</'+tag+'>'): 
                quantidade_fechada += 1
            i += 1

        if quantidade_aberta > quantidade_fechada:
            erro += f'Tem {quantidade_aberta-quantidade_fechada} tag {tag} precisa ser fechada\n'
            numero += 1

        if quantidade_aberta < quantidade_fechada:
            erro += f'Tem {quantidade_fechada-quantidade_aberta} tag {tag} foi fechada porém ela não foi aberta\n'
            numero += 1
        set_tags(tag,tags)
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


            if lista_palavras[contador][0:3] == '<as':
                if lista_palavras[contador][3:7] == 'ide' or lista_palavras[contador][3:7]== 'ide>':
                    tag = lista_palavras[contador][1:]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<bo':
                if lista_palavras[contador][3:6] == 'dy' or lista_palavras[contador][3:6]== 'dy>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
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

            if lista_palavras[contador][0:3] == '<di':
                if lista_palavras[contador][3:5] == 'v' or lista_palavras[contador][3:5]== 'v>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<foo':
                if lista_palavras[contador][4:8] == 'ter' or lista_palavras[contador][4:8]== 'ter>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<for':
                if lista_palavras[contador][4:6] == 'm' or lista_palavras[contador][4:6]== 'm>': 
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<he':
                if lista_palavras[contador][3:6] == 'ad' or lista_palavras[contador][3:6]== 'ad>' or lista_palavras[contador][3:9]== 'ader>' or lista_palavras[contador][3:9]== 'ader':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1] 
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<im':
                if lista_palavras[contador][3:5] == 'g' or lista_palavras[contador][3:5]== 'g>':
                    pass
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<in':
                if lista_palavras[contador][3:7] == 'put' or lista_palavras[contador][3:7]== 'put>': 
                    pass
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<la':
                if lista_palavras[contador][3:7] == 'bel' or lista_palavras[contador][3:7]== 'bel>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<mai':
                if lista_palavras[contador][4:6] == 'n' or lista_palavras[contador][4:6]== 'n>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<met':
                if lista_palavras[contador][4:6] == 'a' or lista_palavras[contador][4:6]== 'a>': 
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:3] == '<na':
                if lista_palavras[contador][3:5] == 'v' or lista_palavras[contador][3:5]== 'v>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<opt':
                if lista_palavras[contador][4:8] == 'ion' or lista_palavras[contador][4:8]== 'ion>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
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
            
            if lista_palavras[contador][0:4] == '<sec':
                if lista_palavras[contador][4:9] == 'tion' or lista_palavras[contador][4:9]== 'tion>': 
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
                
            if lista_palavras[contador][0:4] == '<sel':
                if lista_palavras[contador][4:8] == 'ect' or lista_palavras[contador][4:8]== 'ect>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
                    
            if lista_palavras[contador][0:3] == '<sp':
                if lista_palavras[contador][3:6] == 'an' or lista_palavras[contador][3:6]== 'an>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<ta':
                if lista_palavras[contador][3:7] == 'ble' or lista_palavras[contador][3:7]== 'ble>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1

            if lista_palavras[contador][0:4] == '<tex':
                if lista_palavras[contador][4:10] == 'tarea' or lista_palavras[contador][4:10]== 'tarea>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
                    erros += dado_fechamento[0] 
                    numero_erro += dado_fechamento[1]
                else:
                    erros += f'Tem erro o "{lista_palavras[contador]}" está escrito errado\n'
                    numero_erro += 1
            
            if lista_palavras[contador][0:3] == '<ti':
                if lista_palavras[contador][3:7] == 'tle' or lista_palavras[contador][3:7]== 'tle>':
                    tag = lista_palavras[contador][1:(len(lista_palavras[contador])-1)]
                    tag = tag.split('>')
                    dado_fechamento = fechamento(tag[0],lista_palavras)
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
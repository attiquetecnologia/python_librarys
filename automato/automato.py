#-*- codign: utf-8 -*-

from modulo import Estado, Transicao
import modulo


class Automato:
    """
    Esta classe e utilizada para gerenciar automatos finitos nao deterministicos
    """
    def __init__(self):

        # Lista de estados da maquina
        self.estados = []

        # Lista de transicoes
        self.transicoes = []

        # Self alfabeto
        self.alfabeto = []

        # estados equivalentes

    ## end __init__

    # Devolve o alfabeto da transicao
    def get_alfabeto(self):
        for t in self.transicoes:
            if t.ler not in self.alfabeto:
                self.alfabeto.append(t.ler)
            ## end if
        ## end for
    ## fim def
        
    # Print estados
    def print_estados(self):
        for t in self.estados:
            print t.to_string()
    #fim def
            
    # Print transferencia
    def print_transicoes(self):
        for t in self.transicoes:
            print t.to_string()
    #fim def
    
    # Estados finais list[]
    def finals(self):
        finals = []
        for s in self.estados:
            if s.final:
                finals.append(s)
            ## fim se
        #fim for
        return finals
    ##fim def

    # Estados finais list[]
    def initial(self):
        for s in self.estados:
            if s.initial:
                return s
            ## fim se
        #fim for
    ##fim def


    # Exibe na tela os estados finais
    def print_finals(self):
        for e in self.finals():
            print e.to_string()
    ## end def
            
    # Estados nao finais list[]
    def not_finals(self):
        finals = []
        for s in self.estados:
            if not s.final:
                finals.append(s)
            ## fim se
        #fim for
        return finals
    ##fim def

    # Exibe na tela os estados finais
    def print_not_finals(self):
        for e in self.not_finals():
            print e.to_string()
    ## end def

    ## retorna um estado por id ou por nome
    def get_estado(self,id=None,name=None):
        for e in self.estados:
            try:
                if id and str(e.id) == str(id):
                    return e # retorna o estado por id
                elif name and str(e.name) == (name):
                    return e # retorna por nome
                
                ##fim se
            except ValueError as v:
                print 'Valores inconsistentes\n%s' % v.message
        ## fim for
    ##fim def

            
    # Devolve lista com transicoes de um estado
    def get_transicoes(self,id):
        transicoes = []
        for t in self.transicoes:
            if str(t.de.id) == str(id):
                transicoes.append(t)
            ## fim se
        #fim for
        return transicoes
    ## fim def


            
    ## Retorna uma transicao para uma leitura/opcao
    ## Parametros
    ##  estado - ID do estado
    ##  leitura - alfabeto
    ##  initial - transicao de um estado inicial
    def get_transicao(self,estado=None,leitura=None,initial=False):
        transicao = None
        transicoes = []

        ## Se for uma cadeia, retira o primeiro elemento de si
        if leitura and len(leitura) > 1 :
            leitura = leitura[0]
        
        ## Se vier de um estado inicial pesquia por estado
        if initial: transicoes = self.get_transicoes( self.initial().id )
        else: transicoes = self.get_transicoes(estado)
        
        for t in transicoes:
            # se conter o parametro leitura
            # print "Testando str(t.ler)(%s) == str(leitura)(%s)" % (t.to_string,leitura)
            if str(t.ler) == str(leitura):
                #print "t(%s)-%s" % (t.to_string(),leitura)
                return t
            
            ##fimd se
        #fim for
    ##fim def

     
    # Adiciona um estado ao automato
    def add_estado(self,estado):    
        ## Verifica se o estado existe antes de adicionar
        if not self.get_estado(name=estado.name) and not self.get_estado(id=str(estado.id)):
            ## atualiza o id se for -1
            if self.get_estado(id=str(estado.id)) or int(estado.id) == -1:
                print 'vamod'
                id = 1 + len(self.estados)
            return self.estados.append(estado)

    ## fim def

    def del_estado(self,id):
        for e in self.estados:
            if str(e.id) == str(id):
                self.estados.remove(e)
                #remove as possiveis transicoes
                self.del_transicoes_estado(id)
            # fim se
        #fim for
    #fim def

    ## fim estado
    #Remove as transicoes de um estado
    def del_transicoes_estado(self, id):
        for t in self.transicoes:
            if str(t.de.id) == str(id) or str(t.para.id) == str(id):
                self.transicoes.remove(t)
            #fim se
        #fim for
    #fim def

    #Remove as transicoes de um estado
    # de - id origem
    # ler - leitura
    # para - id destino
    def del_transicao(self,de,para,ler):
        for t in self.transicoes:
            if str(t.de.id) == str(de) and str(t.para.id) == str(para) and str(t.ler) == str(ler):
                self.transicoes.remove(t)
            #fim se
        #fim for
    #fim def

    # Adicionando transicoes
    def add_transicao(self,transicao):
        exists = False
        for t in self.transicoes:
            # se conter o parametro leitura

            if str(t.ler) == str(transicao.ler) and str(t.de.id) == str(transicao.de.id) and str(t.para.id) == str(transicao.para.id):
                exists = True
        if not exists:
            if transicao.ler not in self.alfabeto:
                ## Cria o alfabeto a partir das transicoes
                self.alfabeto.append(transicao.ler)
            return self.transicoes.append(transicao)
    
    # Imprime uma representacao XML
    def print_xml(self):

        xml = '<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 6.4.--><structure>\n'
        xml += '\t<type>fa</type>\n'
        xml += '\t<automaton>\n'

        # Percorre a lista de estados extraindo o dicionario
        for a in self.estados:
            xml += '\t<state id="%s" name="%s">\n' % (a.id,a.name)
            xml += '\t\t<x>%s</x>\n' % a.x
            xml += '\t\t<y>%s</y>\n' % a.y
            if a.initial: xml += '\t\t<initial/>\n'
            if a.final: xml += '\t\t<final/>\n'
            xml += '\t</state>\n'

            
        for t in self.transicoes:
            xml += '\t<transition>\n'
            xml += '\t\t<from>%s</from>\n' % t.de.id
            xml += '\t\t<to>%s</to>\n' % t.para.id
            xml += '\t\t<read>%s</read>\n' % t.ler
            xml += '\t</transition>\n'


        xml += '\t</automaton>\n'
        xml += '</structure>\n'
        
        return xml
    
    # Isto salva um automato no c:\padrao
    def salvar(self,file_name):
        return modulo.salvar(file_name,self)
    ## fim salvar


    # Carreta um arquivo do jff para a memoria
    def carregar(self,file_name):
        if file_name is None:
            return False
        # cria uma nova instancia para evitar conflitos
        self.__init__()
        # Os codigos a seguir foram retirados da documentacao do python em:
        # https://docs.python.org/2/library/xml.etree.elementtree.html
        import xml.etree.ElementTree as ET
        tree = ET.parse(file_name)
        root = tree.getroot()

        # Assumindo que somente nos interessa o conteudo das tags state e
        # transition, vamos diretamente a eles
        state = root.iter('state')
        transition = root.iter('transition')        
        # setando os atributos de state
        self.__set_atributo_estado(state)
        # setando as transicoes
        self.__set_atributo_transicao(transition)
    

    # Seta os atributos de state
    # NOTA: em python o sublinha duplo '__' siginifica private em java
    # Como este metodo trabalha em conjunto com carregar, tambem poderiamos faze-lo como submetodo de carregar
    def __set_atributo_estado(self,state):
        # Agora precisamos carregar os dados para a memoria
        # varrendo os filhos de state
        for child in state:
            # Cria uma instancia de estado e adiciona os atributos a ele
            estado = Estado(id=int(child.attrib["id"]),name=child.attrib["name"])
            # Percorre agora os elementos da tag state para setar atributos
            for c in child:
                if c.tag == 'x':
                    estado.x = c.text
                elif c.tag == 'y':
                    estado.y = c.text
                elif c.tag == 'initial':
                    estado.initial = True
                elif c.tag == 'final':
                    estado.final = True
                else: pass
            # fim for

            # por final adiciona estado a lista
            if not self.get_estado(name=estado.name):
                self.add_estado(estado)
            else: print 'Estado id: %s - name: %s duplicado' % (estado.id,estado.name)
            
        # fim for
    #fim setState

    # Seta os atributos de state
    def __set_atributo_transicao(self,transition):
        # Agora precisamos carregar os dados para a memoria
        # varrendo os filhos
        for child in transition:
            de = 0
            para = 0
            ler = ''
            ## verifica as subtags
            for c in child:
                # Adiciona ao alfabeto do automato
                if c.tag == 'from' :
                    de = c.text
                elif c.tag == 'to' :
                    para = c.text
                elif c.tag == 'read' :
                    ler = c.text                    
                    
                    ## en if
                ## end if
            ## enf for

            ## Assegura que so adicionara um estado existente na maquina

            de = self.get_estado(id=de)
            para = self.get_estado(id=para)
            if de and para: self.add_transicao( Transicao(de=de,para=para,ler=ler) )
        # fim for

    #fim setState

    # Devolve lista com transicoes do estado de origem
    def transicoes_estado(self,id):
        transicoes = []
        for t in self.transicoes:
            if str(t.de.id) == str(id):
                transicoes.append(t)
            ## fim se
        #fim for
        return transicoes
    ## fim def

    #processa a cadeia
    def processa(self,cadeia,transicao):

        # se estiver lendo o penultimo simbo e o estado for retornar para si mesmo verificar possibilidade de ir para outro
        
        if cadeia[1:] == "": # Se estiver vasia verifica se o estado e um estado final

            return transicao.para.final # se nao for estado final nao pertence
        else: # Se nao processa cadeia
            # Confere a leitura
            try:
                if transicao.ler == cadeia[0]:
                    
                    next_transicao = self.get_transicao( estado=transicao.para.id, leitura=cadeia[1] )

                    return self.processa(cadeia[1:], next_transicao) or False

            except AttributeError as ex: print ex
            else: # se nao a cadeia nao pertence
                return False
    ## fim def
    
    # Verifica uma cadeia
    def aceita(self,cadeia):
        # percorre as transicoes para saber
        # pega e3stado inicial
        # Verifica em todas as traniscoes dele para onde pode ir
        # verifica se a opcao combina com a transicao
        # se nao combinar a cadeia nao pertence
        # Se combinar prossegue com a mlhor opcao

        ## NOTA: se nao houver transicoes nao eh possivel continuar
        if len(self.transicoes) == 0: return False

        return self.processa( cadeia, self.get_transicao(leitura=cadeia[0], initial=True) )
            
    ## fim def

    def equivalentes(self):
        trans = []

        ## Metodo de comparacao
        # Imagine que o ele possua um Alfabeto com duas possibilidades A e B
        # Quando ele estiver em um estado e ler A ele ira analizar se o destino e um estado final (f) ou se e normal (n)
        # Se o estado for normal setara a leitura como n se final f
        # n e f sao na verdade grupos que poderiamos chamar de Aa = conjunto dos nao terminals e Ab = conjunto dos terminais

        ## Percorre o vetor de estados verificando se ele esta em transicoes
        ## Este laco compara os estados com as transicoes para determinar seus destinos
        for e in self.estados:
            if str(e.id) not in str(trans):
                ## se a transicao nao esta no vetor
                aux = ''
                ## Verifica se as transicoes do estado vao para  um estado final
                for t in self.transicoes_estado(id=str(e.id)):
                    ## Se leitura estiver no alfabeto e se for para final ele ira marcar como f
                    if t.ler in self.alfabeto and t.para.final:
                        aux += 'f'
                    ## Se ela for para um estado normal ira marcar como n
                    else:
                        aux += 'n'
                    ## fim se
                ## fim for
                trans.append( { aux:e.id } )
            ##fim se
        ## fim for

        ## Foi necessario usar esta quantidade de codigo devido o tempo
        ## vetor que armazena as possibildades
        ## [ {'nf': [0,1], 'nn':[0]... }
        possibles = []  
        for e in trans:
            ## Verifica por repetidos
            if {e.keys()[0]:[]} not in possibles:
                possibles.append( {e.keys()[0]:[]} )

                ## Adiciona os estados as possibilidades
                for p in possibles:
                    for e in trans:
                    ## verifica as chaves
                        if e.keys()[0] == p.keys()[0]:
                            ## recupera a lista do objeto e adiciona o valor 
                            p.get(p.keys()[0]).append( e.get(e.keys()[0]) )

        return possibles

    def print_equivalentes(self):
        for t in self.equivalentes():
            print t

    ## Complemento
    def complemento(self):
        return modulo.complemento(self) ## passa a instancia deste para calcular
    ## fim complemento

    ## mover - recebe um id e retorna id do estado
    def mover(self,estado,cadeia):
        ## uso de recursao se a cadeia vazia retorna o estado atual
        if cadeia == '': return estado
        para = -1
        ## percorre transic0es
        for t in self.transicoes:
            ## se combinar leitura com estado seta estado para
            if str(estado) == str(t.de.id) and str(cadeia[0]) == str(t.ler):
                para = t.para.id
        # chama novamente a funcao com proximo estado e proxima sequencia
        return self.mover(para,cadeia[1:])
    ## fim mover

    ## mover - recebe o nome e retorna o nome do estado
    def mover_name(self,estado,cadeia):
        ## uso de recursao se a cadeia vazia retorna o estado atual
        if cadeia == '': return estado
        para = ''
        ## percorre transic0es
        for t in self.transicoes:
            ## se combinar leitura com estado seta estado para
            if str(estado) == str(t.de.name) and str(cadeia[0]) == str(t.ler):
                para = t.para.name
        # chama novamente a funcao com proximo estado e proxima sequencia
        return self.mover_name(para,cadeia[1:])
    ## fim mover

    ## multiplicacao
    def multiplicar(self,novo):
        return modulo.multiplicar(self,novo)
    
if __name__=='__main__':

    auto = Automato()
    auto.carregar('campare1.jff')
    auto.print_equivalentes()
    auto2 = Automato()
    auto2.carregar('campare2.jff')
    print "========= Carregando o automato 1 ================"
    #auto.print_transicoes()
    print "========= Carregando o automato 2 ================"
    #auto2.print_transicoes()
    print "========= Multiplicando 1 e 2 ===================="    
    #auto3 = auto.multiplicar(auto2)
    #auto3.print_transicoes()

    #print auto3.mover('1','aabb')
   # auto3.print_equivalentes()

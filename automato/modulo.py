#-*- coding: utf-8 -*-

class Estado:
    
    def __init__(self,name,id,final=False,initial=False,x=0.0,y=0.0):
        try:
            self.id = int(id)
            self.name = str(name)
            self.final = final
            self.initial = initial
            self.x = x
            self.y = y
        except ValueError as v:
            print 'Erro ID nao pode ser uma string:\nMessage %s ' % v.message

    # retorna uma representacao da classe como um dicionario
    def to_dict(self):
        return dict(name=dict(id=id,initial=initial,final=final,x=x,y=y))

    def equals(self,estado):
        print 'self.name(%s) == estado.name(%s) or self.id(%s) == estado.id(%s):' % (self.name,estado.name,self.id,estado.id)
        if self.name == estado.name or self.id == estado.id:
            return True
        return False

    ## end def
    
    def to_string(self):
        return "Estado{ id:%2s, name:%s ,final:%s, initial:%s }" % (self.id,self.name,self.final,self.initial)

### FIM ESTADO ###
    
# -----------------------------------------------------------------------------------------------------------------
    
## Classe transição    
class Transicao:
    def __init__(self,de,para,ler):
        ## garante que ira receber uma instância de estado
        if isinstance(de,Estado) and isinstance(para,Estado) and type(ler) is str:
            self.de = de
            self.para = para
            self.ler = ler
        else:
            print 'Objeto nao construido'
    
    def to_string(self):
        return "Transicao{ de:name=%s(id=%2s), para:name=%s(id=%2s), ler:%s }" % (self.de.name,self.de.id,self.para.name,self.para.id,self.ler)
 

### FIM TRANSICAO ###
    
# -----------------------------------------------------------------------------------------------------------------

## OPERACOES ##
from automato import Automato
## Complemento
def complemento(old):
    automato = Automato()
    ## percorre a lista e altera estados finais em normais
    for e in old.estados:
        if e.final:
            e.final = False
            automato.add_estado(e)
        else:
            e.final = True
            automato.add_estado(e)
    ## coloca as transições no novo automato
    automato.transicoes = old.transicoes
    return automato
## fim complemento

## Multiplicacao
def multiplicar(a1,a2):

    # novo automato
    new = Automato()

    # Alfabeto é a combinação dos simbolos dos dois
    new.alfabeto = set(a1.alfabeto+a2.alfabeto)
    
    ## concatenando os nomes
    for e1 in a1.estados:

        for e2 in a2.estados:
            ## novo estados
            new_id = str(e1.id) + str(e2.id)
            new_name = e1.name + e2.name

            ## se for estado inicial
            if e1.initial and e2.initial:
                new.add_estado(Estado(name=new_name,id=new_id,initial=True))

            ## se forem estados finais
            #elif e1.final or e2.final:
            #    new.add_estado(Estado(name=new_name,id=new_id,final=True))
            
            ## se não é normal    
            else: new.add_estado(Estado(name=new_name,id=new_id))

        ## fim for
    
    ## Outro for para fazer as transições, irá combinar leituras com os estados 
    for a in new.alfabeto:
        for e1 in a1.estados:
            for e2 in a2.estados:
                estado_de = new.get_estado(name=str(e1.name)+str(e2.name))
                estado_para = None
                p1 = a1.mover_name(e1.name,a)
                p2 = a2.mover_name(e2.name,a)
                ## se encontrar busca o estado
                if p1 and p2:
                    estado_para = new.get_estado(name=p1+p2)
                    ## cria tansicao
                    new.add_transicao( Transicao(de=estado_de,para=estado_para,ler=a) )
    return new
    
##

### FIM OPERACOES ###
    
# -----------------------------------------------------------------------------------------------------------------

## ARQUIVOS ##

## Salvando automato
def salvar(file_name,automato):
    f = open(file_name,"w") # abre com parametro de escrita
    f.write(automato.print_xml())
    f.close()
    return True


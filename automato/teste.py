#-*- coding: utf-8 -*-

from modulo import Estado, Transicao
import modulo
from automato import Automato

if __name__=='__main__':
    ## criando um novo automato
    a1 = Automato()
    
    ## Adicionando estados
    a1.add_estado( Estado(id=0,name='q0',initial=True) )
    a1.add_estado( Estado(id=1,name='q1') )
    a1.add_estado( Estado(id=2,name='q2',final=True) )

    ## Exibindo estados
    a1.print_estados()

    ## Adicionando transicoes
    a1.add_transicao(
        Transicao(de=a1.get_estado(name='q0'), para=a1.get_estado(name='q1'), ler='a' )
    )    
    a1.add_transicao(
        Transicao(de=a1.get_estado(name='q0'), para=a1.get_estado(name='q0'), ler='b' )
    )
    a1.add_transicao(
        Transicao(de=a1.get_estado(name='q1'), para=a1.get_estado(name='q2'), ler='a' )
    )
    a1.add_transicao(
        Transicao(de=a1.get_estado(name='q2'), para=a1.get_estado(name='q1'), ler='b' )
    )
    a1.add_transicao(
        Transicao(de=a1.get_estado(name='q2'), para=a1.get_estado(name='q2'), ler='a' )
    )

    print 50*'='
    print 5*'-' + 'Testando automato' + 5*'-'
    
    print 'Exibindo transicoes'
    a1.print_transicoes()
    print '\n'
    
    print '-'*5 + 'Consultando estados iniciais'
    print a1.initial().to_string() + '\n'
    
    print 5*'-' + 'consutlando estados finais'
    for e in a1.finals():
        print e.to_string()
    print '\n'

    print 5*'-' + 'verificando cadeia aaabb'
    if a1.aceita('aaabb'): print 'Aceita\n'
    else: print 'Nao aceita\n'

    print 5*'-' + 'consultando o alfabeto'
    print a1.alfabeto

    print '\n'
    print 5*'-' + 'consultando estados esquivalentes'
    a1.print_equivalentes()

    print "\n--Movendo uma cadeia---"
    print a1.mover(0,'abccd')

    print "\n--Complementando o automato---"
    a2 = a1.complemento()
    a2.salvar('a2_complemento_a1.jff')
    print 'Arquivo "a2_complemento_a1.jff" salvo'
    

    
    

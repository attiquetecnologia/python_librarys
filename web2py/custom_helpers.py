
# ---------------------------------------------------------------------------------
# Custom Helpers
# ---------------------------------------------------------------------------------

# Botão de ação no geral serve para customizar botões
# Parametros:
# nome - Nome do botão por padrão assume o icone do tipo
# acao - Função onclick do botão, quando clicado chamar uma função javascript ou window location
# target - ID do destino, div ou tag
# tipo - Especifica que tipo de classe o botão terá
# role - Type propert do botão, button, submit, link
# titulo - Titulo alt do botão
# target - alvo de dados quando não trabalha com ajax function
# url de captura
def btn_acao(nome='',acao=None,target=None,data_target=None,tipo='default',role='button',titulo='default'):
    
    tipos = {'default':'btn-default','edit':'btn-success','del':'btn-danger'
    ,'view':'btn-warning','search':'btn-info','refresh':'btn-default','add':'btn-primary'
    ,'save':'btn-primary','close':'btn-danger','confirm':'btn-success'}
    
    icones = {'default':'','edit':'glyphicon glyphicon-edit'
    ,'del':'glyphicon glyphicon-trash','search':'glyphicon glyphicon-search'
    ,'refresh':'glyphicon glyphicon-refresh','view':'glyphicon glyphicon-zoom-in'
    ,'add':'glyphicon glyphicon-plus','save':'glyphicon glyphicon-save'
    ,'close':'glyphicon glyphicon-remove','confirm':'glyphicon glyphicon-ok'}

    titulos = {'default':'','edit':'Editar','del':'Excluir','view':'Visualizar'
    ,'search':'Pesquisar','refresh':'Atualisar','add':'Adicionar','save':'Salvar'
    ,'close':'Fechar','confirm':'Confirmar'}
    
    click = acao

    return TAG.button(
        TAG.span(_class=icones[tipo]) if tipo != 'default' else ''
        ,nome
        ,_class='btn ' + tipos[tipo] or 'btn-default'
        ,_type=role
        ,_title=titulos[tipo] if tipo != 'default' else ''
        , _onClick=click
        ,**{"_data-target":data_target,"_target":target}
    )

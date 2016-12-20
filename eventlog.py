#-*- coding: utf-8 -*-
import string
import hashlib
import json
from datetime import datetime

class EventLog:
    __doc__ = """
    Esta classe é utilizada para capturar eventos e ações feitas pelo usuário
    ou sessão no sistema, e salva-la na forma de log em banco de dados.
    Seu funcionamento e semelhante as triggers, esta classe é eficiente para
    monitorar eventos específicos do lado de dentro do sistema.
    """
    log_type = 'info'
    log_event = 'insert'
    log_date = datetime.today()
    
    log_id = hashlib.md5(str(datetime.today())) # apenas simula uma sessão

    def logInfo(self,log_event='insert',log_object=None,log_registry=None):

        #validator
        if (log_event is not 'insert' and log_event is not 'update' and log_event is not 'delete'):
            return 'You passed a invalid EventLog. Please use a those options: insert, update, delete, access'
        
        log_message = 'Info! %s %sed. Registry: %s.' % (
                log_object,log_event,log_registry)
        
        print log_message

    def logWarning(self,log_event='access',log_object=None,log_registry=None):

        #validator
        if (log_event is not 'access'):
            return 'You passed a invalid EventLog. Please use a those option: access'
        
        log_message = 'Warning! %s %sed. Registry: %s.' % (
                log_object,log_event,log_registry)
        
        print log_message

    def logError(self,log_event='access',log_object=None,log_registry=None):

        #validator
        if (log_event is not 'access'):
            return 'You passed a invalid EventLog. Please use a those option: access'
        
        log_message = 'Error! Problems in %s at %sed. Registry: %s.' % (
                log_object,log_event,log_registry)
        
        print log_message

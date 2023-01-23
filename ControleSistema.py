import os

#modulo para exibir o diretório atual
def ondeEstou():
    print(os.getcwd())
    return(os.getcwd())

#modulo para mudar de diretório
def irpara(parametro, argumentos):
    try:
        os.chdir(parametro)
    except FileNotFoundError as error: 
        error_number, error_detail = error.args
        print(error_detail)        
    except PermissionError as error:
        error_number, error_detail = error.args
        print(error_detail)
    except NotADirectoryError as error:
        error_number, error_detail = error.args
        print(error_detail)

def voltar():
    local_atual = os.getcwd()
    local_atual = local_atual.split('\\')
    tmr = len(local_atual)
    del(local_atual[tmr-1])
    caminho = ""
    for membro in local_atual:
        caminho = caminho + membro + "/"
    
    try:
        os.chdir(caminho)
    except FileNotFoundError:
        print("Caminho anterior não encontrado")

    
def eventLog(*event):
    
    if os.path.exists("logfile.log") == False:
        with open("logfile.log", "w") as logfile:
            logfile.writelines("Arquivo de registro")
    else:
        with open("logfile.log", "a+") as logfile:
            logfile.writelines(event)

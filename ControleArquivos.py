import os
import ControleArgumentos
import shutil


def criarDiretorio(parametro, argumentos):


    #verifica a presença de argumentos no comando
    #caso não existam argumentos não acontece nada
    requestArgs = ControleArgumentos.buscaArgumentos(argumentos)
    if requestArgs == "sem_argumentos":
        None
    if requestArgs == "argumentos_validados":
        None
    if requestArgs == 0:
        return 0
    
    #analisa se existe o argumento -i e se existir o executa
    if "-i" in argumentos:
        resp = ControleArgumentos.argumentoI()
        if resp == 1:
            None
        else:
            return 0
    
    #caso exista o argumento -d cria o caminho todo
    #caso contrario cria somenteo argumento
    if "-d" in argumentos:
        try:
            os.makedirs(parametro)
            return 0
        except FileExistsError as error1:
            error1 = list[error1.args]
            print(error1[1])
    else:
        try:
            os.mkdir(parametro)
            return 0
        except FileExistsError:
            print("Não é possível criar um diretorio já existente")
        except FileNotFoundError:
            print("Caminho não encontrado")
    
def criarArquivo(parametro, argumentos):
    
    #executa o argumento i
    if "-i" in argumentos:
        resp = ControleArgumentos.argumentoI()
        if resp == 1:
            None
        else:
            return 0
    else:
        with open(parametro, "w") as arquivo_criar:
            None
    
def removerArquivo(parametro, argumentos):

    #executa o argumento i
    if "-i" in argumentos:
        resp = ControleArgumentos.argumentoI()
        if resp == 1:
            None
        else:
            return 0

    #remove o arquivo
    try:
        os.remove(parametro)
    except FileNotFoundError as error:
        args_m = list(error.args)
        print(args_m[1])
    except FileExistsError as error:
        args_m = list(error.args)
        print(args_m[1])

def apagar(parametro, argumentos):
    
    try:
        if os.path.isfile(parametro):
            os.remove(parametro)
        if os.path.isdir(parametro):
            os.rmdir(parametro)
    except FileNotFoundError as error:
        id_erro, mensagem_erro = error.args
        print(mensagem_erro)
    except FileExistsError as error:
        id_erro, mensagem_erro = error.args
        print(mensagem_erro)


def removerDiretorio(parametro, argumentos):
    
    #executa o argumento i
    if "-i" in argumentos:
        resp = ControleArgumentos.argumentoI()
        if resp == 1:
            None
        else:
            return 0
        
    try:
        os.rmdir(parametro)
    except FileNotFoundError:
        print("Arquivo não encontrado")

def listarDiretorio(parametro, argumentos):
    
    if parametro == "":
        
        #tenta acessar o caminho e ler seu registro
        #caso não encontre ou aconteça algum erro o mesmo informa e cancela
        try:
            
            with os.scandir(os.getcwd()) as diretorio_scan:
                print("Exibindo registros do caminho:", os.getcwd())
                print(f'{"Itens":83} {"Tipo"}')
                for item in diretorio_scan:
                    if item.is_file():
                        print(f'{item.name:80} ==> {"arquivo"}')
                        
                    if item.is_dir():
                        print(f'{item.name:80} ==> {"diretório"}')
        except FileNotFoundError:
            print("Caminho não encontrado")
        except FileExistsError:
            print("Caminho não encontrado")
    else:
        try:
            with os.scandir(parametro) as diretorio_scan:
                print("Exibindo registros do caminho:", parametro)
                print(f'{"Itens":83} {"Tipo"}')
                for item in diretorio_scan:
                    if item.is_file():
                        print(f'{item.name:80} ==> {"arquivo"}')
                        
                    if item.is_dir():
                        print(f'{item.name:80} ==> {"diretório"}')
        except FileNotFoundError:
            print("Caminho não encontrado")
        except FileExistsError:
            print("Caminho não encontrado")
    return 0
    
def renomearArquivo(parametro1, parametro2, argumentos):
        
    try:        
        os.rename(parametro1, parametro2)
            
    except FileExistsError as error:
        id_erro, mensagem_erro = error.args
        print(mensagem_erro)

def copiar(parametro1, parametro2, argumentos):
    try:
        if os.path.isfile(parametro1):
            shutil.copy(parametro1, parametro2)
        if os.path.isdir(parametro1):
            
            shutil.copytree(parametro1, parametro2)
    except FileExistsError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    except FileNotFoundError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    except PermissionError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    except ValueError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    
    
    

def mover(parametro1, parametro2, argumentos):

    try:
        shutil.copy(parametro1, parametro2)
    except FileExistsError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    except FileNotFoundError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    except ValueError as error:
        id_erro, id_mensagem = error.args
        print(id_mensagem)
    



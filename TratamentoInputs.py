
import ControleSistema
import ControleArquivos

#método que executa o comando

def executaComandoP2(comando, parametro1, parametro2, argumentos):
    #print("chegou executacomandop2")
    if comando == "renomear":
        #print("identificou")
        ControleArquivos.renomearArquivo(parametro1,parametro2,argumentos)
    elif comando == "copiar":
        ControleArquivos.copiar(parametro1,parametro2,argumentos)
    elif comando == "mover":
        ControleArquivos.copiar(parametro1,parametro2,argumentos)

def executaComando(comando, parametro, argumentos):
    #busca se o comando existe através de um método do mesmo bloco

    if comando == "criardiretorio":
        ControleArquivos.criarDiretorio(parametro, argumentos)
    elif comando == "removerdiretorio":
        ControleArquivos.removerDiretorio(parametro, argumentos)
    elif comando == "criararquivo":
        ControleArquivos.criarArquivo(parametro, argumentos)
    elif comando == "removerarquivo":
        ControleArquivos.removerArquivo(parametro, argumentos)
    elif comando == "localatual":
        ControleSistema.ondeEstou()
    elif comando == "irpara":
        ControleSistema.irpara(parametro, argumentos)
    elif comando == "listar":
        ControleArquivos.listarDiretorio(parametro, argumentos)
    elif comando == "voltar":
        ControleSistema.voltar()
    elif comando == "apagar":
        ControleArquivos.apagar(parametro,argumentos)
    else:
        print("Comando desconhecido, utilize ajuda para exibir ajuda")

def checarMultiParametros(command):
    if command == "renomear":
        return True
    elif command == "copiar":
        return True
    elif command == "mover":
        return True
    else:
        return False

#Separa o comando em (comando parametro argumento)
#Caso o comando utilize mais de 1 argumento ele separa em (comando parametro parametro argumento)
def trataInput(command):
    
    if command == "" or command == None:
        return 0
    #separar o comando e o parametro
    command = command.split()
    #print("Comando split", command)
    executar = command[0]
    #print(executar)
    resp = checarMultiParametros(executar)
   # print(resp)
    parametro = ""
    parametro1 = ""
    parametro2 = ""
    if resp == True:
        parametro1 = command[1]
        parametro2 = command[2]
        #print("parametro1:", parametro1)
        #print("parametro2:", parametro2)
        #separa os argumentos
        args = []
        for arg in command:
            args.append(arg)
        try:
            args.remove(executar)
            args.remove(parametro1)
            args.remove(parametro2)
            #print("argumentos:", args)
        except ValueError:
            None
       # print("chegou aqui")
        executaComandoP2(executar, parametro1, parametro2, args)

    else:
        #print("Não chegou aqui")
        if len(command) == 1:
            parametro = ""
        elif len(command) > 1:
            parametro = command[1]
        

        #separa os argumentos
        args = []
        for arg in command:
            args.append(arg)
        try:
            args.remove(executar)
            args.remove(parametro)
        except ValueError:
            None
        executaComando(executar, parametro, args)


    


        
            


    




import os



def buscaArgumentos(argumentos):

    #retorno sem argumentos
    if argumentos == None:
        return ("sem_argumentos")

    #Dicionário que contém os argumentos disponíveis no sistema
    argsDisponiveis = {
        "-i" : "Pergunta se você realmente deseja executar o comando",
        "-d" : "Força recursividade para executar o comando"
    }

    #Verifica se entre os argumentos existentes eles estão no dicionário
    #Caso o argumento não exista na lista o argumento ele retorna 0 cancelando a thread
    for arg in argumentos:
        if arg in argsDisponiveis:
            continue
        else:
            print("O argumento:", arg, "não é válido, consulte os argumentos disponíveis")
            return (0)

    #caso tudo ocorra corretamente retorna o valor como validado e dá prosseguimento
    return ("argumentos_validados")

def argumentoI():
    #Argumento simples que apenas pergunta se você deseja usar o comando mesmo
    while 10 == 10:
        opcao = str(input("Você realmente deseja executar esta ação? S/N: "))
        opcao = opcao.upper()
        if opcao == "S":
            return 1
        elif opcao == "N":
            return 0
        else:
            print("Opção inválida, utilize S / N")



            
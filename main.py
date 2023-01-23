'''
Projeto de Bash 
-Comandos inseridos

-criardiretorio (nome_pasta) V
-removerpasta (nome_pasta) V 
-removerarquivo (nome_arquivo) V
-criararquivo (nome_arquivo) V
-listar (caminho) V
-ajuda V
-localatual V
'''


import ControleArquivos
import ControleSistema
import TratamentoInputs
import os


def main():
    while 1 == 1:
        comandoInserir = str(input("$Bash//: "))
        TratamentoInputs.trataInput(comandoInserir)
        
main()

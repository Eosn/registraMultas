'''
Éllen Oliveira Silva Neves (20202BSI0071)
Trabalho solicitado pelo professor da disciplina de Programação II, Hilário Seibel Junior
'''

import os
import pickle


def menu():  # módulo que imprime o menu
    print("------ MENU: SELECIONE A OPÇÃO ------")
    print("1) Cadastrar novo motorista")
    print("2) Cadastrar novo veículo")
    print("3) Alterar proprietário do veículo")
    print("4) Cadastrar nova infração")
    print("5) Sair")
    return None


def salvarArq(motoristas, veiculos, infracoes, naturezas):
    with open("multas.bin", "wb") as arq:  # antes de fechar completamente o programa, reescreva o arquivo com as novas informações
        pickle.dump(motoristas, arq)
        pickle.dump(veiculos, arq)
        pickle.dump(infracoes, arq)
        pickle.dump(naturezas, arq)
    return None


def cadastrarMotorista(motoristas):  # opcao 1
    cnh = input("CNH: ")
    if cnh in motoristas:  # se a chave cnh já existir, dá erro
        print("Erro! CNH já cadastrada.")

    else:  # se não, cria nova chave
        nome = input("Nome: ")
        dtVencimento = input("Data de vencimento (DD/MM/AAAA): ").split("/")
        dtVencimento = (int(dtVencimento[0]), int(dtVencimento[1]), int(dtVencimento[2]))  # converte os itens da lista c/ data pra int e salva em tupla
        motoristas[cnh] = (nome, dtVencimento)
    return motoristas


def cadastrarVeiculo(veiculos):  # opcao 2
    placa = input("Placa: ")
    if placa in veiculos:  # se a chave placa já existir, dá erro
        print("Erro! Placa já cadastrada.")

    else:  # se não, cria nova chave
        cnh = input("CNH: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        veiculos[placa] = (cnh, modelo, cor)
    return veiculos


def alterarProprietario(veiculos, motoristas):  # opcao 3
    placa = input("Placa: ")
    if placa in veiculos:  # verifica se a placa foi cadastrada
        cnhNovo = input("CNH do novo proprietário: ")
        if cnhNovo in motoristas:  # verifica se o cnh foi cadastrado
            modelo = veiculos[placa][1]
            cor = veiculos[placa][2]
            veiculos[placa] = (cnhNovo, modelo, cor)  # reescreve conteúdo da chave

        else:
            print("Erro! CNH não cadastrado.")

    else:
        print("Erro! Placa não cadastrada.")
    return veiculos


def cadastrarInfracao(infracoes, naturezas, veiculos):  # opcao 4
    numero = len(infracoes) + 1
    data = input("Data da infração (DD/MM/AAAA): ").split("/")
    data = (int(data[0]), int(data[1]), int(data[2]))  # converte os itens da lista c/ data pra int e salva em tupla

    placa = input("Placa: ")
    if placa in veiculos:
        print("Escolha a natureza da infração: 1) leve; 2) média; 3) grave; 4) gravíssima")

        natureza = int(input(""))
        while (natureza < 1) or (natureza > 4):
            natureza = int(input("Escolha natureza válida: "))

        if natureza == 1:
            natureza = 3
        elif natureza == 2:
            natureza = 4
        elif natureza == 3:
            natureza = 5
        elif natureza == 4:
            natureza = 7

        for nat in naturezas:  # percorre as chaves ("leve", "media", etc)
            if naturezas[nat] == natureza:  # se o conteúdo da chave for igual ao numero digitado
                natureza = nat  # salva o nome da chave
        infracoes.append((numero, data, placa, natureza))  # adiciona nova infracao na lista
    else:
        print("Erro! Placa não cadastrada.")
    return infracoes


def main():
    if os.path.isfile('multas.bin'):  # se o arquivo existir, abra e armazene os dicionários
        with open("multas.bin", "rb") as arq:
            motoristas = pickle.load(arq)
            veiculos = pickle.load(arq)
            infracoes = pickle.load(arq)
            naturezas = pickle.load(arq)
    else:  # se não, crie dicionários e lista
        motoristas = {}
        veiculos = {}
        infracoes = []
        naturezas = {"Leve": 3, "Media": 4, "Grave": 5, "Gravissima": 7}

    menu()
    opcao = int(input(""))
    while (opcao < 1) or (opcao > 5):
        opcao = int(input("Insira opção válida: "))

    while opcao != 5:
        if opcao == 1:
            motoristas = cadastrarMotorista(motoristas)
        elif opcao == 2:
            veiculos = cadastrarVeiculo(veiculos)
        elif opcao == 3:
            veiculos = alterarProprietario(veiculos, motoristas)
        elif opcao == 4:
            infracoes = cadastrarInfracao(infracoes, naturezas, veiculos)

        salvarArq(motoristas, veiculos, infracoes, naturezas)

        menu()
        opcao = int(input(""))
        while (opcao < 1) or (opcao > 5):
            opcao = int(input("Insira opção válida: "))

    print("Até a próxima!")  # encerre


if __name__ == "__main__":
    main()

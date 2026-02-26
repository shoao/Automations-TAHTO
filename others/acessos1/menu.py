from logo_tahto import logo
from selecionar_arquivo import selecionarArquivo
import os
from pathlib import Path

def limparTela():
	os.system('cls')

def cabecalho():
	print(logo)
	print("------== Gestão de Acessos ==------")
	print("\n")



planilha_padrao = None
arquivo_gip = None

limparTela()



while True:
	limparTela()
	cabecalho()
	print(planilha_padrao)
	print(arquivo_gip)
	print("Arquivos selecionados: Nemhum")
	print("\n")
	print("1 - Selecionar Arquivos")
	print("2 - Verificar Matrículas")
	print("3 - Gerar Beneficiários")

	escolha = input("Escolha uma opção: ")

	if escolha == "1":
		limparTela()
		cabecalho()

		planilha_padrao, arquivo_gip = selecionarArquivo()

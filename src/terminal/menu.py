from src.terminal.logo_tahto import logo
from src.core.selecionar_arquivo import selecionarArquivo
from src.core.filtrar import verificarMatricula
from src.core.gerar_beneficiarios import gerarBeneficiarios
from src.core.buscar_matriculas import buscarMatriculas
import os
from pathlib import Path

def iniciarMenu():

	planilha_padrao = None
	arquivo_gip = None

	def limparTela():
		os.system('cls')

	limparTela()

	def cabecalho():
		print(f"{logo}\n")

	def verificarArquivos():
		if planilha_padrao == None or arquivo_gip == None:
			print("Arquivos selecionados: Nemhum")

		else:
			print(f"Arquivos selecionados: {planilha_padrao}, {arquivo_gip}")




	while True:
		limparTela()
		cabecalho()
		verificarArquivos()
		print("\n")
		print("[1] - Selecionar Arquivos")
		print("[2] - Perda de Acessos")
		print("[3] - Verificar Matricula(s)")

		escolha = input("\nEscolha uma opção: ")

		if escolha == "1":
			limparTela()
			cabecalho()

			planilha_padrao, arquivo_gip = selecionarArquivo()

		elif escolha == "2":

			while True:
				limparTela()
				cabecalho()

				print("--- Perda de Acessos ---\n")

				print("[1] - Verificar Planilha Padrão")
				print("[2] - Gerar arquivo Beneficiarios")
				print("[0] - Voltar")
				escolha = input("\nEscolha uma opção: ")

				if escolha == "1":
					limparTela()
					cabecalho()
					matriculas = verificarMatricula(planilha_padrao, arquivo_gip)

				elif escolha == "2":
					limparTela()
					cabecalho()
					gerarBeneficiarios(matriculas)

				elif escolha == "0":
					break


		elif escolha == "3":
			limparTela()
			cabecalho()
			buscarMatriculas(arquivo_gip)

from pathlib import Path

def selecionarArquivo():
	# pasta atual do script
	pasta = Path(__file__).parent

	# lista só arquivos .xlsx
	arquivos = list(pasta.glob("*.xlsx"))

	# mostra os arquivos pro usuário
	print("Selecione a Planilha Padrão de acesso:")
	for i, f in enumerate(arquivos, start=1):
	    print(f"{i} - {f.name}")

	# pede pra escolher a planilha padrão
	escolha = int(input(": "))
	planilha_padrao = arquivos[escolha - 1]
	planilha_padrao = planilha_padrao.name

	print(f"\nVocê selecionou: {planilha_padrao}\n")

	# ESCOLHENDO O GIP

	print("Selecione o arquivo do GIP (em xlsx):")
	for i, f in enumerate(arquivos, start=1):
	    print(f"{i} - {f.name}")

	# pede pra escolher o gip
	escolha = int(input(": "))
	arquivo_gip = arquivos[escolha - 1]
	arquivo_gip = arquivo_gip.name

	print(f"\nVocê selecionou: {arquivo_gip}\n")

	return planilha_padrao, arquivo_gip
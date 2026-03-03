from pathlib import Path
def selecionarArquivo():
    pasta = Path(__file__).resolve().parent.parent.parent / "planilhas"

    arquivos = list(pasta.glob("*.xlsx"))

    if not arquivos:
        print("Nenhuma planilha encontrada.")
        return None, None

    print("Selecione a Planilha Padrão de acesso:")
    for i, f in enumerate(arquivos, start=1):
        print(f"{i} - {f.name}")

    escolha = int(input(": "))
    planilha_padrao = arquivos[escolha - 1]

    print(f"\nVocê selecionou: {planilha_padrao.name}\n")

    print("Selecione o arquivo do GIP (em xlsx):")
    for i, f in enumerate(arquivos, start=1):
        print(f"{i} - {f.name}")

    escolha = int(input(": "))
    arquivo_gip = arquivos[escolha - 1]

    print(f"\nVocê selecionou: {arquivo_gip.name}\n")

    return planilha_padrao, arquivo_gip

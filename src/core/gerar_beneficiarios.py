from openpyxl import Workbook
from pathlib import Path

def gerarBeneficiarios(matriculas):
    beneficiarios = Workbook()
    aba_beneficiarios = beneficiarios.active

    aba_beneficiarios.title = "BENEFICIARIOS"

    aba_beneficiarios["A1"].value = "MATRICULA"

    for linha, matricula in enumerate(matriculas, start=2):
        aba_beneficiarios[f"A{linha}"] = matricula

    # 👇 única mudança real
    pasta = Path(__file__).resolve().parent.parent.parent / "planilhas"
    beneficiarios.save(pasta / "BENEFICIARIOS.xlsx")

    while True:
        print(f"\nArquivo criado, matriculas: {matriculas}")
        input("\nDigite para sair: ")
        break
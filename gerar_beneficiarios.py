from openpyxl import Workbook

def gerarBeneficiarios(matriculas):
    beneficiarios = Workbook()
    aba_beneficiarios = beneficiarios.active

    aba_beneficiarios.title = "BENEFICIARIOS"

    aba_beneficiarios["A1"].value = "MATRICULA"

    for linha, matricula in enumerate(matriculas, start=2):
        aba_beneficiarios[f"A{linha}"] = matricula

    beneficiarios.save("BENEFICIARIOS.xlsx")

    while True:
        print(f"Arquivo criado, matriculas: {matriculas}\n")
        x = input("Digite para sair: ")
        break
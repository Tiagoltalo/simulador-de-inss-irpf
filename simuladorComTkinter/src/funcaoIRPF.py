from .funcaoINSS import calcularINSS

def calcularIRPF():
    baseDeCalculo = calcularINSS()[1]

    # Baseado na base de cálculo faremos o cálculo do imposto de renda que evolui de forma progressiva

    if baseDeCalculo >= 2259.21 and baseDeCalculo <= 2826.65:
        aliquotaIR = 0.075
        deducao = 182.16
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    elif baseDeCalculo >= 2826.66 and baseDeCalculo <= 3751.05:
        aliquotaIR = 0.15
        deducao = 394.16
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    elif baseDeCalculo >= 3751.06 and baseDeCalculo <= 4664.68:
        aliquotaIR = 0.225
        deducao = 675.49
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    elif baseDeCalculo > 4664.68:
        aliquotaIR = 0.275
        deducao = 908.73
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    return round(impostoDeRenda, 2), aliquotaIR, deducao
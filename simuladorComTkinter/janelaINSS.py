from tkinter import *
from tkinter import ttk
from src.funcaoINSS import calcularINSS
from src.variaveisEFuncoesAuxiliares import criadorDeFrames

# Tela que recebe as informações necessárias para o cálculo
def inputINSS(janela, telaInicial):
    salario = DoubleVar()
    segurado = StringVar()
    pensao = DoubleVar()
    dependentes = DoubleVar()
    modalidade = StringVar()

    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = ttk.Frame(janela, padding=10)
    framePrincipal.pack(fill="both", expand=True)

    frameUm = ttk.Frame(framePrincipal, padding=10)
    frameDois = ttk.Frame(framePrincipal, padding=10)
    frameTres = ttk.Frame(framePrincipal, padding=10)
    frameQuatro = ttk.Frame(framePrincipal, padding=10)
    frameCinco = ttk.Frame(framePrincipal, padding=10)

    frameUm.pack(expand=True)
    frameDois.pack(expand=True)
    frameTres.pack(expand=True)
    frameQuatro.pack(expand=True)
    frameCinco.pack(expand=True)

    Label(frameUm, text="Simulador de INSS", font=("Arial", 16, "bold")).grid(column=1, row=0)

    # Salário
    Label(frameDois, text="Salário: ").grid(column=0, row=0)
    Entry(frameDois, textvariable=salario, width=20).grid(column=1, row=0)

    # Tipo de Segurado
    Label(frameDois, text="Segurado: ").grid(column=2, row=0)
    Entry(frameDois, textvariable=segurado, width=20).grid(column=3, row=0)

    # Pensão Alimentícia
    Label(frameTres, text="Pensão: ").grid(column=0, row=0)
    Entry(frameTres, textvariable=pensao, width=20).grid(column=1, row=0)

    # Dependentes
    Label(frameTres, text="Dependentes: ").grid(column=2, row=0)
    Entry(frameTres, textvariable=dependentes, width=20).grid(column=3, row=0)

    # Modalidade
    Label(frameQuatro, text="Modalidade: ").grid(column=0, row=0)
    Entry(frameQuatro, textvariable=modalidade, width=20).grid(column=1, row=0)

    Button(frameCinco, text="Calcular INSS", height=1, width=15, command=lambda: resultadoINSS(janela, telaInicial, salario, segurado, pensao, dependentes, modalidade)).grid(column=1, row=0, padx=5)
    Button(frameCinco, text="Voltar", height=1, width=15, command=lambda: telaInicial()).grid(column=2, row=0, padx=5)


# Tela que mostra os resultados do cálculo
def resultadoINSS(janela, telaInicial, salario, segurado, pensao, dependentes, modalidade):
    # Cálculo do INSS
    contribuicaoDoINSS, aliquotaDoINSS, deducaoDoINSS = calcularINSS(salario, segurado, pensao, dependentes, modalidade)


    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = ttk.Frame(janela, padding=10)
    framePrincipal.pack(fill="both", expand=True)

    frame = criadorDeFrames(framePrincipal, 7)

    # frameUm = ttk.Frame(janela, padding=10)
    # frameDois = ttk.Frame(janela, padding=10)
    # frameTres = ttk.Frame(janela, padding=10)
    # frameQuatro = ttk.Frame(janela, padding=10)
    # frameCinco = ttk.Frame(janela, padding=10)
    # frameSeis = ttk.Frame(janela, padding=10)
    # frameSete = ttk.Frame(janela, padding=10)

    # frameUm.pack(expand=True)
    # frameDois.pack(expand=True)
    # frameTres.pack(expand=True)
    # frameQuatro.pack(expand=True)
    # frameCinco.pack(expand=True)
    # frameSeis.pack(expand=True)
    # frameSete.pack(expand=True)


    Label(frame[0], text="Resultado do Cálculo do INSS", font=("Arial", 16, "bold")).grid(column=1, row=0)

    # Salário
    Label(frame[1], text="Salário: ").grid(column=0, row=0)
    Label(frame[1], text=f"{salario.get()}").grid(column=1, row=0)

    # Tipo de Segurado
    Label(frame[2], text="Segurado: ").grid(column=0, row=0)
    Label(frame[2], text=f"{segurado.get()}").grid(column=1, row=0)

    # Alíquota do INSS
    Label(frame[3], text="Alíquota: ").grid(column=0, row=0)
    Label(frame[3], text=f"{aliquotaDoINSS.get()}%").grid(column=1, row=0)

    # Dedução do INSS
    Label(frame[4], text="Dedução: ").grid(column=0, row=0)
    Label(frame[4], text=f"{deducaoDoINSS.get()}").grid(column=1, row=0)

    # Contribuição do INSS
    Label(frame[5], text="Contribuição: ").grid(column=0, row=0)
    Label(frame[5], text=f"{contribuicaoDoINSS.get()}").grid(column=1, row=0)

    Button(frame[6], text="Voltar", height=1, width=15, command=lambda: telaInicial()).grid(column=1, row=0, padx=5)
from tkinter import *
from tkinter import ttk
from src.funcaoIRPF import calcularIRPF

def inputIRPF(janela, telaInicial):
    salario = DoubleVar()
    segurado = StringVar()
    pensao = DoubleVar()
    dependentes = DoubleVar()

    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = ttk.Frame(janela, padding=10)
    framePrincipal.pack(fill="both", expand=True)

    frameUm = ttk.Frame(framePrincipal, padding=10)
    frameDois = ttk.Frame(framePrincipal, padding=10)
    frameTres = ttk.Frame(framePrincipal, padding=10)
    frameQuatro = ttk.Frame(framePrincipal, padding=10)

    frameUm.pack(expand=True)
    frameDois.pack(expand=True)
    frameTres.pack(expand=True)
    frameQuatro.pack(expand=True)

    Label(frameUm, text="Simulador de IRPF", font=("Arial", 16, "bold")).grid(column=1, row=0)

    # Salário
    Label(frameDois, text="Salário: ").grid(column=0, row=0)
    Entry(frameDois, textvariable=salario,width=20).grid(column=1, row=0)

    # Tipo de Segurado
    Label(frameDois, text="Tipo de Segurado: ").grid(column=2, row=0)
    Entry(frameDois, textvariable=segurado, width=20).grid(column=3, row=0)

    # Pensão Alimentícia
    Label(frameTres, text="Pensão: ").grid(column=0, row=0)
    Entry(frameTres, textvariable=pensao, width=20).grid(column=1, row=0)

    # Dependentes
    Label(frameTres, text="Dependentes: ").grid(column=2, row=0)
    Entry(frameTres, textvariable=dependentes, width=20).grid(column=3, row=0)

    Button(frameQuatro, text="Calcular IRPF", height=1, width=15, command=lambda: resultadoIRPF(janela, telaInicial, salario, segurado, pensao, dependentes)).grid(column=1, row=0, padx=5)
    Button(frameQuatro, text="Voltar", height=1, width=15, command=lambda: telaInicial()).grid(column=2, row=0, padx=5)

def resultadoIRPF(janela, telaInicial, salario, segurado, pensao, dependentes):
    # Cálculo do IRPF
    impostoDeRenda, aliquotaDoIRPF, deducaoDoIRPF = calcularIRPF()

    for widget in janela.winfo_children():
        widget.destroy()

    frameUm = ttk.Frame(janela, padding=10)
    frameDois = ttk.Frame(janela, padding=10)
    frameTres = ttk.Frame(janela, padding=10)
    frameQuatro = ttk.Frame(janela, padding=10)
    frameCinco = ttk.Frame(janela, padding=10)
    frameSeis = ttk.Frame(janela, padding=10)

    frameUm.pack(expand=True)
    frameDois.pack(expand=True)
    frameTres.pack(expand=True)
    frameQuatro.pack(expand=True)
    frameCinco.pack(expand=True)
    frameSeis.pack(expand=True)

    Label(frameUm, text="Resultado do Cálculo do IRPF", font=("Arial", 16, "bold")).grid(column=1, row=0)

    # Base de Cálculo
    Label(frameDois, text="Base de Cálculo: ").grid(column=0, row=0)
    Label(frameDois, text=f"{salario.get()}").grid(column=1, row=0)

    # Alíquota do IRPF
    Label(frameTres, text="Alíquota: ").grid(column=0, row=0)
    Label(frameTres, text=f"{aliquotaDoIRPF.get()}").grid(column=1, row=0)

    # Dedução do IRPF
    Label(frameQuatro, text="Dedução: ").grid(column=0, row=0)
    Label(frameQuatro, text=f"{deducaoDoIRPF}")

    # Segurado
    Label(frameCinco, text="Segurado: ").grid(column=0, row=0)
    Label(frameCinco, text=f"{segurado.get()}").grid(column=1, row=0)

    # Pensão Alimentícia
    Label(frameSeis, text="Pensão: ").grid(column=0, row=0)
    Label(frameSeis, text=f"{pensao.get()}").grid(column=1, row=0)

    # Quantidade de Dependentes
    Label(frameSete, text="Dependentes: ").grid(column=0, row=0)
    Label(frameSete, text=f"{dependentes.get()}").grid(column=1, row=0)

    # Desconto
    Label(frameOito, text="Desconto: ").grid(column=0, row=0)
    Label(frameOito, text=f"{desconto.get()}").grid(column=1, row=0)

    # Imposto de Renda
    Label(frameNove, text="Imposto de Renda: ").grid(column=0, row=0)
    Label(frameNove, text=f"{impostoDeRenda.get()}").grid(column=1, row=0)

    Button(frameDez, text="Voltar", height=1, width=15, command=lambda: telaInicial()).grid(column=1, row=0, padx=5)
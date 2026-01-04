from tkinter import *
from tkinter import ttk

deducaoPorDependente = 189.59
descontoSimplificado = 607.20

seguradosComAliquotaProgressiva = [
    "empregado",
    "empregado doméstico",
    "trabalhador avulso"
]

seguradosSemAliquotaProgressiva = [
    "contribuinte individual",
    "segurado facultativo",
    "segurado especial",
]

tiposDeModalidade = [
    "plano normal",
    "plano simplificado",
    "baixa renda",
    "contribuição obrigatória",
    "contribuição optativa"
]

def criadorDeFrames(framePrincipal, quantidade):
    listaDeFrames = []

    for i in range(quantidade):
        listaDeFrames.append(ttk.Frame(framePrincipal, padding=10).pack(expand=True))

    return listaDeFrames
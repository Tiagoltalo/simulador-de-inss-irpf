from tkinter import *
from tkinter import ttk
from janelaINSS import inputINSS
from janelaIRPF import inputIRPF

def telaInicial():
    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = ttk.Frame(janela, padding=10)
    framePrincipal.pack(fill="both", expand=True)

    frameUm = ttk.Frame(framePrincipal, padding=10)
    frameDois = ttk.Frame(framePrincipal, padding=10)
    frameTres = ttk.Frame(framePrincipal, padding=10)

    frameUm.pack(expand=True)
    frameDois.pack(expand=True)
    frameTres.pack(expand=True)

    Label(frameUm,text="Simulador de IRPF e INSS", font=("Arial", 16, "bold")).grid(column=1, row=0)
    Button(frameDois, text="IRPF", height=1, width=4, command=lambda: inputIRPF(janela, telaInicial)).grid(column=0, row=0, padx=5)
    Button(frameDois, text="INSS", height=1, width=4, command=lambda: inputINSS(janela, telaInicial)).grid(column=1, row=0, padx=5)
    Button(frameDois, text="Sair", height=1, width=4,command=janela.destroy).grid(column=2, row=0, padx=5)

    janela.mainloop()

janela = Tk()
janela.title("Simulador de IRPF e INSS")
janela.geometry("700x500")

telaInicial()
import ttg
import tkinter as tk
from tkinter import messagebox

def TabelaOr():
    tabela = ttg.Truths(['p', 'q'], ['p or q'], ints=False)
    return str(tabela)

def TabelaAnd():
    tabela = ttg.Truths(['p', 'q'], ['p and q'], ints=False)
    return str(tabela)

def TabelaNot():
    tabela = ttg.Truths(['p'], ['not p'], ints=False)
    return str(tabela)

def TabelaXor():
    tabela = ttg.Truths(['p', 'q'], ['p xor q'], ints=False)
    return str(tabela)

def TabelaImplies():
    tabela = ttg.Truths(['p', 'q'], ['p implies q'], ints=False)
    return str(tabela)

def exibir_tabela(tabela):
    messagebox.showinfo("Tabela Verdade", tabela)

def main():
    root = tk.Tk()
    root.title("Tabelas Lógicas")

    botoes = [
        ("OR", TabelaOr),
        ("AND", TabelaAnd),
        ("NOT", TabelaNot),
        ("XOR", TabelaXor),
        ("IMPLIES", TabelaImplies)
    ]

    for nome, funcao in botoes:
        botao = tk.Button(root, text=nome, command=lambda f=funcao: exibir_tabela(f()))
        botao.pack()

    root.mainloop()

if __name__ == "__main__":
    main()


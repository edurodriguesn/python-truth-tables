import ttg

def TabelaOr():
    tabela = ttg.Truths(['p', 'q'], ['p or q'], ints=False)
    return tabela

def TabelaAnd():
    tabela = ttg.Truths(['p', 'q'], ['p and q'], ints=False)
    return tabela

def TabelaNot():
    tabela = ttg.Truths(['p'], ['not p'], ints=False)
    return tabela

def TabelaXor():
    tabela = ttg.Truths(['p', 'q'], ['p xor q'], ints=False)
    return tabela

def TabelaImplies():
    tabela = ttg.Truths(['p', 'q'], ['p implies q'], ints=False)
    return tabela

def main():
    TipoTabela = 0
    while TipoTabela < 1 or TipoTabela > 5:
        TipoTabela = int(input("Gerar tabela da porta: \nOR (1) | AND (2) | NOT (3)\nXOR (4) | IMPLIES (5)\n"))

        if TipoTabela == 1:
            tabela = TabelaOr()
        elif TipoTabela == 2:
            tabela = TabelaAnd()
        elif TipoTabela == 3:
            tabela = TabelaNot()
        elif TipoTabela == 4:
            tabela = TabelaXor()
        elif TipoTabela == 5:
            tabela = TabelaImplies()
        else:
            tabela = "Inválido"

        print(tabela)

if __name__ == "__main__":
    main()


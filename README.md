# Gerador de Tabelas Verdade

Estes programas em python utilizam o pacote Truth Table Generator para gerar tabelas verdade e Tkinter para a interface gráfica. O arquivo `Colab_TruthTableGenerador.ipynb` pode ser aberto no [Google Colab](https://colab.research.google.com/).

## Instalação

1. É necessário ter o Python3 instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale o pacote do Tkinter se estiver no Linux:
    ```bash
    sudo apt-get install python3-tk
    ```
3. Utilize um ambiente virtual para gerenciar as dependências do projeto. Para criar um novo ambiente virtual, abra um terminal, navegue até a pasta do projeto e então execute os comandos:

    ```bash
    python3 -m venv myvenv
    ```

4. Ative o ambiente virtual. O método para ativar o ambiente virtual depende do sistema operacional:

    - No Linux ou macOS:
    
        ```bash
        source myvenv/bin/activate
        ```
    
    - No Windows (PowerShell):
    
        ```bash
        .\myvenv\Scripts\Activate.ps1
        ```
5. Instale as dependências do projeto. Execute o seguinte comando no terminal:

    ```bash
    pip install -r requirements.txt
    ```

    Isso instalará todas as dependências listadas no arquivo `requirements.txt`.

## Executando o programa

Com o ambiente virtual ativo e as dependências instaladas já é possível executar os programas com os seguinte comandos:

1. Executar a versão de terminal:
    ```bash
    python3 TruthTableGenerator.py.py
    ```
2. Executar a interface gráfica:
    ```bash
    python3 GUI_TruthTableGenerator.py
        

# Projeto OCR com PyInstaller
Este repositório contém um script Python que utiliza o `ocrmypdf` para converter PDFs escaneados para PDFs pesquisáveis utilizando OCR para o idioma português.

## Configuração do Ambiente
### Pré-requisitos
Certifique-se de ter o Python instalado em seu sistema. O Python pode ser baixado de [https://www.python.org/downloads/](https://www.python.org/downloads/). Durante a instalação, adicione o Python ao seu PATH.

### Criar e Ativar o Ambiente Virtual
Clone o repositório e navegue até o diretório do projeto. Então, crie um ambiente virtual e ative-o:

#### Windows
```bash
python -m venv env
env\Scripts\activate
```

#### Linux/MacOS
```bash
python3 -m venv env
source env/bin/activate
```

### Instalar dependências
Instale todas as dependências necessárias executando:
```bash
pip install -r requirements.txt
```

## Criar um executável
### Comando
Para compilar este projeto em um executável standalone, utilize o PyInstaller:
```bash
pyinstaller --onefile --hidden-import PIL my_script.py
```

### Distribuição
O executável gerado pode ser encontrado na pasta **dist/** e está pronto para ser distribuído. Certifique-se de incluir quaisquer arquivos de dados adicionais necessários, especialmente se o suporte ao idioma não estiver embutido diretamente no executável.

### Nota
Este projeto presume que os dados de idioma do Tesseract para português estão instalados e configurados corretamente no sistema onde o executável será rodado. Para sistemas Linux, isso geralmente pode ser instalado via gerenciador de pacotes com um comando como sudo apt install tesseract-ocr-por.

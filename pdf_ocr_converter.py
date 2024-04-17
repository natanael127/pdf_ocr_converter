import ocrmypdf
import os
import time

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    ocrmypdf.configure_logging(verbosity=ocrmypdf.Verbosity.quiet, progress_bar_friendly=False)
    while True:
        clear_screen()
        print("CONVERSOR DE ARQUIVOS PDF PARA O MODELO OCR")
        print()
        input_pdf = input("Arraste e solte o arquivo PDF nesta janela e tecle ENTER:\n")
        input_pdf = input_pdf.strip().replace('"', '')      # Remove spaces and quotes from the file path
        result = -1
        try:
            result = ocrmypdf.ocr(input_pdf, input_pdf, language='por')
        except KeyboardInterrupt:
            raise   # Handle on level up
        except Exception as e:
            print(f"Erro ao converter o arquivo. Detalhes: {e}")
        if result == 0:
            print("Conversão realizada com sucesso!")
        else:
            print(f"Erro ao converter o arquivo. Código de erro: {result}")
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        time.sleep(2)

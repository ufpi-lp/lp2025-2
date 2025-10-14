from app.cadastro import CadastroPessoasService
from app.text.rich.telas import Menu, MenuOption, CadastroPessoasTela
from rich.console import Console

def main():
    service = CadastroPessoasService()
    tela = CadastroPessoasTela(service)
    def cadastrar_pessoa():
        tela.cadastrar()
    def listar_pessoas():
        tela.listar()
    def sair():
        service.salvar_csv()
        Console().print("[bold magenta]Dados salvos em pessoas.csv. Saindo...[/]")
        exit()

    options = [
        MenuOption("1", "Cadastrar pessoa", cadastrar_pessoa),
        MenuOption("2", "Listar pessoas cadastradas", listar_pessoas),
        MenuOption("s", "Sair", sair)
    ]
    menu = Menu("Menu de Cadastro de Pessoas", options)
    while True:
        menu.display()
        selected_option = menu.get_choice()
        selected_option.execute()

if __name__ == "__main__":
    main()
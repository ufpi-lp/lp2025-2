from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import readchar

def wait_enter():
    while True:
        key = readchar.readkey()
        if key in ('\r', '\n'):
            break

class MenuOption:
    def __init__(self, key, description, action):
        self.key = key
        self.description = description
        self.action = action

    def execute(self):
        self.action()

class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options
        self.console = Console()

    def display(self):
        self.console.clear()
        menu_text = "\n".join([f"[bold cyan]{opt.key}[/]: {opt.description}" for opt in self.options])
        self.console.print(Panel(menu_text, title=self.title, expand=False))

    def get_choice(self):
        valid_keys = [opt.key for opt in self.options]
        while True:
            choice = Prompt.ask("Escolha uma opção", choices=valid_keys)
            for opt in self.options:
                if opt.key == choice:
                    return opt

class CadastroPessoasTela:
    def __init__(self, service):
        self.service = service

    def cadastrar(self):
        console = Console()
        cpf = Prompt.ask("[bold yellow]Digite o CPF[/]").strip()
        if cpf in self.service.pessoas:
            console.print(f"[red]CPF já cadastrado![/]")
            console.print("[dim]Pressione apenas ENTER para continuar[/]")
            wait_enter()
            return
        nome = Prompt.ask("[bold yellow]Digite o nome[/]").strip()
        telefone = Prompt.ask("[bold yellow]Digite o telefone[/]").strip()
        self.service.cadastrar(cpf, nome, telefone)
        console.print(f"[bold blue]Pessoa cadastrada com sucesso![/]")
        console.print("[dim]Pressione apenas ENTER para continuar[/]")
        wait_enter()

    def listar(self):
        console = Console()
        pessoas = self.service.listar()
        if not pessoas:
            console.print("[yellow]Nenhuma pessoa cadastrada.[/]")
        else:
            table = Table(title="Pessoas Cadastradas")
            table.add_column("CPF", style="cyan", no_wrap=True)
            table.add_column("Nome", style="green")
            table.add_column("Telefone", style="magenta")
            for cpf, dados in pessoas.items():
                table.add_row(cpf, dados["nome"], dados["telefone"])
            console.print(table)
        console.print("[dim]Pressione apenas ENTER para continuar[/]")
        wait_enter()


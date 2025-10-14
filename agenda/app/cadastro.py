import csv
import os

class CadastroPessoasService:
    def __init__(self, filename="./dados/pessoas.csv"):
        self.filename = filename
        self.pessoas = {}
        self.carregar_csv()

    def carregar_csv(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cpf = row["CPF"]
                    self.pessoas[cpf] = {"nome": row["Nome"], "telefone": row["Telefone"]}

    def cadastrar(self, cpf, nome, telefone):
        if cpf in self.pessoas:
            return False
        self.pessoas[cpf] = {"nome": nome, "telefone": telefone}
        return True

    def listar(self):
        return self.pessoas

    def salvar_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["CPF", "Nome", "Telefone"])
            for cpf, dados in self.pessoas.items():
                writer.writerow([cpf, dados["nome"], dados["telefone"]])
# Manipulando Dados de Pessoas em Arquivo Texto com Python

## **Objetivo**  

Criar um programa em Python para cadastrar, listar, salvar e carregar dados de pessoas em um arquivo texto, utilizando estruturas de dados como dicionários e funções.

## **Conteúdo Básico**  

### **1. Introdução**  
- Por que armazenar dados em arquivos?  
  - Persistência de dados após o fechamento do programa.  
  - Facilidade de recuperação e compartilhamento de informações.  
- Estruturas de dados utilizadas:  
  - **Dicionários** (para armazenar dados em memória).  
  - **Arquivos texto** (para persistência).  

### **2. Conceitos-Chave**  
#### **Dicionários em Python**  
- Armazenam pares **chave-valor**.  
- Exemplo:  
  ```python
  pessoa = {"cpf": "123.456.789-00", "nome": "Ana", "telefone": "99999-9999"}
  ```

#### **Arquivos Texto**  
- Modos de abertura:  
  - `"r"` (leitura), `"w"` (escrita), `"a"` (append).  
- Métodos úteis:  
  - `open()`, `read()`, `write()`, `close()`.  

### **3. Implementação Passo a Passo**  

#### **Passo 1: Criar um Dicionário para Armazenar Pessoas**  
```python
pessoas = {}  # CPF será a chave; valor = {"nome": str, "telefone": str}
```

#### **Passo 2: Função para Ler Dados**  
```python
def ler_dados():
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    return cpf, nome, telefone
```

#### **Passo 3: Função para Cadastrar Pessoa**  
```python
def cadastrar_pessoa():
    cpf, nome, telefone = ler_dados()
    pessoas[cpf] = {"nome": nome, "telefone": telefone}
    print("Pessoa cadastrada com sucesso!")
```

#### **Passo 4: Função para Listar Pessoas**  
```python
def listar_pessoas():
    for cpf, dados in pessoas.items():
        print(f"CPF: {cpf}, Nome: {dados['nome']}, Telefone: {dados['telefone']}")
```

#### **Passo 5: Função para Salvar Dados em Arquivo**  
```python
def salvar_dados():
    with open("pessoas.txt", "w") as arquivo:
        for cpf, dados in pessoas.items():
            linha = f"{cpf},{dados['nome']},{dados['telefone']}\n"
            arquivo.write(linha)
    print("Dados salvos em 'pessoas.txt'!")
```

#### **Passo 6: Função para Carregar Dados do Arquivo**  
```python
def carregar_dados():
    try:
        with open("pessoas.txt", "r") as arquivo:
            for linha in arquivo:
                cpf, nome, telefone = linha.strip().split(",")
                pessoas[cpf] = {"nome": nome, "telefone": telefone}
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo...")
```

### **4. Programa Completo**  

```python
# Dicionário para armazenar pessoas
pessoas = {}

# Funções
def ler_dados():
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    return cpf, nome, telefone

def cadastrar_pessoa():
    cpf, nome, telefone = ler_dados()
    pessoas[cpf] = {"nome": nome, "telefone": telefone}
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    for cpf, dados in pessoas.items():
        print(f"CPF: {cpf}, Nome: {dados['nome']}, Telefone: {dados['telefone']}")

def salvar_dados():
    with open("pessoas.txt", "w") as arquivo:
        for cpf, dados in pessoas.items():
            linha = f"{cpf},{dados['nome']},{dados['telefone']}\n"
            arquivo.write(linha)
    print("Dados salvos em 'pessoas.txt'!")

def carregar_dados():
    try:
        with open("pessoas.txt", "r") as arquivo:
            for linha in arquivo:
                cpf, nome, telefone = linha.strip().split(",")
                pessoas[cpf] = {"nome": nome, "telefone": telefone}
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo...")

# Menu principal
def main():
    carregar_dados()
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Salvar dados")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            salvar_dados()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
```

### **5. Exercícios Propostos**  

1. **Validação de CPF:**  
   Verifique se o CPF tem 11 dígitos numéricos antes de cadastrar.  

2. **Buscar pessoa por CPF:**  
   Implemente uma função que recebe um CPF e retorna os dados da pessoa.  

3. **Editar dados:**  
   Permita que o usuário atualize o nome ou telefone de uma pessoa cadastrada.  

4. **Excluir pessoa:**  
   Adicione uma função para remover uma pessoa do dicionário.  

### **6. Considerações Finais**  
- **Vantagens do código:**  
  - Organizado em funções.  
  - Persistência em arquivo.  
  - Fácil expansão para novas funcionalidades.  
- **Melhorias possíveis:**  
  - Usar **JSON** para armazenamento
  - Adicionar tratamento de erros (ex.: CPF duplicado).  

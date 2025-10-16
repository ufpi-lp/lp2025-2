# Agenda simples

Armazena informações de pessoas em um arquivo .csv

## Instalação de dependências

```bash
pip install rich
pip install readchar
```

## Execução 

```bash
python3 main.py
```
## Observação

O módulo cadastro.py requer uma modificação na classe ```CadastroPessoasService``` para garantir o funcionamento adequado em ambiente Windows.

Problema identificado:
O fragmento filename = "./dados/pessoas.csv" utiliza um caminho hard-coded que pode causar problemas de compatibilidade entre diferentes sistemas operacionais.

Solução sugerida:
Recomenda-se criar uma função que generalize o acesso ao sistema de arquivos, tornando o código independente do sistema operacional. Para isso, podem ser utilizados os módulos os e pathlib do Python.

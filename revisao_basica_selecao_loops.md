# Estruturas de Controle em Python
## Laboratório de Programação - 2025.2

## **Slide 1: Introdução**
**Título:** Estruturas de Seleção e Repetição em Python
**Conteúdo:**
- Revisão de conceitos básicos
- Sintaxe e peculiaridades do Python
- Exemplos práticos

## **Slide 2: Estruturas de Seleção (if)**
**Sintaxe Básica:**
```python
if condição:
    # código se verdadeiro
else:
    # código se falso
```

**Características:**
- Blocos definidos por indentação (não usa {})
- Condições devem retornar True ou False
- Uso do `elif` para múltiplas condições

## **Slide 3: Exemplo - Estrutura if**
```python
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

**Exemplo com múltiplas condições:**
```python
nota = 85
if nota >= 90:
    print("Aprovado com A")
elif nota >= 80:
    print("Aprovado com B")
elif nota >= 70:
    print("Aprovado com C")
else:
    print("Reprovado")
```

## **Slide 4: Estruturas de Repetição - for**
**Sintaxe:**
```python
for elemento in sequencia:
    # código a executar
```

**Peculiaridades:**
- Itera sobre sequências (listas, strings, ranges)
- Não precisa de variável de controle explícita
- Uso da função `range()`

## **Slide 5: Exemplos - Loop for**
**Contagem simples:**
```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

**Com passo personalizado:**
```python
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

**Iteração com índices:**
```python
numeros = [10, 20, 30]
for indice, valor in enumerate(numeros):
    print(f"Índice: {indice}, Valor: {valor}")
```

## **Slide 6: Estruturas de Repetição - while**
**Sintaxe:**
```python
while condição:
    # código enquanto verdadeiro
```

**Controle de fluxo:**
- `break`: interrompe o loop
- `continue`: pula para próxima iteração

## **Slide 7: Exemplo - Loop while**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Com break e continue:**
```python
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # pula o 5
    if i == 8:
        break     # para no 8
    print(i)
```

## **Slide 8: Exemplo Integrado**
**Soma de números pares:**
```python
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    if numero % 2 == 0:  # verifica se é par
        soma += numero

print(f"Soma dos pares: {soma}")
```

## **Slide 9: Exercício Prático 1**
**Verificação de número:**
```python
numero = int(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")
```

## **Slide 10: Exercício Prático 2**
**Tabela de multiplicação:**
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:2}", end=" ")
    print()
```

**Saída:**
```
 1  2  3  4  5  6  7  8  9 10
 2  4  6  8 10 12 14 16 18 20
...
```

## **Slide 11: Exercício Prático 3**
**Número primo:**
```python
numero = int(input("Digite um número: "))
eh_primo = True

for i in range(2, int(numero/2) + 1):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo and numero > 1:
    print("É primo")
else:
    print("Não é primo")
```

## **Slide 12: Exercício Prático 4**
**Jogo de adivinhação:**
```python
import random
numero_aleatorio = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe (1-100): "))
    if palpite > numero_aleatorio:
        print("Muito alto!")
    elif palpite < numero_aleatorio:
        print("Muito baixo!")
    else:
        print("Acertou!")
        break
```

## **Slide 13: Peculiaridades do Python**
**Compreensão de listas:**
```python
# Equivalente a for x in range(10)
lista = [x for x in range(10)]

# Apenas números pares
pares = [x for x in range(10) if x % 2 == 0]
```

**Iteração em dicionários:**
```python
dados = {"nome": "João", "idade": 25}
for chave, valor in dados.items():
    print(f"{chave}: {valor}")
```

## **Slide 14: Dicas Importantes**
1. **Indentação:** Use 4 espaços consistentemente
2. **Condições:** Não use parênteses desnecessários
3. **Loops:** Prefira `for` quando possível
4. **Legibilidade:** Python valoriza código claro e legível

## Slide 15: Exercícios
**Para praticar:**

Resolta os exercícios disponíveis em https://github.com/armandossrecife/lp2024-2/blob/main/exercicios1.ipynb

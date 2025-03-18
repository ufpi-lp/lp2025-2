## **Estruturas de Seleção e Repetição em Python**

### **Estruturas de Seleção (if)**

Em Python, as estruturas de seleção, como o comando `if`, funcionam de maneira semelhante ao C, mas com uma sintaxe mais simples e sem a necessidade de chaves `{}`. O bloco de código é definido por indentação.

**Sintaxe básica:**
```python
if condição:
    # Código a ser executado se a condição for verdadeira
else:
    # Código a ser executado se a condição for falsa
```

**Exemplo:**
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

**Características:**
1. **Condição:**  
   Deve ser uma expressão que resulte em um valor booleano (`True` ou `False`).

2. **Blocos de código:**  
   Delimitados por indentação (espaços ou tabulações).

3. **elif:**  
   Equivalente ao `else if` em C, usado para adicionar mais condições.

4. **else:**  
   Executado se nenhuma das condições anteriores for verdadeira.

**Exemplo com `elif`:**
```python
nota = 85
if nota >= 90:
    print("Aprovado com A.")
elif nota >= 80:
    print("Aprovado com B.")
elif nota >= 70:
    print("Aprovado com C.")
else:
    print("Reprovado.")
```

---

### **Estruturas de Repetição (Loops)**

Python oferece estruturas de repetição poderosas e flexíveis, como `for` e `while`. Diferentemente de C, Python não usa chaves `{}` para delimitar blocos de código, mas sim indentação.

#### **1. for**

O loop `for` em Python é usado para iterar sobre uma sequência de valores (listas, strings, ranges, etc.). Ele é mais versátil que o `for` em C, pois não depende de uma variável de controle explícita.

**Sintaxe:**
```python
for elemento in sequencia:
    # Código a ser executado em cada iteração
```

**Exemplo:**
```python
for i in range(5):
    print(i)
```

**Exemplo com lista:**
```python
numeros = [10, 20, 30, 40, 50]
for numero in numeros:
    print(numero)
```

**Peculiaridades do `for` em Python:**
1. **Iteração sobre sequências:**  
   O `for` em Python pode iterar diretamente sobre listas, strings, tuplas, dicionários, etc.

2. **Função `range`:**  
   A função `range` é comumente usada para gerar sequências numéricas. Ela pode receber até três argumentos: `start`, `stop` e `step`.

   Exemplo:
   ```python
   for i in range(1, 10, 2):  # De 1 a 9, pulando de 2 em 2
       print(i)
   ```

3. **Iteração com índices:**  
   Para acessar tanto o índice quanto o valor de uma lista, use a função `enumerate`.

   Exemplo:
   ```python
   numeros = [10, 20, 30]
   for indice, valor in enumerate(numeros):
       print(f"Índice: {indice}, Valor: {valor}")
   ```

---

#### **2. while**

O loop `while` em Python funciona de maneira semelhante ao C, executando um bloco de código enquanto uma condição for verdadeira.

**Sintaxe:**
```python
while condição:
    # Código a ser executado enquanto a condição for verdadeira
```

**Exemplo:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Características:**
1. **Condição:**  
   Deve ser uma expressão que resulte em um valor booleano (`True` ou `False`).

2. **Iteração:**  
   O loop continua até que a condição se torne falsa.

3. **break:**  
   Interrompe o loop imediatamente.

4. **continue:**  
   Pula para a próxima iteração do loop.

**Exemplo com `break` e `continue`:**
```python
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # Pula a iteração quando i == 5
    if i == 8:
        break  # Interrompe o loop quando i == 8
    print(i)
```

---

### **Exemplo Completo em Python**

Aqui está um exemplo que combina estruturas de seleção e repetição para somar os números pares de uma lista:

```python
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos números pares é: {soma}")
```

**Explicação:**
1. A lista `numeros` contém os valores `[1, 2, 3, 4, 5]`.
2. O loop `for` percorre cada elemento da lista.
3. A estrutura `if` verifica se o número é par (`numero % 2 == 0`).
4. Se for par, o número é adicionado à variável `soma`.
5. No final, o programa imprime a soma dos números pares.

---

### **Peculiaridades dos Loops em Python**

1. **Iteração sobre coleções:**  
   Python permite iterar diretamente sobre listas, strings, dicionários, etc., sem a necessidade de índices explícitos.

   Exemplo com dicionário:
   ```python
   dados = {"nome": "João", "idade": 25}
   for chave, valor in dados.items():
       print(f"{chave}: {valor}")
   ```

2. **Compreensão de listas:**  
   Python oferece uma sintaxe concisa para criar listas com base em loops.

   Exemplo1:
   ```python
   for x in range(10):
       print(x)
   ```
    Cria uma lista de inteiros com os 10 elementos
   ```python
   lista_10_inteiros = [x for x in range(10)]
   print(lista_10_inteiros) # Saida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

   Exemplo2:
   ```python
   pares = [x for x in range(10) if x % 2 == 0]
   print(pares)  # Saída: [0, 2, 4, 6, 8]
   ```

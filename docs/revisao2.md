# Revisão 2 sobre **listas**, **tuplas** e **sets** em Python

---

### **Exercício 1: Soma dos Elementos de uma Lista**
**Código em Python:**
```python
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    soma += numero

print(f"A soma dos elementos da lista é: {soma}")
```

**Explicação:**
- O programa cria uma lista de números.
- Um loop `for` percorre cada elemento da lista e acumula a soma na variável `soma`.
- No final, o programa imprime a soma dos elementos.

---

### **Exercício 2: Remover Duplicatas de uma Lista Usando Set**
**Código em Python:**
```python
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicatas = list(set(lista_com_duplicatas))

print(f"Lista original: {lista_com_duplicatas}")
print(f"Lista sem duplicatas: {lista_sem_duplicatas}")
```

**Explicação:**
- O programa converte a lista em um `set`, que automaticamente remove duplicatas.
- Depois, converte o `set` de volta para uma lista.
- O resultado é uma lista sem elementos repetidos.

---

### **Exercício 3: União de Dois Sets**
**Código em Python:**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

uniao = set1 | set2  # Ou set1.union(set2)

print(f"União dos sets: {uniao}")
```

**Explicação:**
- O programa realiza a união de dois sets usando o operador `|` ou o método `union()`.
- O resultado é um novo set contendo todos os elementos de ambos os sets, sem duplicatas.

---

### **Exercício 4: Interseção de Dois Sets**
**Código em Python:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersecao = set1 & set2  # Ou set1.intersection(set2)

print(f"Interseção dos sets: {intersecao}")
```

**Explicação:**
- O programa encontra os elementos comuns entre dois sets usando o operador `&` ou o método `intersection()`.
- O resultado é um novo set contendo apenas os elementos presentes em ambos os sets.

---

### **Exercício 5: Diferença Entre Dois Sets**
**Código em Python:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

diferenca = set1 - set2  # Ou set1.difference(set2)

print(f"Diferença entre set1 e set2: {diferenca}")
```

**Explicação:**
- O programa calcula a diferença entre dois sets usando o operador `-` ou o método `difference()`.
- O resultado é um novo set contendo os elementos que estão no primeiro set, mas não no segundo.

---

### **Exercício 6: Verificar se uma Tupla Contém um Elemento**
**Código em Python:**
```python
tupla = (10, 20, 30, 40, 50)
elemento = 30

if elemento in tupla:
    print(f"O elemento {elemento} está na tupla.")
else:
    print(f"O elemento {elemento} não está na tupla.")
```

**Explicação:**
- O programa verifica se um elemento específico está presente em uma tupla usando o operador `in`.
- Dependendo do resultado, imprime uma mensagem correspondente.

---

### **Exercício 7: Contar Ocorrências de um Elemento em uma Lista**
**Código em Python:**
```python
lista = [1, 2, 2, 3, 4, 2, 5]
elemento = 2

contagem = lista.count(elemento)

print(f"O elemento {elemento} aparece {contagem} vezes na lista.")
```

**Explicação:**
- O programa usa o método `count()` para contar quantas vezes um elemento aparece na lista.
- O resultado é exibido ao usuário.

---

### **Exercício 8: Desempacotamento de Tupla**
**Código em Python:**
```python
coordenadas = (10, 20, 30)
x, y, z = coordenadas

print(f"Coordenadas: x = {x}, y = {y}, z = {z}")
```

**Explicação:**
- O programa desempacota os elementos de uma tupla em variáveis individuais.
- Cada variável recebe um valor correspondente da tupla.

---

### **Exercício 9: Adicionar Elementos a um Set**
**Código em Python:**
```python
meu_set = {1, 2, 3}

meu_set.add(4)
meu_set.add(2)  # Não será adicionado, pois já existe

print(f"Set após adicionar elementos: {meu_set}")
```

**Explicação:**
- O programa adiciona elementos a um set usando o método `add()`.
- Como sets não permitem duplicatas, o elemento `2` não será adicionado novamente.

---

### **Exercício 10: Remover Elementos de um Set**
**Código em Python:**
```python
meu_set = {1, 2, 3, 4, 5}

meu_set.remove(3)  # Remove o elemento 3
meu_set.discard(10)  # Não faz nada, pois 10 não existe

print(f"Set após remover elementos: {meu_set}")
```

**Explicação:**
- O programa remove elementos de um set usando os métodos `remove()` e `discard()`.
- `remove()` gera um erro se o elemento não existir, enquanto `discard()` não faz nada.

---

### **Exercício 11: Ordenar uma Lista**
**Código em Python:**
```python
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()

print(f"Lista ordenada: {numeros}")
```

**Explicação:**
- O programa ordena uma lista em ordem crescente usando o método `sort()`.
- A lista original é modificada.

---

### **Exercício 12: Criar uma Tupla a Partir de uma Lista**
**Código em Python:**
```python
lista = [10, 20, 30, 40]
tupla = tuple(lista)

print(f"Tupla criada a partir da lista: {tupla}")
```

**Explicação:**
- O programa converte uma lista em uma tupla usando a função `tuple()`.
- A tupla resultante é imutável.

---

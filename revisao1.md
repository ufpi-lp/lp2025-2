## **Revisão 1: Tipos, Variáveis, Operadores, Comandos Condicionais (if), Loops (for, while)**

### **Exercício 1: Verificação de Número Positivo, Negativo ou Zero**

**Código em Python:**
```python
numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
```

**Explicação:**
- O programa solicita ao usuário um número.
- Usa uma estrutura `if-elif-else` para verificar se o número é positivo, negativo ou zero.
- Dependendo do valor, imprime a mensagem correspondente.

---

### **Exercício 2: Contagem de 1 a 10**

**Código em Python:**
```python
for i in range(1, 11):
    print(i, end=" ")
print()
```

**Explicação:**
- O loop `for` é usado para iterar de 1 a 10.
- A cada iteração, o valor de `i` é impresso.
- O `end=" "` evita a quebra de linha após cada número.
- No final, uma nova linha é impressa para melhorar a formatação.

---

### **Exercício 3: Soma de Números**

**Código em Python:**
```python
soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números é: {soma}")
```

**Explicação:**
- O programa usa um loop `while True` para continuar solicitando números até que o usuário digite 0.
- A variável `soma` acumula o valor de todos os números digitados.
- Quando o usuário digita 0, o loop é interrompido com `break`, e a soma é exibida.

---

### **Exercício 4: Tabela de Multiplicação**

**Código em Python:**
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:2}", end=" ")
    print()
```

**Explicação:**
- Dois loops `for` aninhados são usados para gerar a tabela de multiplicação.
- O loop externo (`i`) controla as linhas, e o loop interno (`j`) controla as colunas.
- `f"{i * j:2}"` formata os números com dois dígitos.

---

### **Exercício 5: Verificação de Número Primo**

**Código em Python:**
```python
numero = int(input("Digite um número: "))
eh_primo = True

for i in range(2, int(numero / 2) + 1):
    if numero % i == 0:
        eh_primo = False
        break

if eh_primo and numero > 1:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
```

**Explicação:**
- O programa verifica se o número é divisível por algum valor entre 2 e `numero / 2`.
- Se for divisível, `eh_primo` é definido como `False`.
- No final, o programa imprime se o número é primo ou não.

---

### **Exercício 6: Adivinhe o Número**

**Código em Python:**
```python
import random

numero_aleatorio = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    if palpite > numero_aleatorio:
        print("Muito alto!")
    elif palpite < numero_aleatorio:
        print("Muito baixo!")
    else:
        print("Parabéns! Você acertou o número!")
        break
```

**Explicação:**
- O programa gera um número aleatório entre 1 e 100 usando `random.randint()`.
- O loop `while True` continua pedindo palpites até que o usuário acerte o número.
- Dicas são fornecidas se o palpite for muito alto ou muito baixo.

---

### **Exercício 7: Fatorial de um Número**

**Código em Python:**
```python
numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")
```

**Explicação:**
- O programa calcula o fatorial de um número usando um loop `for`.
- A variável `fatorial` acumula o produto dos números de 1 até `numero`.
---

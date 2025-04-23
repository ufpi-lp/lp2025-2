Aqui está a versão do seu conteúdo formatada para **ASCII** e **UTF-8**, sincronizada com Python:

---

### **Tabela ASCII e Formatação UTF-8 em Python**  
*(Conversão do original em C para Python)*  

---

## **O que é a Tabela ASCII?**  
A Tabela ASCII (*American Standard Code for Information Interchange*) é um padrão que define a representação numérica de caracteres (letras, números, símbolos e controles). Cada caractere é associado a um número entre **0 e 127**.  

### **Características em Python**:  
- **Caracteres 0–31**: Controle (não imprimíveis).  
- **Caracteres 32–126**: Imprimíveis (espaço, letras, números, símbolos).  
- **Caractere 127**: Delete (não imprimível).  

### **Exemplos em Python**:  
```python
print(chr(65))   # Saída: 'A'  
print(chr(97))   # Saída: 'a'  
print(chr(48))   # Saída: '0'  
print(chr(32))   # Saída: ' ' (espaço)  
```

---

## **Usando ASCII em Python**  
Python permite manipular ASCII diretamente com as funções `chr()` (inteiro → caractere) e `ord()` (caractere → inteiro).  

### **Exemplo 1: Exibindo caracteres a partir de valores ASCII**  
```python
print(f"ASCII 65: {chr(65)}")  # Saída: A  
print(f"ASCII 97: {chr(97)}")  # Saída: a  
```

### **Exemplo 2: Convertendo caracteres para valores ASCII**  
```python
letra = 'B'  
print(f"Valor ASCII de 'B': {ord(letra)}")  # Saída: 66  
```

### **Exemplo 3: Usando ASCII em operações**  
```python
letra = 'A'  
nova_letra = chr(ord(letra) + 1)  # Incrementa o valor ASCII  
print(f"Nova letra: {nova_letra}")  # Saída: B  
```

---

## **O que é UTF-8?**  
UTF-8 é um padrão Unicode que usa **1 a 4 bytes** por caractere. É compatível com ASCII (os primeiros 128 caracteres são idênticos).  

### **Características em Python**:  
- **Compatível com ASCII**: `'A'` usa 1 byte (como em ASCII).  
- **Suporte a caracteres especiais**: `'é'`, `'☺'`, `'字'` usam múltiplos bytes.  
- **Padrão no Python 3**: Todas as strings são UTF-8 por padrão.  

### **Exemplo 1: Exibindo caracteres UTF-8**  
```python
print("Caractere UTF-8: ☺")  # Emoji  
print("Caractere UTF-8: é")  # Acento  
```

### **Exemplo 2: Manipulando strings UTF-8**  
Python trata strings UTF-8 nativamente:  
```python
texto = "Olá, mundo! ☺"  
print(f"String UTF-8: {texto}")  
print(f"Número de caracteres: {len(texto)}")  # 13 (contagem de caracteres, não bytes)  
```

### **Exemplo 3: Codificação/Decodificação UTF-8**  
```python
# String para bytes UTF-8  
bytes_utf8 = texto.encode('utf-8')  
print(f"Bytes UTF-8: {bytes_utf8}")  # b'Ol\xc3\xa1, mundo! \xe2\x98\xba'  

# Bytes de volta para string  
string_original = bytes_utf8.decode('utf-8')  
print(f"String original: {string_original}")  
```

---

## **Diferenças entre ASCII e UTF-8 em Python**  
| Característica       | ASCII                | UTF-8                     |  
|----------------------|----------------------|---------------------------|  
| **Tamanho**          | 1 byte/caractere     | 1 a 4 bytes/caractere     |  
| **Suporte**          | Apenas inglês básico | Todos os idiomas/emojis   |  
| **Uso em Python**    | `chr()`, `ord()`     | Strings padrão (`str`)     |  

---

## **Exemplo Completo em Python**  
```python
# ASCII  
print(f"ASCII 65: {chr(65)}")  # A  
print(f"ASCII 97: {chr(97)}")  # a  

# UTF-8  
texto = "Olá, mundo! ☺"  
print(f"UTF-8: {texto}")  
print(f"Valor Unicode de 'é': {ord('é')}")  # 233  

# Contagem de caracteres vs bytes  
print(f"Caracteres: {len(texto)}")  # 13  
print(f"Bytes: {len(texto.encode('utf-8'))}")  # 17 (pois 'á' e '☺' usam múltiplos bytes)  
```

---

## **Exercícios Práticos**  
1. **Conversão ASCII**: Peça um número ao usuário e exiba o caractere ASCII correspondente.  
   ```python
   numero = int(input("Digite um valor ASCII (0-127): "))  
   print(f"Caractere: {chr(numero)}")  
   ```  

2. **Emojis com UTF-8**: Exiba uma lista de emojis.  
   ```python
   emojis = "😀 😍 🐍 🌍"  
   print(f"Emojis: {emojis}")  
   ```  

3. **Contagem de caracteres UTF-8**: Crie um programa que conte caracteres (não bytes) em uma string.  
   ```python
   texto = input("Digite um texto com acentos/emojis: ")  
   print(f"Caracteres: {len(texto)}")  
   ```

---

### **Resumo para Python**  
- **ASCII**: Use `chr()` e `ord()` para caracteres básicos.  
- **UTF-8**: Strings em Python 3 já são UTF-8 (suportam acentos, emojis, etc.).  
- **Bytes vs Strings**: Use `.encode('utf-8')` para converter strings em bytes e `.decode('utf-8')` para o inverso.  

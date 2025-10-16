# Modelo de camadas para criação de software

```mermaid
sequenceDiagram
    participant U as Usuário
    participant UI as Camada UI
    participant N as Camada Negócios
    participant A as Camada Armazenamento

    title Fluxo no Modelo de 3 Camadas

    U->>UI: 1. Faz requisição
    UI->>N: 2. Encaminha dados
    N->>N: 3. Aplica regras de negócio
    N->>A: 4. Solicita dados
    A->>A: 5. Consulta/Atualiza storage
    A->>N: 6. Retorna dados
    N->>N: 7. Processa e formata
    N->>UI: 8. Envia resposta
    UI->>U: 9. Apresenta resultado
```

## **Explicação das Camadas:**

### **1. Camada de Apresentação (UI)**
- **Função:** Interface com o usuário
- **Componentes:** Telas, formulários, componentes visuais
- **Responsabilidades:**
  - Capturar entrada do usuário
  - Apresentar dados formatados
  - Validações de interface

### **2. Camada de Negócios**
- **Função:** Coração da aplicação
- **Componentes:** Serviços, Controladores, Regras
- **Responsabilidades:**
  - Aplicar regras de negócio
  - Processar e transformar dados
  - Orquestrar operações
  - Validações de negócio

### **3. Camada de Armazenamento**
- **Função:** Persistência de dados
- **Componentes:** Repositórios, DAOs, APIs
- **Responsabilidades:**
  - CRUD (Create, Read, Update, Delete)
  - Acesso a arquivos ou bancos de dados
  - Integração com serviços externos

## **Vantagens do Modelo:**
- ✅ **Separação de responsabilidades**
- ✅ **Manutenibilidade**
- ✅ **Testabilidade**
- ✅ **Reutilização de código**
- ✅ **Escalabilidade**

O diagrama mostra o fluxo unidirecional de dados, onde cada camada só se comunica com a camada adjacente, mantendo o princípio de baixo acoplamento.

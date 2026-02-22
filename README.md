# 💰 Sistema de Controle de Caixa com Python

Este projeto é uma solução robusta e leve para o controle de fluxos
financeiros (entradas e saídas). Desenvolvido em Python, ele utiliza o
SQLite3 para persistência de dados local, focando em uma arquitetura
organizada e aplicação de boas práticas de Programação Orientada a
Objetos (POO).

O objetivo principal é oferecer um sistema onde o saldo seja gerenciado
de forma prática, garantindo a integridade dos dados e a persistência
automática em um banco de dados local.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   **Gestão Automática de Banco de Dados:** O sistema cria
    automaticamente a pasta `database/` e o arquivo `.db` ao ser
    iniciado.\
-   **Persistência de Dados:** Todas as movimentações de saldo são
    salvas em tempo real no SQLite.\
-   **Caixa Padrão:** Garantia de existência de um registro inicial
    (`NT_GELADOS`) para evitar erros de referência.\
-   **Validação de Transações:** Regras de negócio que impedem a entrada
    de valores inválidos (negativos ou nulos).\
-   **Flexibilidade de Saldo:** Suporte a saldo negativo (permite
    controle de débitos).

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.x\
-   **Banco de Dados:** SQLite3 (nativo do Python)\
-   **Manipulação de Arquivos:** pathlib (para gestão de diretórios de
    forma cross-platform)\
-   **Paradigma:** Programação Orientada a Objetos (POO)

------------------------------------------------------------------------

## 🗂️ Estrutura do Projeto

    ├── database/            # Pasta criada automaticamente contendo o SQLite (.db)
    ├── models/              # Definição das classes de domínio (Ex: Caixa)
    ├── database/            # Lógica de conexão e persistência (Ex: Classe Banco)
    ├── Interface/           # Camada de interação com o usuário (CLI/GUI)
    ├── main.py              # Ponto de entrada da aplicação
    └── requirements.txt     # Dependências do projeto

------------------------------------------------------------------------

## 🧱 Arquitetura e Classes

### 1. Camada de Persistência (Classe Banco)

Responsável por toda a "conversa" com o SQLite.

-   `create_table()` → Cria a tabela `gelados` caso ela não exista.\
-   `garantir_caixa()` → Verifica se o caixa inicial está cadastrado;
    caso contrário, realiza o insert inicial.\
-   `atualizar_caixa()` → Sincroniza o estado do objeto `Caixa` da
    memória com o banco de dados.

### 2. Camada de Domínio (Classe Caixa)

Contém a lógica de negócio e as regras do saldo.

-   `entrada(valor)` → Adiciona fundos ao saldo após validação.\
-   `saida(valor)` → Subtrai fundos do saldo.\
-   `valida_valor(valor)` → Método interno que garante que nenhum valor
    menor ou igual a zero seja processado.

------------------------------------------------------------------------

## 🔧 Como Instalar e Rodar

### 1️⃣ Clone o repositório:

``` bash
git clone https://github.com/TAKKiN7/Sistema-de-caixa-com-Python.git
cd Sistema-de-caixa-com-Python
```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado):

``` bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências:

``` bash
pip install -r requirements.txt
```

### 4️⃣ Execute a aplicação:

``` bash
python main.py
```

------------------------------------------------------------------------

## ⚠️ Regras de Negócio

### 🔐 Segurança de Dados

O sistema utiliza o gerenciador de contexto:

``` python
with sqlite3.connect(...):
```

Garantindo que o banco de dados seja fechado corretamente mesmo em caso
de erro.

### 📏 Validação Rígida

``` python
if valor <= 0:
    raise ValueError("O valor de movimentação deve ser maior que ZERO.")
```

### 💾 Persistência

O saldo é persistido no banco de dados toda vez que uma operação de
entrada ou saída é finalizada com sucesso.

------------------------------------------------------------------------

## 📝 Licença

Este projeto está sob a licença MIT.

------------------------------------------------------------------------

Desenvolvido com foco em estudo de Backend e Engenharia de Software.

# 💰 Sistema de Controle de Caixa com SQLite

Projeto desenvolvido em **Python** utilizando **SQLite** para controle simples de saldo (entrada e saída), aplicando conceitos de:

- Programação Orientada a Objetos (POO)
- Persistência de dados
- Organização em camadas
- Regras de negócio
- Manipulação de arquivos com `pathlib`

---

## 📌 Objetivo do Projeto

Criar um sistema simples de controle de caixa que:

- Cria automaticamente o banco de dados
- Garante a existência de um caixa padrão
- Permite entrada e saída de valores
- Persiste o saldo no banco SQLite

Projeto focado em prática de backend e organização de código.

---

## 🗂 Estrutura Atual do Projeto



---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- sqlite3 (biblioteca padrão)
- pathlib
- Programação Orientada a Objetos

---

## 🧱 Estrutura do Banco de Dados

Tabela criada automaticamente:

```sql
CREATE TABLE IF NOT EXISTS gelados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    saldo REAL
); 
```


Ao iniciar a classe Banco, o sistema:

- Cria a pasta `database` se não existir
- Cria o arquivo `database.db`
- Cria a tabela `gelados`


Insere automaticamente um registro padrão:

nome: NT_GELADOS

saldo: 0


🏗 Arquitetura Atual
🔹 Classe Banco

Responsável pela camada de persistência.

Principais responsabilidades:

- Criar diretório e arquivo do banco
- Criar tabela
- Garantir existência do caixaa
-Buscar dados do caixa
-Atualizar saldo
-Principais métodos:

Método	Função
create_table()	Cria a tabela se não existir
garantir_caixa()	Garante que exista um caixa inicial
obter_caixa()	Retorna objeto Caixa
atualizar_caixa()	Atualiza saldo no banco
🔹 Classe Caixa

Representa o caixa em memória (camada de domínio).

Atributos:

id

nome

saldo

Métodos:

Método	Descrição
entrada(valor)	Adiciona valor ao saldo
saida(valor)	Subtrai valor do saldo (permite negativo)
valida_valor(valor)	Garante valor maior que zero

Regra de validação:

```python
if valor <= 0:
    raise ValueError("Valor de entrada deve ser maior que ZERO")
```

🚀 Exemplo de Uso
from banco import Banco

banco = Banco()

caixa = banco.obter_caixa()

caixa.entrada(150)
banco.atualizar_caixa(caixa)

print(caixa.saldo)

🔄 Fluxo de Funcionamento
Instancia Banco
      ↓
Cria pasta database
      ↓
Cria arquivo database.db
      ↓
Cria tabela gelados
      ↓
Garante caixa padrão
      ↓
Sistema pronto para uso

⚠ Regras de Negócio

Não é permitido entrada ou saída com valor menor ou igual a zero.

O saldo pode ficar negativo (controle de débito permitido).

Todas as conexões utilizam with sqlite3.connect() garantindo fechamento automático.



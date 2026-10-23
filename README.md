# Sistema de Gerenciamento Bancário (MVC)

Sistema bancário completo desenvolvido em Python utilizando a arquitetura **MVC (Model-View-Controller)** e interface gráfica web moderna com **Streamlit**.

---

## 🏛️ Arquitetura do Sistema (MVC)

### 1. Model (`model/`)
Contém a modelagem de dados e as regras de negócio essenciais:
- [`Cliente.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/model/Cliente.py): Representa o cliente titular da conta (Nome, CPF e validações).
- [`Conta.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/model/Conta.py): Representa a conta bancária vinculada ao cliente (Número, Saldo, operações e formatação).
- [`BancoDados.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/model/BancoDados.py): Simulação de banco de dados em memória utilizando uma Lista/Array para armazenar as contas criadas e gerar números sequenciais únicos.

### 2. View (`view/`)
Responsável pelas interfaces com o usuário, métodos de entrada e exibição:
- [`Display.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/view/Display.py): Front-end interativo em Streamlit que implementa o formulário de entrada para **Nome**, **CPF** e **Saldo Inicial**, além de cards estilizados para exibir os dados da conta.
- [`Conta_view.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/view/Conta_view.py): Métodos de formatação e exibição dos dados da conta (`imprimir_dados_conta`, `formatar_dados_conta`).
- [`Cliente_view.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/view/Cliente_view.py): Métodos de leitura e formatação dos dados de cliente.

### 3. Controller (`controller/`)
Intermedeia o fluxo entre a View e o Model:
- [`Conta_controller.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/controller/Conta_controller.py): 
  1. Recebe os dados da View (`Nome`, `CPF`, `Saldo Inicial`).
  2. Instancia o `Cliente`.
  3. Instancia a `Conta`.
  4. Salva a conta na lista do `BancoDados` ("Model").
  5. Comanda a View para exibir a conta criada de forma formatada.
- [`Cliente_controller.py`](file:///C:/Users/lucas/PycharmProjects/mvc-architecture/controller/Cliente_controller.py): Validações e formatações de regras de negócio de clientes.

---

## 🚀 Como Executar

### 1. Ativar o Ambiente Virtual e Instalar Dependências
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Executar o Front-end Web (Streamlit)
Você pode executar diretamente via:
```powershell
streamlit run view/Display.py
```
ou
```powershell
streamlit run app.py
```

### 3. Executar os Testes Automatizados
```powershell
python -m unittest tests/test_banco.py
```

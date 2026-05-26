# 🧪 Testes E2E com Selenium - Sauce Demo

Este projeto implementa testes automatizados E2E (End-to-End) utilizando **Selenium WebDriver + Pytest**, aplicados ao sistema público de demonstração **Sauce Demo**.

O objetivo do trabalho é validar fluxos reais de interação do usuário em uma aplicação web, aplicando boas práticas de automação de testes para a disciplina de **Testes e Qualidade de Software / Automação E2E com Selenium**.

---

## 🌐 Sistema Testado

* **Nome:** Sauce Demo  
* **URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)  
* **Descrição:** Aplicação de demonstração para cenários de e-commerce (login, listagem de produtos, carrinho de compras e checkout).

---

## 🎯 Objetivo do Projeto

* Implementar testes E2E reais (focados no fluxo completo e não testes unitários).
* Simular ações fiéis de um usuário no navegador.
* Validar comportamentos de interface e regras de negócio da aplicação.
* Aplicar boas práticas de automação com Selenium.
* Utilizar o padrão de arquitetura **Page Object Model (POM)**.


## 📁 Estrutura do Projeto

Abaixo está a disposição dos diretórios organizando as páginas e os scripts de teste:


## 📁 Estrutura do Projeto

```text
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   └── test_login.py
└── conftest.py
```

---

## 🧪 Cenários de Teste

### ✅ Implementados & Automatizados

| # | Cenário |
|---|---------|
| 1 | Login com credenciais válidas e validação de redirecionamento |
| 2 | Login com credenciais inválidas |
| 3 | Adição de produtos ao carrinho |
| 4 | Validação de itens no carrinho |
| 5 | Fluxo de checkout completo (preenchimento e finalização) |
| 6 | Remoção de itens do carrinho |

---

## 🚀 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/kauesalazarcardoso/Testes-E2E.git
cd Testes-E2E
```


### 2. Criar e ativar ambiente virtual (opcional)

```bash
# Criar
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os testes

```bash
pytest
```

---

## 🧠 Padrões e Boas Práticas

| Prática | Descrição |
|--------|-----------|
| **Page Object Model (POM)** | Separa a lógica das páginas da execução dos testes |
| **Fixtures com Pytest** | Gerenciamento eficiente do ciclo de vida do WebDriver |
| **Separação de Camadas** | Isolamento entre scripts de teste e elementos da página |
| **Estratégia de Seletores** | Uso de ID, CSS Selector e Class Name |
| **WebDriver Manager** | Gerenciamento automático do driver do navegador |
| **Sincronização Avançada** | Esperas implícitas/explícitas para evitar flakiness |

---

## ⚠️ Observações

- **Ambiente de Testes:** O Sauce Demo é público e voltado exclusivamente para demonstração.
- **Integridade:** Nenhum dado real é alterado ou persistido de forma prejudicial.
- **Simulação Real:** Os testes reproduzem fielmente as ações de um usuário real no browser.

---

## 🎥 Vídeo Explicativo

Assista à apresentação do projeto e à demonstração dos testes em execução:

👉 [Assistir ao vídeo no YouTube](#)

---

## 👨‍💻 Autor

Desenvolvido por **Kauê Salazar Cardoso**  
Disciplina: *Testes e Qualidade de Software — Automação E2E com Selenium*

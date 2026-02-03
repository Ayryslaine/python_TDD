# 🧪 Python e TDD — Explorando Testes Unitários

Este repositório contém os códigos e testes desenvolvidos durante o curso **Python e TDD: explorando testes unitários**, da **Alura**.  
O foco do projeto é aplicar boas práticas de **testes automatizados**, **Test-Driven Development (TDD)** e garantir a **qualidade e confiabilidade do código em Python**.

---

## 📁 Conteúdo do projeto

O repositório está organizado da seguinte forma:

- **codigo/** → código fonte da aplicação  
- **tests/** → testes unitários desenvolvidos com **Pytest**  
- **main.py** → arquivo principal do projeto  
- **pytest.ini** → configurações do Pytest  
- **requirements.txt** → dependências do projeto  
- **.gitignore** → arquivos e pastas ignorados pelo Git

---

## 📂 Estrutura do projeto

  ```bash
  python_TDD/
├── codigo/
│   └── bytebank.py
├── tests/
│   └── test_bytebank.py
├── main.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
   ```

---

## 🧠 O que aprendi neste curso

Durante o curso, desenvolvi conhecimentos práticos sobre:

- Criação dos **primeiros testes unitários com Python**
- Utilização do **Pytest**, principal framework de testes da linguagem
- Compreensão e aplicação de **Test-Driven Development (TDD)**
- Escrita de testes que lidam com **erros e exceções**
- Uso de **markers** para organizar e otimizar a execução dos testes
- Análise de **cobertura de testes** para avaliar a qualidade do código

---

## 🚀 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Ayryslaine/python_TDD.git
  ```

### 2. Acesse a pasta do projeto:

   ```bash
   cd python_TDD
   ```

### 3. (Opcional) Crie e ative um ambiente virtual

   ```bash
   python -m venv venv
   Windows - venv\Scripts\activate
   Linux / macOS - source venv/bin/activate
   ```

### 4. Instale as dependências

  ```bash
  pip install -r requirements.txt
   ```
---

## 🧪 Executando os testes

### Rodar todos os testes:

  ```bash
  pytest
   ```

### Rodar os testes com cobertura:

  ```bash
 pytest --cov=codigo
   ```

### Gerar relatório de cobertura em HTML:

  ```bash
  pytest --cov=codigo --cov-report=html
   ```

---

## 📚 Curso

* **Plataforma:** Alura
* **Curso:** Python para Dados: trabalhando com funções, estruturas de dados e exceções

---

## ✨ Autora

Desenvolvido por **Ayryslaine Kelle** 💙

---

Se este repositório te ajudou de alguma forma, ⭐ fique à vontade para deixar uma estrela!

# notakeout-api

API em Flask desenvolvida como parte do MVP da disciplina de Desenvolvimento Full-Stack básico da pós-graduação em Desenvolvimento Full Stack administrada pela PUC-Rio.

Este sistema tem como objetivo permitir o cadastro de alimentos e receitas, servindo como base para um gerenciador de refeições completo.

--- 

## Tecnologias Usadas

- **Python 3.11**
- **Flask** – framework web para criação da API
- **SQLite** – banco de dados leve e fácil de usar
- **UV** – gerenciador moderno para ambientes virtuais e dependências

---

## Estrutura do Projeto

notakeout-api/
│
├── .venv/                 # Ambiente virtual (não é enviado ao GitHub)
├── app.py                 # Arquivo principal da aplicação Flask
├── requirements.txt       # Lista de dependências do projeto
├── README.md              # Documentação do projeto (você está aqui!)
│
├── models/                # Modelos de dados (ex: Alimento, Receita)
└── routes/                # Arquivos com as rotas da API (ex: /alimentos, /receitas)

---

## Como rodar o projeto

1. Clone este repositório:

git clone https://github.com/seu-usuario/notakeout-api.git


2. Acesse a pasta do projeto:

cd notakeout-api

3. Crie e Ative o ambiente virtual com UV:

uv venv
.venv\Scripts\Activate

4. Instale as dependências:

uv pip install -r requirements.txt

5. Inicie o servidor:

python app.py

6. Acesse no navegador:

http://127.0.0.1:5000/

---

## Status do projeto

🟢 Em desenvolvimento – estrutura inicial criada e funcionando.  
🔜 Próximas etapas: criação das rotas, banco de dados e integração com front-end.

---

## Autoria

Desenvolvido por **Joanita Santiago** como parte do desafio final da disciplina de Desenvolvimento Full Stack Básico – Pós-graduação PUC-Rio Digital.
# notakeout-api

API em Flask desenvolvida como parte do MVP da disciplina de Desenvolvimento Full-Stack básico da pós-graduação em Desenvolvimento Full Stack administrada pela PUC-Rio.

Este sistema tem como objetivo permitir o cadastro de alimentos e receitas, servir como base para criação de menus personalizados e gerar listas de compras em PDF.

--- 

## Tecnologias Usadas

- **Python 3.11**
- **Flask** – framework web para criação da API
- **Flask SQLAlchemy** – ORM para banco de dados
- **SQLite** – banco de dados leve e local
- **Flasgger** – geração automática de documentação Swagger
- **ReportLab** – geração de arquivos PDF (lista de compras)
- **UV** – gerenciador de pacotes python

---

## Estrutura do Projeto

```
notakeout-api/
│
├── app.py                 # Arquivo principal da aplicação
├── requirements.txt       # Lista de dependências do projeto
├── README.md              # Documentação do projeto
│
├── models/                # Modelos de dados com SQLAlchemy
├── routes/                # Rotas organizadas por blueprint
├── schemas/               # Serialização para resposta JSON
└── services/              # Lógica de negócio (lista de compras, PDF)
```

---

### Como rodar o projeto usando UV

[UV](https://github.com/astral-sh/uv) é um gerenciador de pacotes rápido e moderno para Python, desenvolvido pela equipe do `astral.sh`. 
Ele é compatível com `pip`, porém muito mais veloz na instalação de dependências. É uma ótima alternativa ao `pip` e `venv`, especialmente para projetos que querem um ambiente leve e rápido de configurar.


> Este projeto oferece suporte ao UV para facilitar a instalação de ambientes e pacotes sem depender de uma instalação manual do Python na sua máquina.  
> ⚠️ Com o UV, você **não precisa ter o Python instalado previamente**. Ele baixa automaticamente uma versão leve e isolada do Python apenas para este projeto.  
> Isso evita conflitos de versões do Python e dependências entre diferentes projetos no seu sistema.


1. Instale o UV, se ainda não tiver:
   
```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```
   
3. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/notakeout-api.git
cd notakeout-api
```

3. Crie e ative o ambiente virtual:
   
```bash
uv venv
.venv\Scripts\activate no Windows
```

3. Instale as dependências:
   
```bash
uv pip install -r requirements.txt
```

5. Rode o projeto:
   
```bash
uv run app.py
```
   
6. Acesse no navegador:
   
```
http://127.0.0.1:5000/
  
```

---

## Como rodar o projeto usando venv + pip

Caso não deseje usar o UV, será necessário instalar o python antes de começar, portanto, certifique-se de ter o **Python 3.11** instalado:

- Baixe aqui: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- No Windows: durante a instalação, marque a opção **"Add Python to PATH"**


1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/notakeout-api.git
cd notakeout-api
```

2. Crie o ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

 - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Rode o projeto:
   
```bash
python app.py
```

7. Acesse no navegador:

```
http://127.0.0.1:5000/
  
```

---

## Endpoints principais

### Alimentos `/foods`
- `GET /foods`
- `POST /foods`
- `GET /foods/{id}`
- `PUT /foods/{id}`
- `DELETE /foods/{id}`

### Receitas `/recipes`
- `POST /recipes`
- `GET /recipes`
- `GET /recipes/{id}`
- `PUT /recipes/{id}`

### Menus `/menus`
- `POST /menus`
- `GET /menus`
- `GET /menus/{id}`
- `DELETE /menus/{id}`

### Menus - Lista de Compras
- `GET /menus/{id}/shopping-list` – retorna a lista em JSON
- `GET /menus/{id}/pdf` – gera e baixa a lista em PDF

---

## Documentação Swagger

Disponível em:

```
http://127.0.0.1:5000/apidocs/
```

---

## Autoria

Desenvolvido por **Joanita Santiago** como parte do desafio final da disciplina de Desenvolvimento Full Stack Básico – Pós-graduação PUC-Rio Digital.

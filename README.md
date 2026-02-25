# Finanças API

## Descrição
API REST criada por Bruno David para gerenciar finanças pessoais. Possui autenticação com JWT, banco de dados SQLite e as operações completas de CRUD. Cada registro tem id, valor, descrição, categoria e data, sendo separado entre receitas e despesas.

## Tecnologias usadas
- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Bcrypt (passlib)

## Como instalar e rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/BrunoDavid16/financias-api.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a API:
```bash
python -m uvicorn main:app --reload
```

4. Acesse a documentação em:
```
http://127.0.0.1:8000/docs
```

## Rotas

### Finanças
- **GET** `/receitas` — lista todas as receitas
- **POST** `/receitas` — cria uma receita
- **GET** `/despesas` — lista todas as despesas
- **POST** `/despesas` — cria uma despesa
- **GET** `/relatorio` — retorna total de receitas, despesas e saldo

### Autenticação
- **POST** `/register` — cria um novo usuário
- **POST** `/login` — autentica o usuário e retorna o token JWT
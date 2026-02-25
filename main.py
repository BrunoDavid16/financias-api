from database import SessionLocal, engine
from fastapi import FastAPI
from auth import hash_senha, verificar_senha, criar_token
from models import Receita, ReceitaModel, Despesa, DespesaModel, Usuario, UsuarioModel

app = FastAPI()

@app.post("/register")
def registrar(usuario: Usuario):
    db = SessionLocal()
    db_usuario = UsuarioModel(email=usuario.email, senha_hash=hash_senha(usuario.senha))
    db.add(db_usuario)
    db.commit()
    db.close()
    return usuario

@app.post("/login")
def login(usuario: Usuario):
    db = SessionLocal()
    db_usuario = db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first()
    if not verificar_senha(usuario.senha, db_usuario.senha_hash):
        return {"erro": "Senha incorreta"}
    token = criar_token({"sub": usuario.email})
    return {"access_token": token}


@app.get("/receitas")
def get_receitas():
    db = SessionLocal()
    receita = db.query(ReceitaModel).all()
    db.close()
    return receita

@app.post("/receitas")
def post_receitas(receita: Receita):
    db = SessionLocal()
    db_receita = ReceitaModel(valor=receita.valor, descricao=receita.descricao, categoria=receita.categoria, data=receita.data)
    db.add(db_receita)
    db.commit()
    db.close()
    return receita


@app.get("/despesas")
def get_despesas():
    db = SessionLocal()
    despesa = db.query(DespesaModel).all()
    db.close()
    return despesa

@app.post("/despesas")
def post_despesas(despesa: Despesa):
    db = SessionLocal()
    db_despesa = DespesaModel(valor=despesa.valor, descricao=despesa.descricao, categoria=despesa.categoria, data=despesa.data)
    db.add(db_despesa)
    db.commit()
    db.close()
    return despesa

@app.get("/relatorio")
def get_relatorio():
    db = SessionLocal()
    receitas = db.query(ReceitaModel).all()
    total_rec = sum(receita.valor for receita in receitas)
    despesas = db.query(DespesaModel).all()
    total_dep = sum(despesa.valor for despesa in despesas)
    saldo = total_rec- total_dep
    relatorio = {
        "total_rec": total_rec,
        "total_dep": total_dep,
        "saldo": saldo,
    }
    return relatorio

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
from database import Base, engine, get_db
from schemas import TarefaCreate, TarefaResponse, TarefaUpdate

Base.metadata.create_all(bind=engine)  # cria as tabelas ao iniciar

app = FastAPI(title="API de Tarefas — Parte 3 (SQLite)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/tarefas", response_model=list[TarefaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_tarefas(db)


@app.get("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def buscar(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.buscar_tarefa(db, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return tarefa


@app.post("/tarefas", response_model=TarefaResponse, status_code=201)
def criar(dados: TarefaCreate, db: Session = Depends(get_db)):
    return crud.criar_tarefa(db, dados)


@app.put("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def substituir(tarefa_id: int, dados: TarefaCreate,
               db: Session = Depends(get_db)):
    tarefa = crud.substituir_tarefa(db, tarefa_id, dados)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return tarefa


@app.patch("/tarefas/{tarefa_id}", response_model=TarefaResponse)
def atualizar(tarefa_id: int, dados: TarefaUpdate,
              db: Session = Depends(get_db)):
    tarefa = crud.atualizar_tarefa(db, tarefa_id, dados)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return tarefa


@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int, db: Session = Depends(get_db)):
    print(tarefa_id)
    crud.deletar_tarefa(db, tarefa_id)

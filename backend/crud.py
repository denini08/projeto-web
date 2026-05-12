from sqlalchemy.orm import Session
from models import Tarefa
from schemas import TarefaCreate, TarefaUpdate


def listar_tarefas(db: Session):
    return db.query(Tarefa).all()


def buscar_tarefa(db: Session, tarefa_id: int):
    return db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()


def criar_tarefa(db: Session, dados: TarefaCreate):
    tarefa = Tarefa(**dados.model_dump())
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)
    return tarefa


def atualizar_tarefa(db: Session, tarefa_id: int, dados: TarefaUpdate):
    tarefa = buscar_tarefa(db, tarefa_id)
    if not tarefa:
        return None
    atualizacoes = dados.model_dump(exclude_unset=True)
    for campo, valor in atualizacoes.items():
        # tarefa.campo = valor
        setattr(tarefa, campo, valor)
    db.commit()
    db.refresh(tarefa)
    return tarefa


def substituir_tarefa(db: Session, tarefa_id: int, dados: TarefaCreate):
    tarefa = buscar_tarefa(db, tarefa_id)
    if not tarefa:
        return None
    tarefa.titulo    = dados.titulo
    tarefa.descricao = dados.descricao
    tarefa.concluida = False
    db.commit()
    db.refresh(tarefa)
    return tarefa


def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = buscar_tarefa(db, tarefa_id)
    if tarefa:
        db.delete(tarefa)
        db.commit()
    else:
        print(f"Tarefa {tarefa_id} nao encontrada para deletar.")
    return tarefa

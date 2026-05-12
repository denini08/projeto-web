from typing import Optional
from pydantic import BaseModel, ConfigDict

class TarefaCreate(BaseModel):
    titulo:    str
    descricao: str = "desc"

class TarefaUpdate(BaseModel):
    titulo:    Optional[str]  = None
    descricao: Optional[str]  = None
    concluida: Optional[bool] = None

class TarefaResponse(BaseModel):
    id:        int
    titulo:    str
    descricao: str
    concluida: bool

    model_config = ConfigDict(from_attributes=True)

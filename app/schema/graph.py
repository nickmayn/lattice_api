from pydantic import BaseModel
from uuid import UUID
from typing import List

class Graph(BaseModel):
    id: UUID
    name: str
    group: List[str]
    
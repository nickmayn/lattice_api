from pydantic import BaseModel, Extra
from uuid import UUID
from typing import List

class Node(BaseModel, extra=Extra.allow):
    id: UUID
    graph_id: List[UUID]

    



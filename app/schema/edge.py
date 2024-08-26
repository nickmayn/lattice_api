from pydantic import BaseModel, Extra
from uuid import UUID
from typing import List

class Edge(BaseModel, extra=Extra.allow):
    id: UUID
    graph_ids: List[UUID]
    node_a_id: UUID
    node_b_id: UUID
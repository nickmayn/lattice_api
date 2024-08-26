from pydantic import BaseModel, Extra
from uuid import UUID

class Edge(BaseModel, extra=Extra.allow):
    id: UUID
    node_a_id: UUID
    node_b_id: UUID
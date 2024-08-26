from pydantic import BaseModel, Extra
from uuid import UUID

class Node(BaseModel, extra=Extra.allow):
    id: UUID

    



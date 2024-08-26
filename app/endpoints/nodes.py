from fastapi.routing import APIRouter
from fastapi import status

from app.schema.node import Node
from app.crud.create import create_node
from app.crud.read import read_nodes
from app.crud.update import update_node
from app.crud.delete import delete_node

from typing import List, Optional

router = APIRouter()

@router.post('/create')
async def create(node: Node):
    create_node(node)

@router.get('/{node_ids}')
async def read(node_ids: Optional[List[str]] | None):
    nodes = read_nodes(node_ids)
    nodes = nodes.apply(lambda r: r.json())
    return nodes

@router.post('/update/{node_id}')
async def update(node_id: str, node: Node):
    update_node()

@router.post('/delete/{node_id}')
async def delete():
    delete_node()
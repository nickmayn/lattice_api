from fastapi.routing import APIRouter

from app.schema.node import Node
from app.crud.create import create_node
from app.crud.read import read_node
from app.crud.update import update_node
from app.crud.delete import delete_node

router = APIRouter()

@router.post('/create')
async def create(node: Node):
    create_node(node)

@router.get('/')
async def read():
    read_node()

@router.post('/update/{}')
async def update():
    update_node()

@router.post('/delete/{}')
async def delete():
    delete_node()
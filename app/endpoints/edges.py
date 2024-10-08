from fastapi.routing import APIRouter

from app.schema.graph import Graph
from app.crud.create import create_edge
from app.crud.read import read_edge
from app.crud.update import update_edge
from app.crud.delete import delete_edge

router = APIRouter()

@router.post('/create')
async def create(graph: Graph):
    create_edge(graph)

@router.get('/')
async def read():
    read_edge()

@router.post('/update/{}')
async def update():
    update_edge()

@router.post('/delete/{}')
async def delete():
    delete_edge()
from fastapi.routing import APIRouter

from app.schema.edge import Graph
from app.crud.create import create_graph
from app.crud.read import read_graphs
from app.crud.update import update_graph
from app.crud.delete import delete_graph

router = APIRouter()

@router.post('/create')
async def create(edge: Edge):
    create_edge(edge)

@router.get('/')
async def read():
    read_edge()

@router.post('/update/{}')
async def update():
    update_edge()

@router.post('/delete/{}')
async def delete():
    delete_edge()
from fastapi import APIRouter

from app.endpoints import nodes, edges, graph

api_router = APIRouter()

api_router.include_router(nodes.router, prefix='/nodes', tags=['nodes'])
api_router.include_router(edges.router, prefix='/edges', tags=['edges'])
api_router.include_router(graph.router, prefix='/graph', tags=['graph'])
from app.schema.node import Node
from app.schema.edge import Edge
from app.schema.graph import Graph
from typing import List, Optional

def read_nodes(node_ids: Optional[List[str]]) -> List[Node]:
    """
    The purpose of this method is to provide a way to read nodes from the database.

    :param node_ids: an optional list of node ids to search for. If none are passed then return all nodes.
    
    :return: All relevant nodes.
    """
    return

def read_edges(edge_ids: Optional[List[str]]) -> List[Edge]:
    """
    The purpose of this method is to provide a way to read edges from the database.

    :param edge_ids: an optional list of edge ids to search for. If none are passed then return all edges.

    :return: All relevant edges
    """
    return

def read_graphs(graph_ids: List[str]) -> List[Graph]:
    """
    The purpose of this method is to provide a way to read graphs from the database.

    :param graph_ids: an optional list of graph ids to search for. If none are passed then return all graphs.

    :return: all relevant graphs.
    """
    return
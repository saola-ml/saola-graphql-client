# Generated by ariadne-codegen
# Source: graphql

from typing import List

from .base_model import BaseModel
from .fragments import Connection


class GetActiveConnections(BaseModel):
    connections: List["GetActiveConnectionsConnections"]


class GetActiveConnectionsConnections(Connection):
    pass

# Generated by ariadne-codegen
# Source: graphql

from typing import List

from .base_model import BaseModel
from .fragments import Chat


class GetChatsByStatus(BaseModel):
    chats: List["GetChatsByStatusChats"]


class GetChatsByStatusChats(Chat):
    pass
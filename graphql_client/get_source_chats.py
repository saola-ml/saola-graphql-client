# Generated by ariadne-codegen
# Source: graphql

from typing import List

from .base_model import BaseModel
from .fragments import Chat


class GetSourceChats(BaseModel):
    chats: List["GetSourceChatsChats"]


class GetSourceChatsChats(Chat):
    pass
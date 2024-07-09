# Generated by ariadne-codegen
# Source: graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    chat_statuses_enum,
    crm_record_types_enum,
    source_types_enum,
    statuses_enum,
    workspace_roles_enum,
)


class OAuthApp(BaseModel):
    id: Any
    name: Optional[str]
    client_id: str
    created_at: Any
    updated_at: Any
    callback_url: Optional[str]


class Source(BaseModel):
    id: Any
    name: Optional[str]
    type: source_types_enum
    user_id: Optional[Any]
    workspace_id: Any
    config: Any
    created_at: Any
    updated_at: Any
    oauth_app: Optional["SourceOauthApp"]


class SourceOauthApp(OAuthApp):
    pass


class CrmRecord(BaseModel):
    id: Any
    source_id: Any
    chat_id: Any
    type: crm_record_types_enum
    attributes: Any
    updated_at: Any
    created_at: Any


class Workspace(BaseModel):
    id: Any
    name: str
    user_id: Optional[Any]
    created_at: Any
    updated_at: Any
    user_workspaces: List["WorkspaceUserWorkspaces"]


class WorkspaceUserWorkspaces(BaseModel):
    id: Any
    role: workspace_roles_enum
    user_id: Any
    updated_at: Any
    created_at: Any
    workspace_id: Any


class Chat(BaseModel):
    id: Any
    created_at: Any
    updated_at: Any
    workspace_id: Any
    platform_id: str
    channel_id: str
    contact_id: str
    messages: Any
    status: chat_statuses_enum
    last_message_at: Optional[Any]
    source: "ChatSource"
    workspace: "ChatWorkspace"
    crm_records: List["ChatCrmRecords"]


class ChatSource(Source):
    pass


class ChatWorkspace(Workspace):
    pass


class ChatCrmRecords(CrmRecord):
    pass


class Connection(BaseModel):
    id: Any
    state: Any
    created_at: Any
    source_id: Any
    destination_id: Any
    workspace_id: Any
    active: bool
    status: statuses_enum
    state: Any
    source: "ConnectionSource"


class ConnectionSource(Source):
    pass


class User(BaseModel):
    id: Any
    display_name: str = Field(alias="displayName")
    email: Optional[Any]
    user_workspaces: List["UserUserWorkspaces"]


class UserUserWorkspaces(BaseModel):
    workspace: "UserUserWorkspacesWorkspace"


class UserUserWorkspacesWorkspace(Workspace):
    pass


OAuthApp.model_rebuild()
Source.model_rebuild()
CrmRecord.model_rebuild()
Workspace.model_rebuild()
Chat.model_rebuild()
Connection.model_rebuild()
User.model_rebuild()

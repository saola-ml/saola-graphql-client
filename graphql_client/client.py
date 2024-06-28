# Generated by ariadne-codegen
# Source: graphql

from typing import Any, Dict

from .async_base_client import AsyncBaseClient
from .enums import chat_statuses_enum
from .get_active_connections import GetActiveConnections
from .get_chat import GetChat
from .get_chat_crm_records import GetChatCrmRecords
from .get_chats_by_status import GetChatsByStatus
from .get_connection import GetConnection
from .get_crm_record import GetCrmRecord
from .get_source import GetSource
from .get_source_chats import GetSourceChats
from .get_workspace import GetWorkspace
from .get_workspace_connections import GetWorkspaceConnections
from .get_workspace_sources import GetWorkspaceSources
from .get_workspaces import GetWorkspaces


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def get_chat(self, id: Any, **kwargs: Any) -> GetChat:
        query = gql(
            """
            query GetChat($id: uuid!) {
              chats_by_pk(id: $id) {
                ...Chat
              }
            }

            fragment Chat on chats {
              id
              created_at
              updated_at
              workspace_id
              platform_id
              channel_id
              contact_id
              messages
              status
              last_message_at
              source {
                ...Source
              }
              workspace {
                ...Workspace
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetChat", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetChat.model_validate(data)

    async def get_chats_by_status(
        self, status: chat_statuses_enum, **kwargs: Any
    ) -> GetChatsByStatus:
        query = gql(
            """
            query GetChatsByStatus($status: chat_statuses_enum!) {
              chats(where: {status: {_eq: $status}}) {
                ...Chat
              }
            }

            fragment Chat on chats {
              id
              created_at
              updated_at
              workspace_id
              platform_id
              channel_id
              contact_id
              messages
              status
              last_message_at
              source {
                ...Source
              }
              workspace {
                ...Workspace
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {"status": status}
        response = await self.execute(
            query=query,
            operation_name="GetChatsByStatus",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return GetChatsByStatus.model_validate(data)

    async def get_source_chats(self, source_id: Any, **kwargs: Any) -> GetSourceChats:
        query = gql(
            """
            query GetSourceChats($sourceId: uuid!) {
              chats(where: {source_id: {_eq: $sourceId}}) {
                ...Chat
              }
            }

            fragment Chat on chats {
              id
              created_at
              updated_at
              workspace_id
              platform_id
              channel_id
              contact_id
              messages
              status
              last_message_at
              source {
                ...Source
              }
              workspace {
                ...Workspace
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {"sourceId": source_id}
        response = await self.execute(
            query=query, operation_name="GetSourceChats", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetSourceChats.model_validate(data)

    async def get_active_connections(self, **kwargs: Any) -> GetActiveConnections:
        query = gql(
            """
            query GetActiveConnections {
              connections(where: {active: {_eq: true}}) {
                ...Connection
              }
            }

            fragment Connection on connections {
              id
              state
              created_at
              source_id
              destination_id
              workspace_id
              active
              status
              state
              source {
                ...Source
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query,
            operation_name="GetActiveConnections",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return GetActiveConnections.model_validate(data)

    async def get_workspace_connections(
        self, workspace_id: Any, **kwargs: Any
    ) -> GetWorkspaceConnections:
        query = gql(
            """
            query GetWorkspaceConnections($workspace_id: uuid!) {
              connections(where: {workspace_id: {_eq: $workspace_id}, active: {_eq: true}}) {
                ...Connection
              }
            }

            fragment Connection on connections {
              id
              state
              created_at
              source_id
              destination_id
              workspace_id
              active
              status
              state
              source {
                ...Source
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }
            """
        )
        variables: Dict[str, object] = {"workspace_id": workspace_id}
        response = await self.execute(
            query=query,
            operation_name="GetWorkspaceConnections",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return GetWorkspaceConnections.model_validate(data)

    async def get_connection(self, id: Any, **kwargs: Any) -> GetConnection:
        query = gql(
            """
            query GetConnection($id: uuid!) {
              connections_by_pk(id: $id) {
                ...Connection
              }
            }

            fragment Connection on connections {
              id
              state
              created_at
              source_id
              destination_id
              workspace_id
              active
              status
              state
              source {
                ...Source
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetConnection", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetConnection.model_validate(data)

    async def get_chat_crm_records(
        self, chat_id: Any, **kwargs: Any
    ) -> GetChatCrmRecords:
        query = gql(
            """
            query GetChatCrmRecords($chat_id: uuid!) {
              crm_records(where: {chat_id: {_eq: $chat_id}}) {
                ...CrmRecord
              }
            }

            fragment Chat on chats {
              id
              created_at
              updated_at
              workspace_id
              platform_id
              channel_id
              contact_id
              messages
              status
              last_message_at
              source {
                ...Source
              }
              workspace {
                ...Workspace
              }
            }

            fragment CrmRecord on crm_records {
              id
              source_id
              source {
                ...Source
              }
              chat_id
              chat {
                ...Chat
              }
              type
              attributes
              updated_at
              created_at
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {"chat_id": chat_id}
        response = await self.execute(
            query=query,
            operation_name="GetChatCrmRecords",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return GetChatCrmRecords.model_validate(data)

    async def get_crm_record(self, id: Any, **kwargs: Any) -> GetCrmRecord:
        query = gql(
            """
            query GetCrmRecord($id: uuid!) {
              crm_records_by_pk(id: $id) {
                ...CrmRecord
              }
            }

            fragment Chat on chats {
              id
              created_at
              updated_at
              workspace_id
              platform_id
              channel_id
              contact_id
              messages
              status
              last_message_at
              source {
                ...Source
              }
              workspace {
                ...Workspace
              }
            }

            fragment CrmRecord on crm_records {
              id
              source_id
              source {
                ...Source
              }
              chat_id
              chat {
                ...Chat
              }
              type
              attributes
              updated_at
              created_at
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetCrmRecord", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetCrmRecord.model_validate(data)

    async def get_source(self, id: Any, **kwargs: Any) -> GetSource:
        query = gql(
            """
            query GetSource($id: uuid!) {
              sources_by_pk(id: $id) {
                ...Source
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetSource", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetSource.model_validate(data)

    async def get_workspace_sources(
        self, workspace_id: Any, **kwargs: Any
    ) -> GetWorkspaceSources:
        query = gql(
            """
            query GetWorkspaceSources($workspace_id: uuid!) {
              sources(where: {workspace_id: {_eq: $workspace_id}}) {
                ...Source
              }
            }

            fragment OAuthApp on oauth_apps {
              id
              name
              client_id
              created_at
              updated_at
              callback_url
            }

            fragment Source on sources {
              id
              name
              type
              user_id
              workspace_id
              config
              created_at
              updated_at
              oauth_app {
                ...OAuthApp
              }
            }
            """
        )
        variables: Dict[str, object] = {"workspace_id": workspace_id}
        response = await self.execute(
            query=query,
            operation_name="GetWorkspaceSources",
            variables=variables,
            **kwargs,
        )
        data = self.get_data(response)
        return GetWorkspaceSources.model_validate(data)

    async def get_workspace(self, id: Any, **kwargs: Any) -> GetWorkspace:
        query = gql(
            """
            query GetWorkspace($id: uuid!) {
              workspaces_by_pk(id: $id) {
                ...Workspace
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(
            query=query, operation_name="GetWorkspace", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetWorkspace.model_validate(data)

    async def get_workspaces(self, **kwargs: Any) -> GetWorkspaces:
        query = gql(
            """
            query GetWorkspaces {
              workspaces {
                ...Workspace
              }
            }

            fragment Workspace on workspaces {
              id
              name
              user_id
              created_at
              updated_at
              user_workspaces {
                id
                role
                user_id
                updated_at
                created_at
                workspace_id
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="GetWorkspaces", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetWorkspaces.model_validate(data)
from src.models.repositories.tools_repository import RepositoryTools


class ControllerTools:
    def __init__(self):
        self.repo = RepositoryTools()

    def get_all_tools(self):
        tools = self.repo.list_tools()
        return tools

    def get_tools_for_tags(self, tag: str):
        tools = self.repo.get_tools_for_tags(tag)
        return tools

    def create_tools(self, data: dict):
        return self.repo.create_tools(data)

    def delete_tools(self, id: int):
        return self.repo.delete_tools(id)

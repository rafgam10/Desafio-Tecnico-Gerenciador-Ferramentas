from src.settings.extensions import db
from src.models.tools_model import Tool
from ..interfaces.tools_interface import InterfaceTools


class RepositoryTools(InterfaceTools):
    def list_tools(self) -> list[dict]:
        try:
            array_tools = db.session.query(Tool).all()
            lista = [tool.to_dict() for tool in array_tools]
            return lista

        except Exception as e:
            ...

    def get_tools_for_tags(self, tag: str) -> list[dict]:
        try:
            if not tag:
                raise ValueError('Falta de tag')

            lista_tools = db.session.query(Tool).all()
            lista_tools_with_tags = [
                tool.to_dict()
                for tool in lista_tools
                if tag in tool.get_tags()
            ]
            return lista_tools_with_tags

        except Exception as e:
            ...

    def create_tools(self, data: dict) -> dict:
        try:

            if not data:
                return Exception('Falta de body no repository.')

            new_tool = Tool(data['title'], data['link'], data['description'])
            new_tool.set_tags(data['tags'])
            db.session.add(new_tool)
            db.session.commit()

            return new_tool.to_dict()

        except Exception as e:
            db.session.rollback()
            return str(e)

    def delete_tools(self, id: int) -> dict:
        try:

            obj_tool = db.session.query(Tool).filter(Tool.id == id).first()
            db.session.delete(obj_tool)
            db.session.commit()

            return {}

        except Exception as e:
            db.session.rollback()
            return str(e)

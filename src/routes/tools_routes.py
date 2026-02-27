from flask import Blueprint, jsonify, request
from src.controllers.tools_controller import ControllerTools

tools_bp = Blueprint('Tools', __name__, url_prefix='/tools')
controller = ControllerTools()


@tools_bp.route('', methods=['POST'])
def create_tool():
    """
    Create Tool
    ---
    tags:
      - Tools

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - link
          properties:
            title:
              type: string
              example: Postman
            link:
              type: string
              example: https://postman.com
            description:
              type: string
              example: API testing tool
            tags:
              type: array
              items:
                type: string
              example: ["api", "test"]

    responses:
      201:
        description: Tool created successfully
        schema:
          type: object
      400:
        description: Invalid input
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({'msg': 'Body vazio...'}), 400

        tool = controller.create_tools(data)
        return jsonify(tool), 201

    except Exception as e:
        return jsonify({'Error': str(e)}), 400


@tools_bp.route('', methods=['GET'])
def list_tools():
    """
    List Tools
    ---
    tags:
      - Tools

    parameters:
      - in: query
        name: tag
        type: string
        required: false
        description: Filter tools by tag

    responses:
      200:
        description: List of tools
        schema:
          type: array
          items:
            type: object
      400:
        description: Error
    """
    try:
        tag = request.args.get('tag')

        if tag:
            tools = controller.get_tools_for_tags(tag)
        else:
            tools = controller.get_all_tools()

        return jsonify(tools), 200

    except Exception as e:
        return jsonify({'Error': str(e)}), 400


@tools_bp.route('/<int:id>', methods=['DELETE'])
def delete_tool(id: int):
    """
    Delete Tool
    ---
    tags:
      - Tools

    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: Tool ID

    responses:
      200:
        description: Tool deleted successfully
      404:
        description: Tool not found
      400:
        description: Error
    """
    try:
        tool = controller.delete_tools(id)
        return jsonify(tool), 200

    except Exception as e:
        return jsonify({'Error': str(e)}), 400
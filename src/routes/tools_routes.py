from flask import Blueprint, jsonify, request

from src.controllers.tools_controller import ControllerTools

tools_bp = Blueprint('Tools', __name__, url_prefix='/tools')
controller = ControllerTools()


@tools_bp.route('', methods=['POST'])
def create_tool():
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
    try:
        tag = request.args.get('tag')

        if tag:
            tools = controller.get_tools_for_tags(tag)
        else:
            tools = controller.get_all_tools()

        return jsonify(tools), 200

    except Exception as e:
        return jsonify({'Error': str(e)}), 400


@tools_bp.route('<int:id>', methods=['DELETE'])
def delete_tool(id: int):
    try:
        tool = controller.delete_tools(id)
        return jsonify(tool), 200

    except Exception as e:
        return jsonify({'Error': str(e)}), 400

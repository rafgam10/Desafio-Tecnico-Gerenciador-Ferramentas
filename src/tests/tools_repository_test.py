from src import create_app
from src.settings.extensions import db
from src.models.repositories.tools_repository import RepositoryTools
import pytest
import json


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.mark.skip(reason='Passou')
def test_create_tools():

    app = create_app()

    with app.app_context():

        db.create_all()

        data = {
            'title': 'hotel',
            'link': 'https://github.com/typicode/hotel',
            'description': 'Local app manager. Start apps within your browser, developer tool with local .localhost domain and https out of the box.',
            'tags': [
                'node',
                'organizing',
                'webapps',
                'domain',
                'developer',
                'https',
                'proxy',
            ],
        }

        data2 = {
            'title': 'json-server',
            'link': 'https://github.com/typicode/json-server',
            'description': 'Fake REST API based on a json schema. Useful for mocking and creating APIs for front-end devs to consume in coding challenges.',
            'tags': ['api', 'json', 'schema', 'node', 'github', 'rest'],
        }

        repo = RepositoryTools()
        response = repo.create_tools(data)
        repo.create_tools(data2)
        print()
        print(response)


@pytest.mark.skip(reason='Passou')
def test_list_tools(app):

    repo = RepositoryTools()
    response = repo.list_tools()
    print()
    print(response)


@pytest.mark.skip(reason='Passou')
def test_list_tools_for_tags(app):

    repo = RepositoryTools()
    response = repo.get_tools_for_tags('node')
    print()
    print(response)


def test_delete_tools(app):

    repo = RepositoryTools()
    response = repo.delete_tools(1)
    print(response)

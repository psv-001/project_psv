from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.Category import CategoryResource
from resources.Tables import TableResource

app_name = 'project_psv'
api_bp = Blueprint('api', app_name)
print('api_bp', api_bp)
api = Api(api_bp)

print('api ---', api)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/categories')
api.add_resource(TableResource, '/createtable')

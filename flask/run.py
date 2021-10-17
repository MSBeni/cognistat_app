# from app.views import app
#
#
# if __name__ == 'main':
#     app.run(port=5000, debug=True)


from app import app

from flask_restful import Resource, Api
from app.views import EnvName, Item, AddItem
api = Api(app)
api.add_resource(EnvName, '/')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(AddItem, '/items/Add')


if __name__ == "__main__":
    app.run()
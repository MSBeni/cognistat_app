from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Items = list()


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['Name'] == name, Items), None)
        return item, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['Name'] == name, Items), None):
            return({'message': 'Item {} already exists'.format(name)}, 400)
        itemPrice = request.get_json()
        item = {'Name': name,
                'Price': itemPrice['Price']}
        Items.append(item)
        return {'message': 'Price of Item {} is added successfully'.format(item['Name'])}, 201


class AddItem(Resource):
    def post(self):
        item = request.get_json()
        Items.append(item)
        return {'message': 'Item {} is added successfully'.format(item['Name'])}, 201


api.add_resource(Item, '/items/<string:name>')
api.add_resource(AddItem, '/items/Add')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
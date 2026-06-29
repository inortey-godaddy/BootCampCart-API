from itertools import product

import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseProducts


class Product:
    def on_get(self, req, resp, product_id):
        product = DatabaseProducts.get(id=product_id)
        resp.media = model_to_dict(product)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, product_id):
        DatabaseProducts.delete_by_id(product_id)
        resp.status = falcon.HTTP_204


# Excercise 2:
# Products route should respond to GET and POST requests
# GET products returns a list of every product in the database
# POST products creates a product and returns the data it created


class Products:
    def on_get(self, req, resp):
        products = []
        products_list = DatabaseProducts.select()
        for product in products_list:
            products.append(model_to_dict(product))
        resp.media = products
        resp.status = falcon.HTTP_200
    def on_post(self, req, resp):
        products_data = req.get_media()
        new_product = DatabaseProducts.create(**products_data)
        resp.media = model_to_dict(new_product)
        resp.status = falcon.HTTP_201
    # pass must have a pass line because you cannot have a "blank" class
    # def on_get(self, req, resp):

    # def on_post(self, req, resp):

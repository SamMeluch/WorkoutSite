import falcon
import os
import json

class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [{
                'href': '216.png'
             }]
        }

        resp.body = json.dumps(doc, ensure_ascii=False)

        resp.status = falcon.HTTP_200

api = application = falcon.API()

images = Resource()
api.add_route('/images', images)

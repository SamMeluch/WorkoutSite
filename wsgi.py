import falcon
import os
import json

class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [{
                'href': 'fractals/216.png'
             }]
        }

        print('got inside function')
        resp.body = json.dumps(doc)
        resp.content_type = 'text/json'
        resp.status = falcon.HTTP_200

api = falcon.API()

images = Resource()
api.add_route('/api/img', images)
application = api
#def application(env, start_response):
#   start_response('200 OK', [('Content-Type', 'text/html')]
#   return [b"Hello World"]

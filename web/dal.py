__author__ = 'felix.shaw@tgac.ac.uk - 03/09/15'

import pymongo
from bson import ObjectId

class db:

    con = pymongo.MongoClient('localhost', 27017)['mozfest']['ontology']

    def PUT(self, image_name, isa, has, does):
        self.con.insert({'image_name': image_name, 'is': isa, 'has': has, 'does': does})

    def GET(self, id):
        return self.con.find_one({'_id': ObjectId(id)})

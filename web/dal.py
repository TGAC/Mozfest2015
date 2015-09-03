__author__ = 'felix.shaw@tgac.ac.uk - 03/09/15'

import pymongo


class db:

    con = pymongo.MongoClient('localhost', 27017)['mozfest']['ontology']

    def PUT(self, isa, has, does):
        pass

    def GET(self, id):
        pass
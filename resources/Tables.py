#!/usr/bin/env python3.4
from flask_restful import Resource
from Model import db

class TableResource(Resource):
    def post(self):
        response = dict()
        status = 200

        # Create Table
        try:
            db.create_all()
            response['message'] = 'Table is created'
        except Exception as exp:
            response['message'] = 'Error in Table creation'
            status = 500

        return response, status 

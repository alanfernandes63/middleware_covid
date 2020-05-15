from flask_restplus import Resource, reqparse
import requests
from controller.full_series_state import FullSeriesState

class FullSeries(Resource):
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument("initialDate", type=str,required=True, help="id of alert is required")
        parse.add_argument("lastDate", type=str,required=True, help="id of alert is required")
        parse.add_argument("uf", type=str,required=True, help="id of alert is required")
        fullSeriesState = FullSeriesState()

        args = parse.parse_args()
        return fullSeriesState.loadData(args['initialDate'], args['lastDate'], args['uf'])
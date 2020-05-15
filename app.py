from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from resources.full_series import FullSeries



app = Flask(__name__)

api = Api(app)
cors = CORS(app, resources={r"/api/*":{"origins":"*"}})

api.add_resource(FullSeries, '/api/data/')


if __name__ == '__main__':
    app.run(debug=True)


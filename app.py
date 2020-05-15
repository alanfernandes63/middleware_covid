from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from resources.full_series import FullSeries
import os


app = Flask(__name__)

api = Api(app)
cors = CORS(app, resources={r"/api/*":{"origins":"*"}})

api.add_resource(FullSeries, '/api/data/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=False)


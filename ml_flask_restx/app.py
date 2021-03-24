import pickle
from sklearn.linear_model import LogisticRegression
from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='ML API Example', validate=True)

ns = api.namespace('iris', description='IRIS model')

iris_row = api.model('IrisRow', {
    'sepal_length': fields.Float(required=True),
    'sepal_width': fields.Float(required=True),
    'petal_length': fields.Float(required=True),
    'petal_width': fields.Float(required=True)
})

iris_prediction = api.inherit('IrisPrediction', iris_row, {
    'prediction': fields.List(fields.Float, min_items=3, max_items=3)
})


@ns.route('/')
class IrisClassification(Resource):
    @ns.doc('obtain_prediction')
    @ns.expect(iris_row)
    @ns.marshal_with(iris_prediction, code=200)
    def post(self):
        payload = api.payload
        values_tuple = tuple(payload.values())
        prediction = [round(p, 5) for p in model.predict_proba([values_tuple])[0]]
        payload.update({'prediction': prediction})
        return payload


if __name__ == '__main__':
    app.run(debug=True)
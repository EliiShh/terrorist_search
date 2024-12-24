from flask import Flask
from app.controllers.elastic_controller import elastic_blueprint


app = Flask(__name__)
app.register_blueprint(elastic_blueprint, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from collections import OrderedDict
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('BASE_URL_DATABASE')
app.config['JSON_AS_ASCII'] = False
CORS(app)
db = SQLAlchemy(app)
auth = HTTPBasicAuth()


USER_DATA = {
    "admin": os.getenv('PASS_AUTH')
}

#movies_id movie_title movie_score create_at movie_description movie_type release_date director rating country main_actors movie_genre

class Movies(db.Model):
    __tablename__ = 'movies'
    movies_id:Mapped[int] = mapped_column(primary_key=True)
    movie_title:Mapped[str] = mapped_column(nullable=False)
    movie_score:Mapped[str] = mapped_column(nullable=False)
    movie_description:Mapped[str] = mapped_column(nullable=False)
    movie_type:Mapped[str] = mapped_column(nullable=False)
    movie_genre:Mapped[str] = mapped_column(nullable=False)
    release_date:Mapped[str] = mapped_column(nullable=False)
    director:Mapped[str] = mapped_column(nullable=False)
    rating:Mapped[str] = mapped_column(nullable=False)
    country:Mapped[str] = mapped_column(nullable=False)
    main_actors:Mapped[str] = mapped_column(nullable=False)
    create_at:Mapped[str] = mapped_column(nullable=False)
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/')
def hello_world():
    return make_response(jsonify({"msg": "hello world"}), 200)



# @auth.verify_password
# def verify_password(username, password):
#     if username in USER_DATA and USER_DATA[username] == password:
#         return username
#     return jsonify({"error": "Unauthorized"}), 401



@app.route('/api/v1/movies')
def movies():
    resluts = Movies.query.all()
    data = [reslut.to_dict() for reslut in resluts]
    try:
        if request.headers['X-Api-Key'] == os.getenv('API_KEY'):
            res = {
                "status": True,
                "message": "success",
            }
            res["data"] = data
            return jsonify(res), 200
        else:
            return jsonify({"error": "Unauthorized"}), 401
    except Exception as e:
        return jsonify({"error": "key not found"}), 500


if __name__ == "__main__":
    app.run(port=5001)



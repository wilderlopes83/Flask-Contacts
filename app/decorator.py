from functools import wraps
from flask_restful import request
import jwt
from flask import current_app
from app.models import User

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "authorization" in request.headers:
            token = request.headers["authorization"]
            

        if not token:
            return {"error": "Você não tem permissão para acessar esta rota"}, 401

        print(token)

        if not "Bearer" in token:
            return {"error": "Invalid token"}, 401

        try:
            token_pure = token.replace("Bearer ", "")
            decoded = jwt.decode(token_pure, current_app.config["SECRET_KEY"])
            current_user = User.query.get(decoded["id"])
        except:
            return {"error": "O token é inválido"}, 403

        return f(current_user=current_user, *args, **kwargs)

    return decorated


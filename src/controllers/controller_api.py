from src import app
from flask import request, Response
from ..repositories import log_repository

@app.route('/api/post_informations', methods=['POST'])
def post_informations():
    data = request.get_json()

    log_repository.insert_log(data)

    return Response(status=200)
import os
from utils import format_date
from quart import Blueprint, g, current_app as app, request

api = Blueprint('api', __name__)

def get_db():
    return g.sqlite_db

@api.route('/', methods=['POST'])
async def index():
    if request.content_type == 'application/json':
        data = await request.get_json()
        if data is not None:
            db = get_db()
            db.execute(
                "INSERT INTO posts(latitude,longitude,velocidade,satelites,data_hora) VALUES(?,?,?,?,?);",
                [data['Latitude'], data['Longitude'], data['Velocidade'], data['Satelites'], str(format_date(f"{data['Data']} {data['Hora']}"))],
            )
            db.commit()
    return 'success'
import os
from fastapi import FastAPI, status
from mangum import Mangum
from src.schemas.flatten import FlattenRequest, FlattenResponse
from src.utils import flatten as f

STAGE = os.environ.get('STAGE')
root_path = '/' if not STAGE else f'/{STAGE}'

app = FastAPI(title="Flatten app API", root_path=root_path)


@app.post(
    '/flatten',
    status_code=status.HTTP_200_OK,
    tags=["Flatten"],
    response_model=FlattenResponse
)
def flatten(request: FlattenRequest):
    elements = request.data
    result = list(f(elements))
    return {'results': result}


handler = Mangum(app)

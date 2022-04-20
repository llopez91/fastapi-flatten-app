from typing import List
from pydantic import BaseModel


class FlattenRequest(BaseModel):
    data: List = []


class FlattenResponse(BaseModel):
    results: List = []

from typing import List
from pydantic import BaseModel


class MyBaseModel(BaseModel):
    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))


class TitleList(MyBaseModel):
    titles: List[str]


class PiDec(MyBaseModel):
    # TODO: Define PiDec Pydantic Model for response


class NewsCount(MyBaseModel):
    # TODO: Define NewsCount Pydantic Model for response


class AreaCircle(MyBaseModel):
    # TODO: Define AreaCircle Pydantic Model for response

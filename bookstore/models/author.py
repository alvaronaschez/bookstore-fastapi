from pydantic import HttpUrl
from sqlmodel import SQLModel

from .base import CamelCaseModel, required
from .id import Id


class AuthorBase(CamelCaseModel):
    name: str
    biography: str
    image: HttpUrl


@required([])
class AuthorInPartial(AuthorBase):
    pass


@required(["name"])
class AuthorIn(AuthorBase):
    pass


@required(["id", "name"])
class AuthorOut(AuthorBase):
    id: Id


class AuthorInDb(SQLModel):
    pass

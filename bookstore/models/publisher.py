from pydantic import HttpUrl
from sqlmodel import Field

from .base import CamelCaseModel, required
from .id import Id


class PublisherBase(CamelCaseModel):
    name: str
    website: HttpUrl


@required([])
class PublisherInPartial(PublisherBase):
    pass


@required(["name"])
class PublisherIn(PublisherBase):
    pass


@required(["id", "name"])
class PublisherOut(PublisherBase):
    id: Id


class PublisherInDb(PublisherBase, table=True):
    __tablename__ = "publishers"
    id: int = Field(primary_key=True, ge=1)

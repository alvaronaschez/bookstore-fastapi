from pydantic import HttpUrl, conlist
from sqlalchemy import Column
from sqlmodel import JSON, Field

from .author import AuthorOut
from .base import CamelCaseModel, required
from .id import Id
from .isbn import ISBN, ISBN13
from .price import Price
from .publisher import PublisherOut


class BookBase(CamelCaseModel):
    title: str
    summary: str
    image: HttpUrl
    price: Price = Field(sa_column=Column(JSON))


@required([])
class BookInPartial(BookBase):
    author_ids: conlist(Id, min_items=1, max_items=6, unique_items=True)
    # not working
    # author_ids: list[Id] = Field(min_items=1, max_items=6, unique_items=True)
    publisher: PublisherOut


@required(["isbn", "author_ids", "title", "price"])
class BookIn(BookInPartial):
    isbn: ISBN


@required(["isbn", "authors", "title", "price"])
class BookOut(BookBase):
    isbn: ISBN13
    # not working
    # authors: list[AuthorOut] = Field(min_items=1, max_items=6, unique_items=True)
    authors: conlist(AuthorOut, min_items=1, max_items=6, unique_items=True)


class BookInDb(BookBase, table=True):
    __tablename__ = "books"
    # isbn: ISBN13 = Field(primary_key=True)
    isbn: str = Field(regex="^\\d{13}$", primary_key=True)

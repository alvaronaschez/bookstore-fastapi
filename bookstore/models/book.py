from pydantic import Field, HttpUrl
from sqlmodel import SQLModel

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
    price: Price


@required([])
class BookInPartial(BookBase):
    author_ids: list[Id] = Field(min_items=1, max_items=6, unique_items=True)
    publisher: PublisherOut


@required(["isbn", "author_ids", "title", "price"])
class BookIn(BookInPartial):
    isbn: ISBN


@required(["isbn", "authors", "title", "price"])
class BookOut(BookBase):
    isbn: ISBN13
    authors: list[AuthorOut] = Field(min_items=1, max_items=6, unique_items=True)


class BookInDb(SQLModel):
    pass

from pydantic import BaseModel, Field


class ISBN10(BaseModel):
    __root__: str = Field(regex="^\\d{10}$")


class ISBN13(BaseModel):
    __root__: str = Field(regex="^\\d{13}$")


class ISBN(BaseModel):
    __root__: ISBN10 | ISBN13

from pydantic import BaseModel, Field


class Id(BaseModel):
    __root__: int = Field(ge=1)

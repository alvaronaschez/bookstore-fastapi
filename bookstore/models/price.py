from pydantic import Field

from .base import CamelCaseModel
from .currency import Currency


class Price(CamelCaseModel):
    currency: Currency
    value: int = Field(ge=0)

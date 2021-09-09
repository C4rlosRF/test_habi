
from typing import Optional
from pydantic import BaseModel


class Property(BaseModel):
    address: Optional[str]
    city: Optional[str]
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]

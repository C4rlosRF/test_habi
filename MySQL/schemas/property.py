  
from typing import Optional

from pydantic import BaseModel

from app import models


class Property(models.Property):
    pass

class PropertyRequest(BaseModel):
    year:Optional[str]
    city:Optional[str]
    state:Optional[str]

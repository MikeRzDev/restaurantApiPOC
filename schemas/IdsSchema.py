from pydantic import BaseModel, Field
from typing import Optional, List

class IdsSchema(BaseModel):

    number: int = Field()

from pydantic import BaseModel, Field
from typing import Optional, List

class RestaurantsSchema(BaseModel):

    name: str = Field()

from pydantic import BaseModel, Field
from typing import Optional, List

class MenusSchema(BaseModel):

    name: str = Field()

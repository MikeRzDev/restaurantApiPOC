from pydantic import BaseModel, Field
from typing import Optional, List

class PersonsSchema(BaseModel):

    name1: str = Field()
    name2: str = Field()
    lastName1: str = Field()
    lastName2: str = Field()

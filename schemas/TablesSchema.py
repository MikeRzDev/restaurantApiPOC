from pydantic import BaseModel, Field
from typing import Optional, List

class TablesSchema(BaseModel):

    number: int = Field()

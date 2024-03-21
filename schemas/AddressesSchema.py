from pydantic import BaseModel, Field
from typing import Optional, List

class AddressesSchema(BaseModel):

    address: str = Field()

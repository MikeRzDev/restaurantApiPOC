from pydantic import BaseModel, Field
from typing import Optional, List

class ReservationsSchema(BaseModel):

    number: int = Field()

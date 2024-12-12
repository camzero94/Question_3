from pydantic import BaseModel
from typing import Optional

class GreetRequest(BaseModel):
    name: Optional[str] = None

class GreetResponse(BaseModel):
    message: str

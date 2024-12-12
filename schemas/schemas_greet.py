from pydantic import BaseModel,model_validator 
from typing import Optional

class GreetRequest(BaseModel):
    name: Optional[str] = None

class GreetResponse(BaseModel):
    message: str
    
    @model_validator(mode="before")
    def check_status(cls, values):
        if not values.get('message'): 
            raise ValueError('Invalid response does not contains correct format')
        return values 

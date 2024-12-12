from fastapi import FastAPI, Depends 
from typing import Optional
from schemas.schemas_greet import GreetRequest, GreetResponse
import os
import uvicorn


app = FastAPI()

@app.get('/greet')
async def greet(query_params: GreetRequest = Depends(GreetRequest)) -> GreetResponse:
    """
    Greet a user with a message.
    Validate request query parameters and response body.
    """
    name = query_params.name
    if name is None or name == '':
        return GreetResponse(message='Hello, World!')
    return GreetResponse(message=f'Hello, {name}!')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)


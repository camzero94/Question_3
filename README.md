# Question_3: API
### How to run it
1. Run docker-compose to start the API

If you dont have docker-compose installed:
For Mac OS 
```sh
brew install docker-compose
```

For Linux  OS 
```sh
sudo apt update
sudo apt install docker-compose
```

For Windows OS
```sh
https://docs.docker.com/compose/install/
```

Go inside the Question_3/ folder and run the following:
```sh
docker-compose up --build -d
```
This will build the Dockerfile that wraps the main.py file and will run it in the background.

Your API is ready to some testing
Run the following command to test the API
```sh
curl -X GET "http://localhost:5000/greet"
```
Then run:
```sh
curl -X GET "http://localhost:5000/greet?name=Camilo"
```

![Alt Text](./media/api.gif)

### Description and directory  structure 
```sh
├── Dockerfile
├── README.md
├── __init__.py
├── docker-compose.yaml
├── main.py
├── media
│   └── api.gif
├── requirements.txt
└── schemas
    ├── __init__.py
    ├── __pycache__
    └── schemas_greet.py

4 directories, 9 files
```

### Requirements.txt
```sh
annotated-types==0.7.0
anyio==4.7.0
click==8.1.7
fastapi==0.115.6
h11==0.14.0
idna==3.10
pydantic==2.10.3
pydantic_core==2.27.1
sniffio==1.3.1
starlette==0.41.3
typing_extensions==4.12.2
uvicorn==0.32.1
```

## Some considerations 

For this simple API I decided to use FastAPI and Pydantic to validate the input.
When the API request is made, the input is validated by the Pydantic schema (in this case does not matter because it will only return "Hello World!" if it has a query parameter) and if the response is not valid will return an invalid format message.o

I we hit a wrong endpoint we will get a 404 "Not Found" error.

I choose fast API mainly because we can see the shape of the request and responses and many other utilities in <id host>:<port>/docs

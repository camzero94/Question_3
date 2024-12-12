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
├── README.md
├── docker-compose.yml
├── main.py
├── media
│   └── rabbitmq.gif
├── open_env
│   ├── bin
│   ├── include
│   ├── lib
│   └── pyvenv.cfg
└── requirements.txt

6 directories, 6 files
```
**Setup Rabbitmq**:
- Exchange: is set to default. It means that the routing key will match with the queue name. 
- Queue: The queue is named "test_queue" and it is durable. It means that the queue will survive a broker restart.
- ack: The message is acknowledged by the consumer. It means that the message is removed from the queue when the consumer receives it.
- Channel management: The channel is closed after the message is sent. And each function send_message() and consume_message() creates a new channel. **Multiplexing happens** 

### Requirements.txt
```sh
pika==1.3.2
```

## Some considerations 

When sending the message the connection is close. It is a good practice to close the connection after the message is sent. 

When consuming the message the program hang so the user can decide to exit by pressing Ctrl + C. This is because I want to show the message is consumed only once and the queue is empty.


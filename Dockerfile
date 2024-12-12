FROM python:3.10 

WORKDIR /app

COPY requirements.txt /app
RUN pip install --requirement /app/requirements.txt

COPY . /app

# Expose the port
EXPOSE 5000

# Command to run when the container starts
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]


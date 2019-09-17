# Use official Python3 as parent image
FROM python:3

# Set working directory inside container to /app
WORKDIR /app
COPY . /app

# Install requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]
# Use python container image
FROM python:3.7.2-stretch

RUN mkdir /app

# Copy the current directory into the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install the dependencies
RUN pip install -r requirements.txt

# Start UWSGI
CMD ["uwsgi", "app.ini"]
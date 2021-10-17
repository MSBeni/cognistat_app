# Using python 3 container image
FROM python:3
# Set the working Directiry to the app
#WORKDIR /usr/src/app
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt
# run the command to start uWSGI
CMD [ "uwsgi", "app.ini" ]
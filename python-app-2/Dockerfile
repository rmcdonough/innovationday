# our base image
FROM alpine:3.7

# Install python and pip
RUN apk add --update py2-pip bind-tools curl netcat-openbsd

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY unicorn1.jpg /usr/src/app/
COPY unicorn2.gif /usr/src/app/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]

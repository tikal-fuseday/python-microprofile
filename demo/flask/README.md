# python-microprofile

## flask framework

The module will show an example of how to use the microprofile libraries within a flask context

to build the docker file run:

### build app
* pip install -r requirements.txt


### build docker
docker build -t flask-demo:latest .

 ## run docker
docker run -it --name flask-demo -p 8080:8080 flask-demo:latest
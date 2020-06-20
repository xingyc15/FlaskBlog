# FlaskBlog

---

## Tips

- host='0.0.0.0' : defined in main function. Used for docker port mapping

- port=5000 : defined by flask

- On AWS, these need `sudo` before `docker/docker-compose`

---

## Run In Python

      python run.py

Visit http://$(localhost):5000

---

## Run In Docker

### - Build Image

      docker build --rm --no-cache -t flaskblog:v1.0

- --rm : remove middle images
- --no-cache : build images without cached images
- -t : tags for the image

### - Run Container

      docker run -it --rm -p 5000:5000 -v /home/ubuntu/FlaskBlog:/usr/src/flaskblog flaskblog:v1.0
      #docker run -it --rm -p 5000:5000 -v /Users/yuchenxing/PycharmProjects/FlaskBlog:/usr/src/app/flaskblog flaskblog:v1.0
  
- -i : interactive=True
- -t : support login from terminal
- --rm : remove the container when stoped
- -p : port $(localhost port):$(port in docker)
- -v : volume, change 1 => change both
- -d : in backend

### - Exec Container

Enter the container by shell

    docker exec -it $(container_name) /bin/bash

Visit http://$(aws_server_ip_address):5000 or what you specified in $(localhost port)

---

## Run In Docker Compose

### - Build Image

      docker build --rm --no-cache -t flaskblog:v1.0

### - Launch Services on Containers

      cd $(dir for docker-compose.yaml)
      docker-compose up

### - Stop Services

      docker-compose down // stop and remove container
      docker-compose stop // just stop

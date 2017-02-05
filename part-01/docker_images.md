# Imagens 


* Procurar imagens
```sh 
root@hands-on:/home/vagrant# docker search python
NAME                           DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
python                         Python is an interpreted, interactive, obj...   1592      [OK]       
kaggle/python                  Docker image for Python scripts run on Kaggle   52                   [OK]
google/python                  Please use gcr.io/google-appengine/python ...   34                   [OK]
tsutomu7/alpine-python         Python3.5 and scientific packages on alpine.    4                    [OK]
vimagick/python                mini python                                     3                    [OK]
pandada8/alpine-python         An alpine based python image                    3                    [OK]
beevelop/nodejs-python         Node.js with Python                             2                    [OK]
lucidfrontier45/python-uwsgi   Python with uWSGI                               2                    [OK]
tsuru/python                   Image for the Python platform in tsuru PaaS.    2                    [OK]
lcgc/python                    The base image for applications written in...   1                    [OK]
colstrom/python                Docker on Python, with pip!                     1                    [OK]
orbweb/python                  Python image                                    1                    [OK]
1science/python                Python Docker images based on Alpine Linux      1                    [OK]
allanlei/python                Python Images                                   0                    [OK]
funkygibbon/python             Minimal python based on funkygibbon/ubuntu      0                    [OK]
kirigamico/python              Base Docker image which contains Python, G...   0                    [OK]
croscon/python                 Python image for Croscon                        0                    [OK]
samtayuk/python                Python with bower, less and sass                0                    [OK]
bynd/python                    Debian-based Python image                       0                    [OK]
exostack/python                Automated Exostack Python builds.               0                    [OK]
ceecko/python                  Python image                                    0                    [OK]
hivesolutions/python           Python runtime distribution                     0                    [OK]
1maa/python                    Python images                                   0                    [OK]
dockershelf/python             Repository for docker images of Python. Te...   0                    [OK]
codekoalas/python              Runs python scripts every 5 minutes after ...   0                    [OK]
root@hands-on:/home/vagrant# 
```

* Baixar uma imagem
```sh 
root@hands-on:/home/vagrant# docker pull hello-world 
Using default tag: latest
latest: Pulling from library/hello-world
78445dd45222: Pull complete 
Digest: sha256:c5515758d4c5e1e838e9cd307f6c6a0d620b5e07e6f927b07d05f6d12a1ac8d7
Status: Downloaded newer image for hello-world:latest
root@hands-on:/home/vagrant# 
```

* Listar imagens local
```sh 
root@hands-on:/home/vagrant# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              f49eec89601e        7 days ago          129 MB
hello-world         latest              48b5124b2768        2 weeks ago         1.84 kB
root@hands-on:/home/vagrant# 
```

* Remover uma imagem
```sh 
root@hands-on:/home/vagrant# docker rmi hello-world
Untagged: hello-world:latest
Untagged: hello-world@sha256:c5515758d4c5e1e838e9cd307f6c6a0d620b5e07e6f927b07d05f6d12a1ac8d7
Deleted: sha256:48b5124b2768d2b917edcb640435044a97967015485e812545546cbed5cf0233
Deleted: sha256:98c944e98de8d35097100ff70a31083ec57704be0991a92c51700465e4544d08
root@hands-on:/home/vagrant# 
```

* Criar uma imagem de um container
```sh 
root@hands-on:/home/vagrant# docker run -it --name customizando-imagem ubuntu
root@container_id:/# groupadd web
root@container_id:/# useradd -d /home/caos -m caos
root@container_id:/# exit
exit
root@hands-on:/home/vagrant# docker commit -m "add user" -a "caos@caos.com" container_id caos/ubuntu:v1
sha256:f03258647d272a4d774eb70dd79f094531c626a91b815786d2a9b04cbafea7dc
root@hands-on:/home/vagrant# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
caos/ubuntu         v1                  f03258647d27        12 seconds ago      130 MB
ubuntu              latest              f49eec89601e        9 days ago          129 MB
hello-world         latest              48b5124b2768        2 weeks ago         1.84 kB
root@hands-on:/home/vagrant# 
```

* Criar uma imagem com Dockerfile


```python 
from bottle import route, run

@route('/')
def hello():
    return "Hello Python!\n Chat do caos.\n"

run(host='0.0.0.0', port=8085, debug=True)
```

```bash 
FROM ubuntu
MAINTAINER Chat do CAOS  <chatcaos@gmail.com>

RUN groupadd web
RUN useradd -d /home/caos -m caos

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install python-pip -y
ADD server.py /home/caos/server.py
RUN pip install bottle

EXPOSE 8085
ENTRYPOINT ["/usr/bin/python", "/home/caos/server.py"]
USER caos
```


```bash 
root@hands-on:/home/vagrant# docker build -t caos/python_hello ./hands_on_src/part-01/hello-python/Dockerfile
```
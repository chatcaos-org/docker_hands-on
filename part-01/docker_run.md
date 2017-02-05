# Executando um container ($ docker run ...)

Para executar um container usamos o comando: 
```sh 
$ docker run 
```

Quando executamos:
```sh 
$ docker run hello-world
```

O docker executa os seguintes passos:

- Verifica se existe a imagem localmente.
- Se não existir, ele baixa a imagem.
- Cria e lança o container.

Essa imagem apenas exibe um "Hello from Docker!" e um informativo.

```sh
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
78445dd45222: Pull complete 
Digest: sha256:c5515758d4c5e1e838e9cd307f6c6a0d620b5e07e6f927b07d05f6d12a1ac8d7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

## Principais Opções do (docker run)


| Opção              | Tipo do Argumento | Descrição                                              |
| ------------------ |:-----------------:| :------------------------------------------------------|
| -i, --interactive  | N/A               | Mantém o STDIN aberto                                  |
| -t, --tty          | N/A               | Aloca um pseudo-TTY                                    |
| -p, --publish      | list              | mapea as portas de um container com as do host         |
| -d, --detach       | N/A               | Roda o container em background e exibe o container ID  |
| -e, --env          | list              | Define variaves de ambiente                            |
| -v, --volume       | list              | monta um volume                                        |
| --link             | list              | Cria um link para outro container                      |
| --name             | string            | Define um nome para o container                        |


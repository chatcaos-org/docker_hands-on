# Administrar Containers 

* Parar um container
```sh 
root@hands-on:/home/vagrant# docker stop administrando-container
administrando-container
root@hands-on:/home/vagrant# 
```

* Iniciar um container
```sh 
root@hands-on:/home/vagrant# docker start administrando-container
administrando-container
root@hands-on:/home/vagrant# 
```

* Remover um container
```sh 
root@hands-on:/home/vagrant# docker rm administrando-container
administrando-container
root@hands-on:/home/vagrant# 
```

* Executar comando em um container
```sh 
root@hands-on:/home/vagrant# docker exec administrando-container mkdir /tmp/test-exec
root@hands-on:/home/vagrant# docker exec administrando-container ls /tmp/
test-exec
root@hands-on:/home/vagrant#
```

* Copiar arquivos do host para um container
```sh 
root@hands-on:/home/vagrant# touch teste_copia_de_arquivo.txt
root@hands-on:/home/vagrant# docker cp teste_copia_de_arquivo.txt administrando-container:/tmp/
root@hands-on:/home/vagrant# docker exec administrando-container ls /tmp/
test-exec  
teste_copia_de_arquivo.txt
root@hands-on:/home/vagrant# 
```

* Conectando a um container que está em execução
```sh 
root@hands-on:/home/vagrant# docker attach administrando-container
root@container_id:root@hands-on:/home/vagrant# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.3  18232  1924 ?        Ss   00:39   0:00 /bin/bash
root         9  0.0  0.2  34416  1456 ?        R+   00:40   0:00 ps aux
root@container_id:root@hands-on:/home/vagrant# 
```
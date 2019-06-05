# author angel quingaluisa
# file utilizado para deployar el microservicion en un  contenedor docker

#!/bin/bash
imageName=devops-image:1.0
containerName=devops-container


echo Eliminar contenedores anteriores...
docker rm -f $containerName

echo Correr nuevo contenedor...
docker-compose up -d
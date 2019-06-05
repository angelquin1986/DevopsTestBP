# author angel quingaluisa
# file utilizado para deployar el microservicion en un  contenedor docker

#!/bin/bash
imageName=devops-image:1.0



echo Eliminar contenedores anteriores...
if [  "$(docker ps -q -f name=devops-container1)" ]; then
                docker rm -f devops-container1
fi

if [  "$(docker ps -q -f name=devops-container2)" ]; then
                docker rm -f devops-container2
fi

if [  "$(docker ps -q -f name=devops-container)" ]; then
                docker rm -f devops-container
fi

echo Correr nuevo contenedor...
docker-compose up -d --build
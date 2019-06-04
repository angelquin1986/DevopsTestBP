# Documentación  infraestructura
Se documenta todoos los comandos que se utiliza para  levantar el ambiente devops

## Instalar docker
- sudo apt update
- sudo apt install apt-transport-https ca-certificates curl software-properties-common

## Agregar claves
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

## Agregar docker al repositorio
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update

#validara verionsar docker
apt-cache policy docker-ce

sudo apt install docker-ce

# validar el  estado servicio de docker
sudo systemctl status docker

# instalar jenkins en docker
sudo docker pull jenkins/jenkins

#arrancar jekins
sudo docker run -d -p 8080:8080 -p 50000:50000 jenkins/jenkins
# ver los  contenedores activos
sudo docker ps -a
# dar de baja un contenedor
sudo docker rm dac335d87508
# stop a un contenedor 
sudo docker stop contenedor_id

#jenkins user : admin  pasws_admin
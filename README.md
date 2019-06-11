# DevopsTestBP

## Test Devops
### Autor :Angel Quingaluisa

#### Lenguage Python 3.6
 - django
 - djangorestframework
 - gunicorn
 - Pycharm
![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/py.png)
### Descripción 
   - Aplicación alojada en google cloud, utiliza docker para  crear contenedores de la app y jenkins  para validar cambios en la rama y realizar CI/DI con pipeline   encargados de:
        - Checkout
        - Build
        - Test
        - Deploy(construye app en contenedores dockey y despliega con balanceo de carga en dos nodos (nginx)).    

### Google Cloud
   -  Instancia VM  Ubuntu 18.04
   
![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/googleCloud.png)
### URL Jenkins
   - http://35.239.91.65:8080/
   - usuario: admin
   - password admin
   - Nombre pipLine en  Jenkins (PipeLineDevops) , se ejecuta cada 2 minutos
![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/jenkins.png)   
### URL APP MICROSERVICIO
   - http://35.239.91.65:8000/Devops
   - ### NOTA: NO ES HTTPS
### Directorio codigo fuente microservio
    devops_env

### Directorio comandos shell utilizados en infraestructura 
    infraestructura/comandos.md

## Lista de   archivos relacionados
   - #### Archivos pipline
        - pipline-source
           ###### Se encuentra el codigo de los stage   incluidos el deploy 
   - #### Archivos docker
        - Dockerfile (crear imagen de la app de microservio)
        - docker-compose.yml (archivo docker-compose para crear contenedores de la app y del balanceador de carga(gninx)).    
        - nginx/Dockerfile (crear la imagen del balanceador nginx).
   - ### Archivos sh
        - start1 (levantar el servidor del  nodo 1)
        - start2 (levantar el servidor del  nodo 2)
### Balanceo de carga
   - Se utiliza nginx en un contenedor que se encarga   hacer la peticion al nodo1 o nodo 2
        - Nginx contenedor configurado con el puerto 8000
        - Nodo1 contenedor(devops-container1) configurado con el puerto 8001
        - Nodo2 contenedor(devops-container2) configurado con el puerto 8002
 
             
     
### comando prueba con curl

curl -X POST http://35.239.91.65:8000/Devops   -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "Content-Type: application/json" -d  '{ "message" : "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec" : 45 }'

![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/TestMicroServicio.png)

-----------------------------------------------------------------------------
### ACTUALIZACION
Para la modificac{on de esta app se utilizo:
CircleCI.- en el proyecto se encuentra la configuracion del pipline (.circleci/config.yml)
	Este  valida :
	-Librerias utilizadas por la app del microservicio
	-Ejecuta los test del proyecto 
	-Deploya en proyecto en APP Engine cuenta aquingaluisa (gcloud-key-file.json) medianto una imagen doker que contiene el SDK de google.

NOTA: SI necesitan la cuenta de circleCI pedirme por whatapp ya que es la misma de mi githun y mi correo personal.

APP ENGINE se utiliza cuentas de servicio para poder logearse a goole cloud desde CircleCI y deployar la  app.

Se crea los Tests para validar los status de las peticiones HTTP en 200 y en 403 (devops_env/test.py)


El codigo se actualiza en el repositorio GIT https://github.com/angelquin1986/DevopsTestBP


NOTA: no pude utizar  molecular por cuestion de tiempo para la investigacion, CircleCI si deploya en APP ENGINE pero al momento del probar el microservicio, da un error de gateway de gninx.


Faltantes: Molecular y validar porque no respode en APIREST de APP ENGINE , se prueba localmente  y el microservicio si funciona.


![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/circleCI.png)
![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/circleCI2.png)
![alt text](https://raw.githubusercontent.com/angelquin1986/DevopsTestBP/master/assert/circleCI3.png)
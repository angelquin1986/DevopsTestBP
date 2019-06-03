# DevopsTestBP

Test para Banco Pichincha
Angel Quingaluisa

Lenguage Python 3.6

comando local

curl -X POST http://localhost:8000/devops   -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "Content-Type: application/json" -d  '{ "message" : "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec" : 45 }'

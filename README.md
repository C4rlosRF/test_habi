## Tecnologias
Se utilizará docker para exponer los microservicios y FAST Api para desarrollar el servicio de consulta.

## Instalación
1. instalar docker
2. crear y colocar credenciales de MySQL en test_habi\credentials.env
3. abrir terminal cmd e ir a la raiz del proyecto
4. en la terminal escribir "docker-compose up -d"
5. felicidades, ahora tiene Habi_Api funcionando.!
6. abrir, http://localhost:8009/Property/docs
## localhost:8009/Property/docs
### `docker-compose down --rmi all`
eliminar todas las imagenes y contenedores de docker-compose
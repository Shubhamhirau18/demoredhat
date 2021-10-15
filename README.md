## Prerequisite 

## Make Sure Port 443,3001 Not Already In Use on Host Machine

## Tested On Docker Version
- Docker version 20.10.8
- docker-compose version 1.29.2 

## Generate Self Signed Certificate (Linux)
- openssl req -newkey rsa:2048 -nodes -keyout nginx/my-site.com.key -x509 -days 365 -out nginx/my-site.com.crt

## How to Run (Docker Compose)
- docker volume create uptime-kuma
- docker-compose up -d

## Accessible Url - https://uptime.monitor.local/

## Customizations
- You can change this domain name "uptime.moitor.local" to whatever you want in file "nginx/nginx.conf"
- Make sure you have host entry OR Public domain pointed to server with Respective SSL Certificates

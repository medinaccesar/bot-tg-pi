![Static Badge](https://img.shields.io/badge/status-En%20desarrollo-brightgreen)
# bot-tg-pi
Bot de telegram para la Raspberry Pi

Permite el control remoto y la ejecución de comandos en la «Raspberri Pi» usando «telegram».

## Cosas que puede hacer
    - Resolver comandos privados y públicos.
    - Encender y apagar un centro multimedia (Kodi...).
    - Encender y apagar la cámara.
    - Encender y apagar un sensor de presencia:
        - El sensor enviará un mensaje a «telegram» cuando detecte movimiento.
        - El sensor activará la cámara y ésta comenzará a grabar.
        - Las grabaciones se guardan en la nube (Filen, Drive ... ).
    - Sacar una foto y recibirla por «Telegram».
    - Grabar vídeo y recibirlo por «Telegram».
    - Activar un servidor VNC con túnel ssh para el control gráfico de «RaspberriPi» desde otro equipo.
    - Estado de los posibles comandos (encendido/apagado).
    - Cualquier otra cosa que se quiera añadir:
           - Consultar el tiempo.
           - Activar o desactivar un servidor SFTP.
           - Activar o desactivar un servidor WEB.
           - (...)         
## Requisitos previos

1) Se necesita un «token» para poder acceder a la API de «telegram», se puede obtener creando un bot con «BotFather», se trata del bot oficial de «telegram» y dispone de un proceso guiado de creación de un bot que culmina con la obtención del «token».

2) Elementos físicos opcionales: 
    - Una cámara 
    - Un sensor de presencia

## Dependencias
    python-dotenv
    python-telegram-bot   
    gpiozero
Resolver dependencias

```
pip install .
```
  

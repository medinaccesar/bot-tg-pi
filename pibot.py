import argparse
import subprocess
from services.pid_service import PidService
from  util.locale_manager import _
from  constantes import Configuracion as conf
from  services.pibot_manager import PiBotManager
import os
import sys

from dotenv import load_dotenv

class PiBot():
   
    def __init__(self):
        token = os.getenv('TOKEN')
        user_id = os.getenv('USER_ID')         
        self._pibot_manager = PiBotManager(token,user_id) 
        self._guardar_pid()        

    def iniciar(self):
       
        self._pibot_manager.iniciar()     
    
    def _guardar_pid(self):
        pid_service = PidService()   
        pid_service.guardar_pid()

if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description=conf.NOMBRE_AP+" "+str(conf.VERSION))
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
            '-c', '--check', action='store_true', help=_('Comprueba la compatibilidad de la versión de la librería de telegram'))
    args = parser.parse_args()
    
    if args.check:
        script_path = "scripts" + os.path.sep + "comprobar_version.py"
        subprocess.run(["python", script_path])
    else:        
    
        pi_bot = PiBot()
        pi_bot.iniciar()
        
        

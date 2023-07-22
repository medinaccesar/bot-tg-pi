from setuptools import setup
from constantes import Configuracion as conf
setup(
    name = conf.NOMBRE_AP,
    version = conf.VERSION,
    packages=[''],
    install_requires=[
        'python-dotenv',
        'python-telegram-bot',
        'gpiozero',        
        'python-gettext'        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU GENERAL PUBLIC LICENSE V3',
        'Operating System :: OS Independent',
    ],
    description='Bot de telegram para la Raspberry Pi ',
    url='https://github.com/medinaccesar/bot-tg-pi'
)

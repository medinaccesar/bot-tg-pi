from setuptools import setup

setup(
    name='bot-tg-pi',
    version='1.0',
    packages=[''],
    install_requires=[
        'python-dotenv',
        'python-telegram-bot',
        'gpiozero'        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU GENERAL PUBLIC LICENSE V3',
        'Operating System :: OS Independent',
    ],
    description='Bot de telegram para la Raspberry Pi ',
    url='https://github.com/medinaccesar/bot-tg-pi'
)
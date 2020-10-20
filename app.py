from argparse import ArgumentParser
from string import Template
import os
texto = ''
arg_nome = ''
nomes = ''



def ler_cli():
    parser = ArgumentParser()
    parser.add_argument('nome', type=str)
    nome = parser.parse_args().nome
    ler_arquivo(nome)

def ler_arquivo(nome):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'Template\\Controllers\\WeatherForecastController.cs')
    with open('Template\\Controllers\\WeatherForecastController.cs', 'r') as f:
        text_file = f.read()
        template_text_file = Template(text_file).substitute(template=nome)
        escrever_arquivo(template_text_file)

def escrever_arquivo(texto_arquivo):
    with open('arq2.cs', 'w') as f:
        f.write(texto_arquivo)
ler_cli()

# Simple Python script to load template, load variables and render
from jinja2 import Environment, FileSystemLoader

import yaml,sys,os

stream = file(sys.argv[1], 'r')

config_data = yaml.load(stream)

env = Environment(loader = FileSystemLoader(os.path.dirname(os.path.abspath(__file__))), trim_blocks=True, lstrip_blocks=True)
template = env.get_template(sys.argv[2])

print(template.render(config_data))

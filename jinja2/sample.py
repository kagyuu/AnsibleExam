#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from jinja2 import Environment, FileSystemLoader
import yaml

def main():
    # load template
    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tmpl = env.get_template('template.j2')

    # load object
    f = open('data.yml')
    obj = yaml.load(f)
    f.close()

    # mix template and object
    output = tmpl.render(obj).encode('utf-8')
    print output

if __name__ == '__main__':
    main()


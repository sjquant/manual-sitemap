from importlib import import_module
import os
import sys

import click

from .core import (
    generate_url,
    create_xml_url
)

XML_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
"""
XML_FOOTER = "</urlset>"


@click.option('--output', default='sitemap.xml')
@click.argument('config')
@click.command()
def create_sitemap(config, output):
    """
    Create final sitemap
    """
    # import config
    # add current dir to sys.path to find module in your directory
    current_dir = os.getcwd()
    sys.path.insert(0, current_dir)
    obj = import_module(config)

    configs = {
        key: item
        for key, item in obj.__dict__.items()
        if key.isupper()
    }

    domain = configs['DOMAIN']
    routes = configs['ROUTES']
    queries = configs['QUERIES']

    with open(output, mode='w') as f:
        f.write(XML_HEADER)
        for url in generate_url(domain, routes, queries):
            f.write(create_xml_url(url))
        f.write(XML_FOOTER)
        print(output, 'created.')


if __name__ == "__main__":
    create_sitemap()

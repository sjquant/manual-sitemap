from typing import List, Dict, Tuple
from itertools import product

XML_URL = """    <url>
        <loc>{url}</loc>
    </url>
"""


def create_query_string(query_dict: Dict[str, str]):
    """Create query string with dictionary"""
    query_string = '?'
    for key, item in query_dict.items():
        query_string += '{}={}&'.format(key, item)
    return query_string[:-1]


def generate_url(domain: str,
                 routes: List[Tuple[str, List[str]]],
                 queries: Dict[str, List]):
    """
    Generate full_url which will be used to create sitemap

    Args:
        domain: domain name such as "http://example.com"
        routes: urls which after domain
                It consists of tuple ('url', [query string keys]).
                query string keys are used to match with queries in params.
        queries: query key and query values
                 which will be used such as {'page': [1,2,3,4]}

    Yields:
        full_url: full_url
    """
    for route in routes:
        # url and query_keys
        route_url, query_keys = route
        url = domain + route_url

        query_data = [queries[key] for key in query_keys]
        for each in product(*query_data):
            query_dict = dict(zip(query_keys, each))
            query_string = create_query_string(query_dict)
            full_url = url + query_string
            yield full_url


def create_xml_url(full_url: str):
    """
    create sitemap url format with full_url
    """
    return XML_URL.format(url=full_url)

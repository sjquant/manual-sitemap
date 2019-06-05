Manual Sitemap
==============

Introduction
-------------

Nowadays, SPA (Single Page Application) Websites using ``Vue``, ``React`` and ``Angular`` are booming. But, for those SPA websites, creating sitemap is not easy task for considering all uri query string and uri parameters. This module helps create sitemap manually using `python` file where we define urls, and query strings.

Installation
------------

``pip install manual-sitemap``

.. note::

    It might be good using virtualenv tools such as `virtualenv` and `pipenv` to protect your root python and avoid dependency issue.

Example
--------

Make config.py and set `DOMAIN`, `ROUTES` and `QUERIES` (optional).

.. code:: python

    # config.py

    DOMAIN = 'https://example.com'

    # (route, [querie string keys])
    # queries must be emtpy list if it has no query strings.
    ROUTES = [
        ('/exercise', ['page', 'date']),
        ('/homework', ['date']),
    ]

    # { query string key: [query string values ]}
    QUERIES = {
        'page': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'date': ['2019-01-01', '2019-04-03', '2019-04-08', '2019-05-06']
    }


Manual-sitemap can be easily run using ``manual-sitemap``

.. code::

    $ manual-sitemap config


.. note::

    - Remove ``.py`` at the end of config
    - You can change output filename using ``--output`` keyword

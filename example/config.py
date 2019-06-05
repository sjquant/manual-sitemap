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

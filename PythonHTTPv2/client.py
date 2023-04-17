import json
from hyper import HTTP20Connection

conn = HTTP20Connection('localhost:8080', secure=True)
conn.request('GET', '/')
resp = conn.get_response()

# process initial page with book ids
index_data = json.loads(resp.read().decode("utf8"))

print(index_data)

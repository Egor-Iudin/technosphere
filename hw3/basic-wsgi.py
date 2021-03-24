import json
from time import gmtime, strftime


def app(environ, start_response):
    data = json.dumps(
        {"time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
         "url": environ.get("RAW_URI")})
    data = data.encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

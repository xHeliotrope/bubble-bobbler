import os


from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', 
            port=int(os.environ.get('PORT', 8000)),
            workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
            debug=bool(os.environ.get('DEBUG', '')))



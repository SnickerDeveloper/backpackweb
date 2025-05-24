from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form action="/browse" method="get">
        <input name="url" type="text" placeholder="Enter URL" />
        <input type="submit" value="Go" />
    </form>
    '''

@app.route('/browse')
def browse():
    target_url = request.args.get('url')
    if not target_url:
        return 'No URL provided.'
    
    try:
        resp = requests.get(target_url)
        return Response(resp.content, content_type=resp.headers.get('Content-Type', 'text/html'))
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=8080)

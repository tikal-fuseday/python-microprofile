from flask import Flask
import sys
sys.path.append("/Users/mottidadison/work/fuse_022020/python-microprofile/spec/graphql/")
import graph

app = Flask(__name__)

@app.route('/')
def hello_whale():
    app.logger.info('hello_whale')
    return 'Whale, Hello there!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
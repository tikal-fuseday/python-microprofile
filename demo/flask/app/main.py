from flask import Flask, jsonify
import sys
sys.path.append("/Users/slavad/dev/python-microprofile")
import spec.health.microhealth.api as health_api

# sys.path.append("/Users/mottidadison/work/fuse_022020/python-microprofile/spec/graphql/")
# import graph

app = Flask(__name__)


@app.route('/')
def hello_whale():
    app.logger.info('hello_whale')
    return 'Whale, Hello there!'


@app.route('/health')
def get_health():
    return health_api.get_health()


@app.route('/health/ready')
def get_health_ready():
    return health_api.get_health_ready()


@app.route('/health/live')
def get_health_live():
    return health_api.get_health_live()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

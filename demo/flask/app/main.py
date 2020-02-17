from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

class Query(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="World"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name

schema = graphene.Schema(query=Query)

@app.route('/')
def hello_whale():
    app.logger.info('hello_whale')
    return 'Whale, Hello there!'


if __name__ == '__main__':
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True, host='0.0.0.0', port=8080)

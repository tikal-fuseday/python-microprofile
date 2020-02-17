from flask import Flask
from flask_graphql import GraphQLView
import graphene
from main import app

class Query(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="World"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name

schema = graphene.Schema(query=Query)

@app.route('/graphql/status')
def graph():
    return "running..."
         
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


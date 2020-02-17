
Microprofile Python GraphQL Specification
==========================================


## Specification:

GraphiQL is a powerfull graphical UI that enables a smooth and easy API discovery.

Just navigate to `/graphql` in your browser and you'll see [GraphiQL](https://github.com/graphql/graphiql/)


## About

GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data.

It provides an alternative, though not necessarily a replacement for REST.

GraphQL was developed internally by Facebook in 2012 before being publicly released in 2015.

## What is GraphQL?
GraphQL is a query language for your API, and a server-side runtime for executing queries by using a type system you define for your data. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data. [From [graphql.org](https://graphql.org/learn/)]

GraphQL is used by many large and small customers including Atlassian, Coursera, Facebook, GitHub, PayPal, Twitter, and https://graphql.org/users/[many more].

  

* More info: https://en.wikipedia.org/wiki/GraphQL

* Home page: https://graphql.org/

* Specification: https://facebook.github.io/graphql/draft/

  

## Why GraphQL

The main reasons developers might want to use GraphQL are:

  

* Improved data consumption for customers (IoS, Android, Web). Allowing for example to be able to retrieve several types of data in a single request or limiting the response data to exactly the specific data requested.

* Better analysis of the exhaustiveness of data calls (allowing to know the use of each node) and better manage the deletion of deprecated fields.

* Advanced developer experience:

** The schema defines how the data can be accessed and serves as the contract between the client and the server. Developer teams on both sides can work without further communication,

** Native schema introspection enabling to discover the API and to refine the queries on the client-side.

** On the client-side, the query language provides a lot of flexibility and efficiency enabling developers to adapt to the constraints of their technical environments (IoS, Android, Web).

  

## Why MicroProfile


The official purpose of MicroProfile is to optimize development for a microservices architecture and delivers application portability across multiple MicroProfile runtimes.

GraphQL is already widely used in Microservices architectures as the API Endpoint.

As noted in the Known java libraries section, there are several Java-based GraphQL libraries available, but none with the reach of the MicroProfile community.

GraphQL continues to grow in popularity, and as such there should be a specification for GraphQL development in Java.

MicroProfile is the optimal place to host that standard as it is open, ideally suited for incubating technologies, and has broad reach both in terms of the user community and vendor support.

  

## What GraphQL is not
  

This specification will focus on making it easy for developers to create a GraphQL Service/Endpoint and publish it as an API.

Where the data comes from (NoSQL, Relational DB, another service, etc.) is not the concern of this Proposed Specification.

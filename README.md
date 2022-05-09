# Idea: Example of how to use Classical Mapping with clear models for TDD with SQLAlchemy
Refactore existing code 
    https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
from ideas of the book "Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices"
at https://www.amazon.es/Architecture-Patterns-Python-Domain-Driven-Microservices/dp/1492052205
Book repository: https://github.com/cosmicpython/

Ideas of the book:
- separate models from database
- TDD

## v0 is Declarative Mapping in SQLAlchemy
Started with code from this tutorial on SQLAlchemy:
https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

## v1 is Classical Mapping
Created clear python models in `model.py`. Connected models with tables in `orm.py`. 
Test all in `queries_orm.py`

# Setup

`pip install -r requirements.txt`

`make build`

`make up`

# Run
`inserts.py` add data to database
`queries_orm.py` execute mapping model with PostreSQL and make queries from db.

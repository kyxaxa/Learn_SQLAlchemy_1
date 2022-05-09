# coding=utf-8

# 1 - imports
from model import *
import orm
from base import Session

orm.start_mappers()

session = Session()

# 3 - extract all movies
actors = session.query(Actor).all()
print(f"{len(actors)} actors: {actors=}")

movies = session.query(Movie).all()
movies = list(movies)

for num, movie in enumerate(movies, 1):
    print(f"{num}/{len(movies)} {movie=}")

# 5 - extract all stuntmans
stuntmans = session.query(Stuntman).all()

print(f"{len(stuntmans)} stuntmans: {stuntmans=}")

# 7 - get actors that have house in Glendale
glendale_stars = (
    session.query(Actor)
    .join(ContactDetails)
    .filter(ContactDetails.address.ilike("%glendale%"))
    .all()
)

print(f"\n### {len(glendale_stars)} Actors that live in Glendale:")
for actor in glendale_stars:
    print(f"{actor.name} has a house in Glendale")
print("")

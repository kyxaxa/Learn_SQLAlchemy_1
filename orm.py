from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import mapper, relationship, backref

import model


metadata = MetaData()

actors = Table(
    "actors",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("birthday", Date, nullable=True),
)

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255)),
    Column("release_date", Date, nullable=True),
    # actors = relationship("Actor", secondary=movies_actors_association)
)

movies_actors_association = Table(
    "movies_actors",
    metadata,
    Column("movie_id", Integer, ForeignKey("movies.id")),
    Column("actor_id", Integer, ForeignKey("actors.id")),
)

stuntmen = Table(
    "stuntmen",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("active", Boolean),
    Column("actor_id", Integer, ForeignKey("actors.id")),
    # actor = relationship("Actor", backref=backref("stuntman", uselist=False))
)

contact_details = Table(
    "contact_details",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("phone_number", String),
    Column("address", String),
    Column("actor_id", Integer, ForeignKey("actors.id")),
    # actor=relationship("Actor", backref="contact_details"),
)


def start_mappers():
    actor_mapper = mapper(model.Actor, actors)

    actor_movie_mapper = mapper(
        model.Movie,
        movies,
        properties={
            "actors": relationship(actor_mapper, secondary=movies_actors_association,)
        },
    )

    stuntmen_mapper = mapper(
        model.Stuntman,
        stuntmen,
        properties={
            "actor": relationship(
                actor_mapper, backref=backref("stuntman", uselist=False)
            )
        },
    )
    contact_details_mapper = mapper(
        model.ContactDetails,
        contact_details,
        properties={
            "actor": relationship(actor_mapper, backref=backref("contact_details"))
        },
    )

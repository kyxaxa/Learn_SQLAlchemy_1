from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Actor:
    name: str
    birthday: date


class Movie:
    def __init__(self, title: str, release_date: date):
        self.title = title
        self.release_date = release_date
        self.actors: List[Actor] = []

    def __repr__(self):
        return f"<`{self.title}` at {self.release_date} with {len(self.actors)} actors={self.actors}>"


class Stuntman:
    def __init__(self, name: str, active: bool, actor: Actor):
        self.name = name
        self.active = active
        self.actor = actor

    def __repr__(self):
        return f"<Stuntman {self.active} `{self.name}` with actor={self.actor}>"


@dataclass
class ContactDetails:
    phone_number: str
    address: str
    actor: Actor

    def __repr__(self):
        return f"<ContactDetails: phone {self.phone_number}, address {self.address} for actor={self.actor}>"

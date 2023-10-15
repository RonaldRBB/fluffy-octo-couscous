"""A module for generating random people."""
import randominfo as ri


class Person:
    """A person."""
    def __init__(self) -> None:
        self.first_name = ri.get_first_name()
        self.last_name = ri.get_last_name()
        self.birthdate = ri.get_birthdate()
        self.full_name = ri.get_full_name()
        self.email = ri.get_email(self)
        self.username = self.email.split("@")[0]

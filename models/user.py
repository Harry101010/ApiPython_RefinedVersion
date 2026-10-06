from .base import BaseEntity

class User(BaseEntity):
    def __init__(self, id, name: str, email: str):
        super().__init__(id)
        self.__name = name
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def to_dict(self):
        return {
            "type": "User",
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    __abstract__ = True

    def model_to_dict(self) -> dict | None:
        # Convert the model instance to a dictionary, excluding internal attributes
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}



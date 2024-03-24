import dataclasses
import uuid


@dataclasses.dataclass
class User:
    _id: uuid.UUID
    email: str

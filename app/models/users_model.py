from beanie import Document
from pydantic import Field


class User(Document):
    class Settings:
        name = "sample-users"
    
    name: str = Field(min_length=1)
    age: int = Field(gt=0)

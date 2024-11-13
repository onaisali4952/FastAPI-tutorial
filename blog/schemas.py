from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

# This is a pydantic model
# class Blog(BaseModel):
#     id: int
#     author: str
#     title: str
#     body: str
#     date_published: str
#     published_status: Optional[bool] = True

# This is a table 
class Blog(SQLModel, table = True):
    id: int = Field(primary_key=True, index=True)
    title: str = Field(index=True)
    author: str = Field()
    date_published: str | None = Field(default=None)
    body: str | None = Field(default=None)
    published_status: bool = Field(default=True)
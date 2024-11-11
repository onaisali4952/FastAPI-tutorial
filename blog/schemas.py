from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    author: str
    title: str
    content: str
    date_published: str
    published_status: Optional[bool] = True
    description: Optional[str] = None
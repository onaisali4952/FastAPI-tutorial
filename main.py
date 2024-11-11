from typing import Optional
from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

class Blog(BaseModel):
    author: str
    title: str
    content: str
    date_published: str
    published_status: Optional[bool] = True
    description: Optional[str] = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/blog_details")
def get_blog_list(limit: int = 10, sort: Optional[str] = None):
    return {"data" : f"{limit} blogs from the database"}

@app.get("/blog_details/{id}")
def get_blog_details(id:int):
    return {"Blog ID" : id}

@app.get("/blog_details/{id}/comments")
def get_blog_comments(id:int):
    return {"Blog Comments" : {"Comments List"}}

@app.post("/create_blog")
async def create_blog(blog: Blog):
    return {"Status": f"Blog was published by {blog.author} with title '{blog.title}'"}

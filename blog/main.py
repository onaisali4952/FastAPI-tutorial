from fastapi import FastAPI
from typing import Optional
from . import schemas

app = FastAPI()

@app.post("/create_blog")
async def create_blog(blog: schemas.Blog):
    return {"Status": f"Blog was published by {blog.author} with title '{blog.title}'"}
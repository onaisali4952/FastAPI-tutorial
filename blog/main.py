from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
from . import schemas
from . import database as db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Events on startup placed before yield
    db.create_db_and_tables()
    yield
    # Events before shutdown placed after yield

app = FastAPI(lifespan=lifespan)

@app.post("/create_blog")
async def create_blog(blog: schemas.Blog):
    return {"Status": f"Blog was published by {blog.author} with title '{blog.title}'"}

@app.post("/save_blog_to_db")
async def save_blog_to_db(blog: schemas.Blog, session: db.SessionDep) -> schemas.Blog:
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog

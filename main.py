from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': {
            'name': 'Juan'
        }
    }

@app.get('/about')
def about():
    return {
        'data': {
            'page_name': 'About Page'
        }
    }

@app.get('/blog')
def showBlog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    
    if published:
        return {
            'data': f'{limit} published blogs from the db'
        }
    else:
        return {
            'data': f'{limit} blogs from the db'
        }
    

@app.get('/blog/unplubished')
def unpublished():
    return {
        'data': {
            'unplubished_blogs': 'unpublished blogs here'
        }
    }

@app.get('/blog/{id}')
def show(id: int):
    return {
        'data': {
            'id': id
        }
    }

@app.get('/blog/{id}/comments')
def showComments(id: int):
    return {
        'data': {
            'id': id
        }
    }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': 'blog is created!'}
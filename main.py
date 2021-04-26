from fastapi import FastAPI

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
from fastapi import FastAPI
from routes.index import newsApi
app = FastAPI()


@app.get('/', tags=['Home'])
def home():
    return {'pageName': "Homepage"}


app.include_router(newsApi)

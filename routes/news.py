from fastapi import APIRouter
from models.index import News


newsApi = APIRouter()
news = News()


@newsApi.get('/news/', tags=['News'])
async def all_news():
    return "Welcome to Sri Lankan News Api"


@newsApi.get('/news/dailymirror', tags=['News'])
async def daily_mirror():
    return news.daily_mirror()


@newsApi.get('/news/tamilmirror', tags=['News'])
async def tamil_mirror():
    return news.tamil_mirror()


@newsApi.get('/news/newswire', tags=['News'])
async def newswire():
    return news.newswire()


@newsApi.get('/news/newsfirst/ta', tags=['News'])
async def newsfirsttamil():
    return news.newsfirsttamil()


@newsApi.get('/news/newsfirst/en', tags=['News'])
async def newsfirstenglish():
    return news.newsfirstenglish()


@newsApi.get('/news/newsfirst/sin', tags=['News'])
async def newsfirstsinhala():
    return news.newsfirstsinhala()
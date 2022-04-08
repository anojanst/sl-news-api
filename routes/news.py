from fastapi import APIRouter


newsApi = APIRouter()


@newsApi.get('/news/', tags=['News'])
async def all_news():
    return "Welcome to Sri Lankan News Api"

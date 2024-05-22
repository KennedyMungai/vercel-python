"""The main file for the app"""
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(
    title='Vercel FastAPI',
    description="A simple application to be deployed to vercel"
)

handler = Mangum(app)


@app.get('/', tags=['Root'])
async def root():
    """The root endpoint of the application

    Returns:
        dict: A dictionary containing a simple message
    """
    return {'message': 'Hello World'}

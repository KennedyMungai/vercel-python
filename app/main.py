"""The main file for the app"""
from fastapi import FastAPI

app = FastAPI(
    title='Vercel FastAPI',
    description="A simple application to be deployed to vercel"
)


@app.get('/')
async def root():
    return {'message': 'Hello World'}

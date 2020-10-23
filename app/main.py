
from fastapi import FastAPI, HTTPException, Request
import requests
import feedparser
import logging
import json

from .config import logs
from .config.pydantic_classes import TitleList, PiDec, NewsCount, AreaCircle


# Setting up logging
logs.setup_logging()
logger = logging.getLogger(__name__)
logger.info('Starting Pipple Lecture Test Application')


app = FastAPI()


@app.get("/reddit", response_model=TitleList)
def reddit():
    """
    :return: List of Titles of news of Reddit
    """

    logger = logging.getLogger(__name__)
    logger.info('START : Return list of titles')

    try:
        # TODO make function to retrieve reddit news categories
        titles = reddit.reddit_news()
        return TitleList(titles=titles)
    except Exception as e:
        logger.error(f'Stacktrace : {e}')
        raise HTTPException(status_code=500)


@app.get('/pi_generator', response_model=PiDec)
def pi_generator_default():
    # TODO : Add description
    logger.info(f'START : Return pi with 5 digits')

    url = f'https://uploadbeta.com/api/pi/?cached&n=5'
    try:
        # TODO : Get the number pi from url given in notebook and return pi as float with 5 digits
    # TODO : Raise Exception


@app.get('/pi_generator/{digits}', response_model=PiDec)
def pi_generator(digits: int):
    logger.info(f'START : Return pi with {digits} digits')

    url = f'https://uploadbeta.com/api/pi/?cached&n={str(digits + 1)}'
    try:
        # TODO : Get the number pi from url given in notebook and return pi as float with 5 digits
    # TODO : Raise Exception


@app.get('/reddit_cat_count', response_model=NewsCount)
def reddit_news_count(request: Request):
    # TODO : Add description
    """
    :return: number of categories in Reddit list
    """
    logger.info(f'START : Return number of categories within Reddit')

    url = f'http://{request.client.host}:8000/reddit'
    # TODO : Get the number pi from url given in notebook and return pi as float with 5 digits


@app.get('/area', response_model=AreaCircle)
def area(request: Request):
    """
    Calculate area of a circle with radius 1

    :param request: Request information of API - Automatically generated
    :return:  approximation of area of circle with radius 1
    """
    logger.info(f'START : Return area with radius 1')

    # TODO : get the number pi by using our own API (/pi_generator/100)
    # TODO : return area based on radius 1


@app.get('/area/{r}', response_model=AreaCircle)
def area(r: float, request: Request):
    """
    Calculate area of a circle

    :param request: Request information of API - Automatically generated
    :param r:  radius of circle
    :return:  approximation of area of circle
    """
    logger.info(f'START : Return area with radius of {r}')

    # TODO : get the number pi by using our own API (/pi_generator/100)
    # TODO : return area based on radius r

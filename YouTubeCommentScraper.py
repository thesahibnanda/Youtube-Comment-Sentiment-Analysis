#YouTube Comment Scraper
from youtube_comment_scraper_python import *
import pandas as pd


def YouTube_Comment(YTurl):

    #Comment Scraping
    youtube.open(YTurl)
    all_data = []
    for i in range(0,10):
        response = youtube.video_comments()
        data = response['body']
        all_data.extend(data)
    #Extracting Just Comments
    comments = []
    for i in all_data:
        comments.append(i["Comment"])
    #Only Getting Unique Comments As Scraper Can Give Duplicate Comments
    comments = list(set(comments))

    #Returning Comments
    return comments


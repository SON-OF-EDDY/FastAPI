from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel
from bank_of_quotes import collection
import random

app = FastAPI()

class Item(BaseModel):
    quote:str
    author:str

@app.get("/get-random/")
def get_item():

    size_collection= len(collection) - 1

    random_number = random.randint(0, size_collection)

    random_quote = collection[random_number]

    return random_quote

@app.get("/get-by-author/")
def get_item(author:Optional[str] = None):

    matching_quotes = []

    # split up the search string
    individual_words_search = author.lower().split(sep=' ')

    for item in collection:
        # split up the item string
        individual_words_item = collection[item]['author'].lower().split(sep=' ')
        for word in individual_words_item:
            if word in individual_words_search:
                matching_quotes.append(collection[item])

    # if still after everything the matching quotes array is empty...
    if matching_quotes != []:

        size_matching_quotes = len(matching_quotes)-1

        random_number = random.randint(0,size_matching_quotes)

        return matching_quotes[random_number]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No quotes from this author!")

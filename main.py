from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel
import random

app = FastAPI()

collection = {
    1: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    2: {'quote': "In the middle of every difficulty lies opportunity.", 'author': 'Albert Einstein'},
    3: {'quote': "Success is not final, failure is not fatal: It is the courage to continue that counts.", 'author': 'Winston Churchill'},
    4: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    5: {'quote': "Don't count the days; make the days count.", 'author': 'Muhammad Ali'},
    6: {'quote': "The only thing we have to fear is fear itself.", 'author': 'Franklin D. Roosevelt'},
    7: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    8: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    9: {'quote': "The greatest glory in living lies not in never falling, but in rising every time we fall.", 'author': 'Nelson Mandela'},
    10: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    11: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    12: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    13: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    14: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    15: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    16: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    17: {'quote': "Change your thoughts and you change your world.", 'author': 'Norman Vincent Peale'},
    18: {'quote': "Believe you can and you're halfway there.", 'author': 'Theodore Roosevelt'},
    19: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    20: {'quote': "It is during our darkest moments that we must focus to see the light.", 'author': 'Aristotle Onassis'},
    21: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    22: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    23: {'quote': "The greatest wealth is to live content with little.", 'author': 'Plato'},
    24: {'quote': "The best way to predict the future is to invent it.", 'author': 'Alan Kay'},
    25: {'quote': "Your time is limited, don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    26: {'quote': "Do what you can, with what you have, where you are.", 'author': 'Theodore Roosevelt'},
    27: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    28: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    29: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas Edison'},
    30: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    31: {'quote': "The greatest glory in living lies not in never falling, but in rising every time we fall.", 'author': 'Nelson Mandela'},
    32: {'quote': "The best way to predict your future is to create it.", 'author': 'Abraham Lincoln'},
    33: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    34: {'quote': "If you are not willing to risk the usual, you will have to settle for the ordinary.", 'author': 'Jim Rohn'},
    35: {'quote': "The way to get started is to quit talking and begin doing.", 'author': 'Walt Disney'},
    36: {'quote': "The future depends on what you do today.", 'author': 'Mahatma Gandhi'},
    37: {'quote': "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.", 'author': 'Steve Jobs'},
    38: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    39: {'quote': "Opportunities don't happen. You create them.", 'author': 'Chris Grosser'},
    40: {'quote': "It's not whether you get knocked down, it's whether you get up.", 'author': 'Vince Lombardi'},
    41: {'quote': "You have to learn the rules of the game. And then you have to play better than anyone else.", 'author': 'Albert Einstein'},
    42: {'quote': "The only thing we have to fear is fear itself.", 'author': 'Franklin D. Roosevelt'},
    43: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    44: {'quote': "Do not wait for leaders; do it alone, person to person.", 'author': 'Mother Teresa'},
    45: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    46: {'quote': "If you can dream it, you can do it.", 'author': 'Walt Disney'},
    47: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    48: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    49: {'quote': "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do.", 'author': 'Mark Twain'},
    50: {'quote': "Your time is limited, don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    51: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    52: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    53: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    54: {'quote': "Believe you can and you're halfway there.", 'author': 'Theodore Roosevelt'},
    55: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    56: {'quote': "It is during our darkest moments that we must focus to see the light.", 'author': 'Aristotle Onassis'},
    57: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    58: {'quote': "The greatest wealth is to live content with little.", 'author': 'Plato'},
    59: {'quote': "The best way to predict the future is to invent it.", 'author': 'Alan Kay'},
    60: {'quote': "Your time is limited, don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    61: {'quote': "Do what you can, with what you have, where you are.", 'author': 'Theodore Roosevelt'},
    62: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    63: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    64: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas Edison'},
    65: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    66: {'quote': "The greatest glory in living lies not in never falling, but in rising every time we fall.", 'author': 'Nelson Mandela'},
    67: {'quote': "The best way to predict your future is to create it.", 'author': 'Abraham Lincoln'},
    68: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    69: {'quote': "If you are not willing to risk the usual, you will have to settle for the ordinary.", 'author': 'Jim Rohn'},
    70: {'quote': "The way to get started is to quit talking and begin doing.", 'author': 'Walt Disney'},
    71: {'quote': "The future depends on what you do today.", 'author': 'Mahatma Gandhi'},
    72: {'quote': "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.", 'author': 'Steve Jobs'},
    73: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    74: {'quote': "Opportunities don't happen. You create them.", 'author': 'Chris Grosser'},
    75: {'quote': "It's not whether you get knocked down, it's whether you get up.", 'author': 'Vince Lombardi'},
    76: {'quote': "You have to learn the rules of the game. And then you have to play better than anyone else.", 'author': 'Albert Einstein'},
    77: {'quote': "The only thing we have to fear is fear itself.", 'author': 'Franklin D. Roosevelt'},
    78: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    79: {'quote': "Do not wait for leaders; do it alone, person to person.", 'author': 'Mother Teresa'},
    80: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    81: {'quote': "If you can dream it, you can do it.", 'author': 'Walt Disney'},
    82: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    83: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    84: {'quote': "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do.", 'author': 'Mark Twain'},
    85: {'quote': "Success is not final, failure is not fatal: It is the courage to continue that counts.", 'author': 'Winston Churchill'},
    86: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    87: {'quote': "Don't count the days; make the days count.", 'author': 'Muhammad Ali'},
    88: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    89: {'quote': "In the middle of every difficulty lies opportunity.", 'author': 'Albert Einstein'},
    90: {'quote': "Success is not final, failure is not fatal: It is the courage to continue that counts.", 'author': 'Winston Churchill'},
    91: {'quote': "The best way to predict the future is to invent it.", 'author': 'Alan Kay'},
    92: {'quote': "Don't count the days; make the days count.", 'author': 'Muhammad Ali'},
    93: {'quote': "The only thing we have to fear is fear itself.", 'author': 'Franklin D. Roosevelt'},
    94: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    95: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    96: {'quote': "The greatest glory in living lies not in never falling, but in rising every time we fall.", 'author': 'Nelson Mandela'},
    97: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    98: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    99: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    100: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'}
}

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

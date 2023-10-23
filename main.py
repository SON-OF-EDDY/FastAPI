from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel
import random

app = FastAPI()

collection = {
    1: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    2: {'quote': "In the middle of every difficulty lies opportunity.", 'author': 'Albert Einstein'},
    3: {'quote': "Success is not final, failure is not fatal: It is the courage to continue that counts.", 'author': 'Winston Churchill'},
    4: {'quote': "Your time is limited, don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    5: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    6: {'quote': "Don't watch the clock; do what it does. Keep going.", 'author': 'Sam Levenson'},
    7: {'quote': "The harder I work, the luckier I get.", 'author': 'Samuel Goldwyn'},
    8: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    9: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    10: {'quote': "Success usually comes to those who are too busy to be looking for it.", 'author': 'Henry David Thoreau'},
    11: {'quote': "Believe you can and you're halfway there.", 'author': 'Theodore Roosevelt'},
    12: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    13: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    14: {'quote': "The only source of knowledge is experience.", 'author': 'Albert Einstein'},
    15: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    16: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    17: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    18: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    19: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
    20: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    21: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    22: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    23: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    24: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    25: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    26: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    27: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    28: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    29: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    30: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    31: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    32: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    33: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    34: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    35: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    36: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    37: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    38: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    39: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    40: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    41: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    42: {'quote': "You become what you believe.", 'author': 'Oprah Winfrey'},
    43: {'quote': "You are what you believe yourself to be.", 'author': 'Paulo Coelho'},
    44: {'quote': "Do not wait for leaders; do it alone, person to person.", 'author': 'Mother Teresa'},
    45: {'quote': "The only thing that will stop you from fulfilling your dreams is you.", 'author': 'Tom Bradley'},
    46: {'quote': "You are the only person on earth who can use your ability.", 'author': 'Zig Ziglar'},
    47: {'quote': "Do not let what you cannot do interfere with what you can do.", 'author': 'John Wooden'},
    48: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    49: {'quote': "You become what you believe.", 'author': 'Oprah Winfrey'},
    50: {'quote': "You are what you believe yourself to be.", 'author': 'Paulo Coelho'},
    51: {'quote': "Do not wait for leaders; do it alone, person to person.", 'author': 'Mother Teresa'},
    52: {'quote': "The only thing that will stop you from fulfilling your dreams is you.", 'author': 'Tom Bradley'},
    53: {'quote': "You are the only person on earth who can use your ability.", 'author': 'Zig Ziglar'},
    54: {'quote': "Do not let what you cannot do interfere with what you can do.", 'author': 'John Wooden'},
    55: {'quote': "Aim for the moon. If you miss, you may hit a star.", 'author': 'W. Clement Stone'},
    56: {'quote': "The only place where success comes before work is in the dictionary.", 'author': 'Vidal Sassoon'},
    57: {'quote': "The biggest adventure you can take is to live the life of your dreams.", 'author': 'Oprah Winfrey'},
    58: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    59: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    60: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    61: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    62: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    63: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    64: {'quote': "You become what you believe.", 'author': 'Oprah Winfrey'},
    65: {'quote': "You are what you believe yourself to be.", 'author': 'Paulo Coelho'},
    66: {'quote': "Do not wait for leaders; do it alone, person to person.", 'author': 'Mother Teresa'},
    67: {'quote': "The only thing that will stop you from fulfilling your dreams is you.", 'author': 'Tom Bradley'},
    68: {'quote': "You are the only person on earth who can use your ability.", 'author': 'Zig Ziglar'},
    69: {'quote': "Do not let what you cannot do interfere with what you can do.", 'author': 'John Wooden'},
    70: {'quote': "Aim for the moon. If you miss, you may hit a star.", 'author': 'W. Clement Stone'},
    71: {'quote': "The only place where success comes before work is in the dictionary.", 'author': 'Vidal Sassoon'},
    72: {'quote': "The biggest adventure you can take is to live the life of your dreams.", 'author': 'Oprah Winfrey'},
    73: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    74: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    75: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    76: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    77: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    78: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    79: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
    80: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    81: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    82: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    83: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    84: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    85: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    86: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    87: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    88: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    89: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    90: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    91: {'quote': "Your time is limited, so don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    92: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    93: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    94: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    95: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    96: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    97: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    98: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    99: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    100: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    101: {'quote': "Always use 4-ply toilet paper.", 'author': 'Tim Hyde'}
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

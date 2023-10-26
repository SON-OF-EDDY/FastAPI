from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel
import random

app = FastAPI()

collection = {
    1: {'quote': "Believe you can and you're halfway there.", 'author': 'Theodore Roosevelt'},
    2: {'quote': "Life is either a daring adventure or nothing at all.", 'author': 'Helen Keller'},
    3: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    4: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    5: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    6: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    7: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    8: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    9: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    10: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    11: {'quote': "The harder I work, the luckier I get.", 'author': 'Samuel Goldwyn'},
    12: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    13: {'quote': "Success usually comes to those who are too busy to be looking for it.", 'author': 'Henry David Thoreau'},
    14: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    15: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    16: {'quote': "The only source of knowledge is experience.", 'author': 'Albert Einstein'},
    17: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    18: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    19: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    20: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
    21: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    22: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    23: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    24: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    25: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    26: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    27: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    28: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    29: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    30: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    31: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    32: {'quote': "Your time is limited, so don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    33: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    34: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    35: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    36: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    37: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    38: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    39: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    40: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    41: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    42: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    43: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    44: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    45: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    46: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    47: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    48: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    49: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    50: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    51: {'quote': "The harder I work, the luckier I get.", 'author': 'Samuel Goldwyn'},
    52: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    53: {'quote': "Success usually comes to those who are too busy to be looking for it.", 'author': 'Henry David Thoreau'},
    54: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    55: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    56: {'quote': "The only source of knowledge is experience.", 'author': 'Albert Einstein'},
    57: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    58: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    59: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    60: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
    61: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    62: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    63: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    64: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    65: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    66: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    67: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    68: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    69: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    70: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    71: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    72: {'quote': "Your time is limited, so don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    73: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    74: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    75: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    76: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    77: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    78: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    79: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    80: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    81: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    82: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    83: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    84: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    85: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    86: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    87: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    88: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    89: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    90: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    91: {'quote': "The harder I work, the luckier I get.", 'author': 'Samuel Goldwyn'},
    92: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    93: {'quote': "Success usually comes to those who are too busy to be looking for it.", 'author': 'Henry David Thoreau'},
    94: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    95: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    96: {'quote': "The only source of knowledge is experience.", 'author': 'Albert Einstein'},
    97: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    98: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    99: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    100: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
    101: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    102: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    103: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    104: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    105: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    106: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    107: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    108: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    109: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    110: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    111: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    112: {'quote': "Your time is limited, so don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    113: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    114: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    115: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    116: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    117: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    118: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    119: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    120: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    121: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    122: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    123: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    124: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    125: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    126: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    127: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    128: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    129: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    130: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    131: {'quote': "The harder I work, the luckier I get.", 'author': 'Samuel Goldwyn'},
    132: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    133: {'quote': "Success usually comes to those who are too busy to be looking for it.", 'author': 'Henry David Thoreau'},
    134: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    135: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    136: {'quote': "The only source of knowledge is experience.", 'author': 'Albert Einstein'},
    137: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    138: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    139: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    140: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
     141: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    142: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    143: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    144: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    145: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    146: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    147: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    148: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    149: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    150: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    151: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    152: {'quote': "Your time is limited, so don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    153: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    154: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    155: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    156: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    157: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    158: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    159: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    160: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
    161: {'quote': "What you get by achieving your goals is not as important as what you become by achieving your goals.", 'author': 'Zig Ziglar'},
    162: {'quote': "Success is walking from failure to failure with no loss of enthusiasm.", 'author': 'Winston Churchill'},
    163: {'quote': "The only limit to our realization of tomorrow will be our doubts of today.", 'author': 'Franklin D. Roosevelt'},
    164: {'quote': "The journey of a thousand miles begins with one step.", 'author': 'Lao Tzu'},
    165: {'quote': "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.", 'author': 'Jordan Belfort'},
    166: {'quote': "The best way to predict the future is to create it.", 'author': 'Peter Drucker'},
    167: {'quote': "The only thing necessary for the triumph of evil is for good men to do nothing.", 'author': 'Edmund Burke'},
    168: {'quote': "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible.", 'author': 'Joel Brown'},
    169: {'quote': "The future belongs to those who believe in the beauty of their dreams.", 'author': 'Eleanor Roosevelt'},
    170: {'quote': "The only way to do great work is to love what you do.", 'author': 'Steve Jobs'},
    171: {'quote': "The harder I work, the luckier I get.", 'author': 'Samuel Goldwyn'},
    172: {'quote': "It does not matter how slowly you go as long as you do not stop.", 'author': 'Confucius'},
    173: {'quote': "Success usually comes to those who are too busy to be looking for it.", 'author': 'Henry David Thoreau'},
    174: {'quote': "You are never too old to set another goal or to dream a new dream.", 'author': 'C.S. Lewis'},
    175: {'quote': "What lies behind us and what lies before us are tiny matters compared to what lies within us.", 'author': 'Ralph Waldo Emerson'},
    176: {'quote': "The only source of knowledge is experience.", 'author': 'Albert Einstein'},
    177: {'quote': "In the end, we will remember not the words of our enemies, but the silence of our friends.", 'author': 'Martin Luther King Jr.'},
    178: {'quote': "You miss 100% of the shots you don't take.", 'author': 'Wayne Gretzky'},
    179: {'quote': "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", 'author': 'Jimmy Dean'},
    180: {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.", 'author': 'Chinese Proverb'},
    181: {'quote': "It always seems impossible until it is done.", 'author': 'Nelson Mandela'},
    182: {'quote': "A journey of a thousand miles begins with a single step.", 'author': 'Lao Tzu'},
    183: {'quote': "Life is what happens when you're busy making other plans.", 'author': 'John Lennon'},
    184: {'quote': "The mind is everything. What you think you become.", 'author': 'Buddha'},
    185: {'quote': "You don't have to be great to start, but you have to start to be great.", 'author': 'Zig Ziglar'},
    186: {'quote': "A person who never made a mistake never tried anything new.", 'author': 'Albert Einstein'},
    187: {'quote': "The only person you are destined to become is the person you decide to be.", 'author': 'Ralph Waldo Emerson'},
    188: {'quote': "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", 'author': 'Ralph Waldo Emerson'},
    189: {'quote': "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.", 'author': 'Thomas A. Edison'},
    190: {'quote': "Life is really simple, but we insist on making it complicated.", 'author': 'Confucius'},
    191: {'quote': "The only true wisdom is in knowing you know nothing.", 'author': 'Socrates'},
    192: {'quote': "Your time is limited, so don't waste it living someone else's life.", 'author': 'Steve Jobs'},
    193: {'quote': "In the end, it's not the years in your life that count. It's the life in your years.", 'author': 'Abraham Lincoln'},
    194: {'quote': "In three words I can sum up everything I've learned about life: it goes on.", 'author': 'Robert Frost'},
    195: {'quote': "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", 'author': 'Christian D. Larson'},
    196: {'quote': "Life is 10% what happens to us and 90% how we react to it.", 'author': 'Charles R. Swindoll'},
    197: {'quote': "Life is short, and it is up to you to make it sweet.", 'author': 'Sarah Louise Delany'},
    198: {'quote': "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.", 'author': 'Mark Zuckerberg'},
    199: {'quote': "The best revenge is massive success.", 'author': 'Frank Sinatra'},
    200: {'quote': "To live is the rarest thing in the world. Most people exist, that is all.", 'author': 'Oscar Wilde'},
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

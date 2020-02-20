from random import randint 

def shuffle():

    images = ['assets/cat.png', 'assets/dog.png']
    url = images[randint(0,1)]

    return url

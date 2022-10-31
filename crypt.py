import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generate(int=8):
    password =''
    for i in range(int):
        password += random.choice(chars)
    return password

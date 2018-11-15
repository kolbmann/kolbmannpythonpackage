import random 
wildcats = ['A Bobcat', 'A Canada Lynx', 'A Eurasian Lynx', 'A Siberian Lynx', 'An Ocelot', 'A Margay', 'A Jaguarundi', 'A Geoffreys', 'A Serval', 'A Black Footed Cat', 'A Fishing Cat', 'A Caracal', 'A Kodkod', 'A Marbled Cat', 'A Sandcat']

def favorite_cat():
    print(random.choice(wildcats) + " is my favorite cat today!")
    print("**Just kidding they're all my favorite**")
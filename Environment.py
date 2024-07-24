#####

def sayilar():
    import random
    print(random.randrange(1, 6))
    global x,friends,y
    x = 15
    y = str(x)
    print(y)
    print(type(y))

    friends = ["Ugur", "Nazim", "Ozge", "Mujdat", "Mihrap"]
    a, b, c, d, e = friends
    print(friends)
sayilar()
from threading import Timer


def truth():
    print("Python rocks!")


t = Timer(3, truth)
t.start() # truth will be called after a 15 second interval
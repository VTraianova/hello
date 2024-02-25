def announce(f):
    def wrapper():
        print("About to run the functuon...")
        f()
        print("Done with a functuon.")
    return wrapper

@announce    
def hello():
    print("Hello, world!")  

hello()

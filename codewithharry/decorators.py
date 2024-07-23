def greet(fx):
    def mfx (*args,**kwargs):
        print("Thanks for using this function ")
        fx(*args,**kwargs)
        print("Hate you !")
    return mfx
@greet
def add(a,b):
    return a + b
x = add(1,2)
print(x)
# In those funcs where something is passed use args and kwargs in decorator func
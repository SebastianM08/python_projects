
def hello():
    print("Hello user, welcome!")

def pack(toothbrush, toothpaste, trimmer):
    return(toothbrush, toothpaste, trimmer)

def eat_lunch(lunchbag):
    if len(lunchbag) == 0:
        print("No lunch for me!")
    else:
        for i in range(len(lunchbag)):
            if i == 0:
                print(f"My lunch today is a {lunchbag[i]}")
            else:
                print(f"Then I will eat {lunchbag[i]}")

    
hello()
print(pack("toothbrush", "toothpaste", "trimmer"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["fruit","soda","sandwich","chocolate bar"]) 
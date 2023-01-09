##1.text file
#Opening a file
file=open("random.txt","w")
print(file.write("blah blah blah"))
print(file.write("\n new line"))
file=open("random.txt", "w")
print(file.write("Jyotirmoy"))
a=["jatin", "samarth", "sujith", "saransh"]
file.writelines(a)
file.close()

#file=open("sample.txt", "r")
#file.read()

##Streams 
# -->Iterables which can iterates in single direction
# -->It don't have starting and ending point

##Contex Programming 
with open("random.txt", "r") as file:
    print(file.read())


class A:
    def __enter__(self):
        print("Entered")
    def __exit__(self, *args):
        print("Exitted")
with A():
    print("inside context")
print("outside context")
print("")

class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self, *args):
        print("Exitted")
        print(args)
        return True
with A() as x:
    print(x)
    print("inside context")
    raise Exception
print("outside context")
print("")

##1.JSON files
#<html>
#    <body>
#        Hello World
#    </body>
#</html>
#In JSON-->
#{
#    "html":{
#        "body":"Hello World"
#    }
#}
a={
    "name":"Jatin Katayal",
    "marks":100,
    "languages":[
        "C++",
        "python",
        "go",
        "rust"
    ]
}
import json
a=json.dumps(a)
print(type(a))
print(a)
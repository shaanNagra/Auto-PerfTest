import sys

def parseFile(argumetns):
    try:
        if len(argumetns) == 2:
            file = open(argumetns[1],"r")
            file.read()

            file = open(argumetns[1],"r")
            return file
 
    except (IOError, ValueError, EOFError) as e:
        print(e)
        print("try again or type exit to stop")
        return None
    return None


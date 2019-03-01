def test():
    f=open("helloImAFile.txt", 'r') 

    contents = f.read()
    print(contents)
    if contents == "hello":
        print "passed"
    
        return True

    else:  
        return False

test()
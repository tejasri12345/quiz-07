for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("fizzbuzz");
        continue;
    elif(i%5==0):
        print("buzz");
        continue;
    elif(i%3==0):
        print("fizz");
        continue;
    else:
        print(i);
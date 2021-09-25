def areaCalculator():
    a=input("enter the shape you want to caculate the area of:")
    pie = 3.14
    area = 0
    if(a == "square"):
        side=int(input("Enter the value of side:"))
        area = area+(side**2)
    elif(a == "circle"):
        radius=int(input("Enter the value of the radius:"))
        area = area+(pie*radius**2)
    elif(a == "rectangle"):
        length=int(input("Enter the value of the length:"))
        breadth=int(input("Enter the value of the breadth:"))
        area = area+(length*breadth)
    elif(a == "triangle"):
        height=int(input("Enter the value of the height:"))
        base=int(input("Enter the value of the base:"))
        area = area+(0.5*base*height)
    else:
        print("please enter a valid shape")
    print("%.2f"%area)
areaCalculator()



x = input("1.ali \n2.mersad\n3.hasan\n4.saeed\n")

match x :
    case "1" :
        y =x
    case "2" :
        y =x
    case "3" :
        y =x
    case "4" :
        y =x
    case _ :
        print("bye")

sen = input("enter sen :\n")
if sen.isdigit():
    sen = int(sen)
else :
    print("vorodi na motabar")

match x :
    case "1" :
        print("ali",sen)
    case "2" :
        print("mersad",sen)
    case "3" :
        print("hasan",sen)
    case "4" :
        print("saeed",sen)
    case _ :
        print("bye")

name_1_1 = "soup"
p_1_1 = 250000

name_1_2 = "salad sezar"
p_1_2 = 450000

name_1_3 = "salad kimchi"
p_1_3 = 300000

name_1_4 = "gharch sokhari"
p_1_4 = 250000

name_1_5 = "sib zamini ba panir"
p_1_5 = 350000

print("\n\n" , "1.",name_1_1 ,"..." ,p_1_1, "\n", "2.", name_1_2 ,"..." ,p_1_2, "\n", "3.", name_1_3 ,"..." ,p_1_3, "\n", "4.", name_1_4 ,"..." ,p_1_4, "\n", "5.", name_1_5 ,"..." ,p_1_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
choice = input()


match choice :
    case "1" :
        name = name_1_1
        price = p_1_1
    case "2" :
        name = name_1_2
        price = p_1_2
    case "3" :
        name = name_1_3
        price = p_1_3
    case "4" :
        name = name_1_4
        price = p_1_4
    case "5" :
        name = name_1_5
        price = p_1_5
    case _ :
        print()


sub_choice = input ("1.edit name \n2.edit price \n3.edit name and price\n")
match sub_choice :
    case "1" :
        #if admin_user == 2 :
            #print("EROR :: user cant")
            #break

        name = input("please enter new name :\n")
        print("new name is :" , name)
    case "2" :
        new_price = input("please enter new price :\n")
        if new_price.isdigit():
            price = int(new_price)
            print("new price is :" , price)
        else:
            print("vorodi eshtebah ast")
        
    case "3" :
        #if admin_user == 2 :
            #print("EROR :: user cant")
            #break
        
        name = input("please enter new name :\n")
        new_price = input("please enter new price :\n")

        if new_price.isdigit():
            price = int(new_price)
            print("new name is :" , name, "and" ,"new price is :" , price )
        else:
            print("vorodie price eshtebah ast")

match choice :
    case "1" :
        name_1_1 = name
        p_1_1 = price
    case "2" :
        name_1_2 = name
        p_1_2 = price
    case "3" :
        name_1_3 = name
        p_1_3 = price
    case "4" :
        name_1_4 = name
        p_1_4 = price
    case "5" :
        name_1_5 = name
        p_1_5 = price
    case _ :
        print()

print("\n\n" , "1.",name_1_1 ,"..." ,p_1_1, "\n", "2.", name_1_2 ,"..." ,p_1_2, "\n", "3.", name_1_3 ,"..." ,p_1_3, "\n", "4.", name_1_4 ,"..." ,p_1_4, "\n", "5.", name_1_5 ,"..." ,p_1_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
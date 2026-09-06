


print("wellcome to my program")

#کاربر admin به همه امکانات دسترسی دارد
#کاربر user دسترسی محدود به امکانات دارد
main_username_admin = "admin"
main_password_admin = "admin"

main_username_user = "user"
main_password_user = "user"

backup_password = "12345"
bazyabi_password = "54321"

#عدد اول مربوط به سرفصل منو و عدد دوم مربوط به زیرمجموعه منو است
#منظور از name نام زیرمجموعه مورد نظر است
#منظور از p قیمت پایه است که خلاصه شده price است

business_name = "resturan golbahar"

sarfas_1 = "pish ghaza"

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


sarfas_2 = "ghazaye irani"

name_2_1 = " khorak kabab koobide"
p_2_1 = 600000

name_2_2 = "khorake jooje kabab"
p_2_2 = 500000

name_2_3 = "khorake kababe barg"
p_2_3 = 900000

name_2_4 = "khorake mahi ghezel ala"
p_2_4 = 800000

name_2_5 = "berenj irani"
p_2_5 = 180000


sarfas_3 = "ghazaye farangi"

name_3_1 = "stake reybon"
p_3_1 = 1300000

name_3_2 = "stake t-bon"
p_3_2 = 1400000

name_3_3 = "pasta alferdo"
p_3_3 = 600000

name_3_4 = "lazania"
p_3_4 = 700000

name_3_5 = "panini morgh"
p_3_5 = 800000


sarfas_4 = "fast food"

name_4_1 = "pizza goosht"
p_4_1 = 1100000

name_4_2 = "pizza jambon"
p_4_2 = 900000

name_4_3 = "file sokhari normal 4 tike"
p_4_3 = 1000000

name_4_4 = "burger"
p_4_4 = 750000

name_4_5 = "hotdog"
p_4_5 = 500000


sarfas_5 = "noshidani bar"

name_5_1 = "mohito"
p_5_1 = 250000

name_5_2 = "limonad"
p_5_2 = 200000

name_5_3 = "pinakolada"
p_5_3 = 350000

name_5_4 = "coffee"
p_5_4 = 280000

name_5_5 = "nooshabe"
p_5_5 = 100000

total_por_forosh_name = " "
total_kam_forosh_name = " "

por_forosh_name_1 = " "
por_forosh_name_2 = " "
por_forosh_name_3 = " "
por_forosh_name_4 = " "
por_forosh_name_5 = " "

kam_forosh_name_1 = " "
kam_forosh_name_2 = " "
kam_forosh_name_3 = " "
kam_forosh_name_4 = " "
kam_forosh_name_5 = " "

d_servis = 0.12
d_tax = 0.09
s_peyk = 100000

tedad_factor = 0

total_num = 0

total_num_1_1 = 0
total_num_1_2 = 0
total_num_1_3 = 0
total_num_1_4 = 0
total_num_1_5 = 0

total_num_2_1 = 0
total_num_2_2 = 0
total_num_2_3 = 0
total_num_2_4 = 0
total_num_2_5 = 0

total_num_3_1 = 0
total_num_3_2 = 0
total_num_3_3 = 0
total_num_3_4 = 0
total_num_3_5 = 0

total_num_4_1 = 0
total_num_4_2 = 0
total_num_4_3 = 0
total_num_4_4 = 0
total_num_4_5 = 0

total_num_5_1 = 0
total_num_5_2 = 0
total_num_5_3 = 0
total_num_5_4 = 0
total_num_5_5 = 0


total_forosh = 0
total_num_forosh = 0
por_forosh_1 = 0
por_forosh_2 = 0
por_forosh_3 = 0
por_forosh_4 = 0
por_forosh_5 = 0

kam_forosh_1 = 0
kam_forosh_2 = 0
kam_forosh_3 = 0
kam_forosh_4 = 0
kam_forosh_5 = 0

total_por_forosh = 0
total_kam_forosh = 0

total_sell_1_1 = 0
total_sell_1_2 = 0
total_sell_1_3 = 0
total_sell_1_4 = 0
total_sell_1_5 = 0

total_sell_2_1 = 0
total_sell_2_2 = 0
total_sell_2_3 = 0
total_sell_2_4 = 0
total_sell_2_5 = 0

total_sell_3_1 = 0
total_sell_3_2 = 0
total_sell_3_3 = 0
total_sell_3_4 = 0
total_sell_3_5 = 0

total_sell_4_1 = 0
total_sell_4_2 = 0
total_sell_4_3 = 0
total_sell_4_4 = 0
total_sell_4_5 = 0

total_sell_5_1 = 0
total_sell_5_2 = 0
total_sell_5_3 = 0
total_sell_5_4 = 0
total_sell_5_5 = 0

num_salon = 0
num_peyk = 0



#shomarande change password
j = 0
#shomarande passworde admin
k = 0
start = 0
administrator_exit = 0
program_exit = 0
no_order = 0
admin_user = 0
price = 0

while True :

    while True :

        if program_exit == 1 :
            break

        if start == "2" :
            break

        if k < 3 :

            while True :

                administrator_exit = 0
                
                start = input("1.administrator \n2.sefaresh giri\n0.EXIT_0_\n")
               

                if start == "0" :
                    program_exit = 1
                    break
                else :
                    program_exit = 0
                

                if start == "2" :
                        break

                match start :

                    case "1" :

                        if k < 3 :

                            while True :

                                if administrator_exit == 1 :
                                    break

                                print("EXIT_0_\ntalashe", k +1 ,"/3\n" ,"please enter username :\n")
                                username = input( )

                                if username == "0" and k < 2 :

                                    k = 0

                                    break

                                password = input("0EXIT_0_\nplease enter password :\n")

                                if password == "0" and k < 2 :

                                    k = 0

                                    break

                                if username == main_username_admin and password == main_password_admin or username == main_username_user and password == main_password_user :

                                    if username == main_username_admin and password == main_password_admin :

                                        admin_user = 1

                                    elif username == main_username_user and password == main_password_user :

                                        admin_user = 2
                                    

                                    k = 0

                                    while True :

                                        print("\n" , "\n1.edit" , sarfas_1 ,"\n2.edit",sarfas_2,"\n3.edit", sarfas_3, "\n4.edit",sarfas_4,"\n5.edit", sarfas_5, "\n6.edit service/tax/peyk \n7.gozareshat \n8.change username and password \n9.change business name \n0.EXIT_0_\n")
                                        menu = input()
                                        administrator_exit = 0
                                        if menu == "0" :
                                            administrator_exit = 1
                                            break

                                        while True :

                                            match menu :
                                                case "1" :
                                                    if j < 3 :
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
                                                            case "6" :
                                                                name = sarfas_1
                                                            case _ :
                                                                break


                                                        sub_choice = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match sub_choice :
                                                            case "1" :
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break

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
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break
                                                                
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
                                                            case "6" :
                                                                sarfas_1 = name
                                                            case _ :
                                                                break
                                                    else :
                                                        print("you are block")
                                                        break


                                        
                                                case "2" :
                                                    if j < 3 :
                                                        print("\n\n" , "1.",name_2_1 ,"..." ,p_2_1, "\n", "2.", name_2_2 ,"..." ,p_2_2, "\n", "3.", name_2_3 ,"..." ,p_2_3, "\n", "4.", name_2_4 ,"..." ,p_2_4, "\n", "5.", name_2_5 ,"..." ,p_2_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                        choice = input()
                                    
                                                        match choice :
                                                            case "1" :
                                                                name = name_2_1
                                                                price = p_2_1
                                                            case "2" :
                                                                name = name_2_2
                                                                price = p_2_2
                                                            case "3" :
                                                                name = name_2_3
                                                                price = p_2_3
                                                            case "4" :
                                                                name = name_2_4
                                                                price = p_2_4
                                                            case "5" :
                                                                name = name_2_5
                                                                price = p_2_5
                                                            case "6" :
                                                                name = sarfas_2
                                                            case _ :
                                                                break


                                                        sub_choice = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match sub_choice :
                                                            case "1" :
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break

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
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break
                                                                
                                                                name = input("please enter new name :\n")
                                                                new_price = input("please enter new price :\n")

                                                                if new_price.isdigit():
                                                                    price = int(new_price)
                                                                    print("new name is :" , name, "and" ,"new price is :" , price )
                                                                else:
                                                                    print("vorodie price eshtebah ast")

                                                        match choice :
                                                            case "1" :
                                                                name_2_1 = name
                                                                p_2_1 = price
                                                            case "2" :
                                                                name_2_2 = name
                                                                p_2_2 = price
                                                            case "3" :
                                                                name_2_3 = name
                                                                p_2_3 = price
                                                            case "4" :
                                                                name_2_4 = name
                                                                p_2_4 = price
                                                            case "5" :
                                                                name_2_5 = name
                                                                p_2_5 = price
                                                            case "6" :
                                                                sarfas_2 = name
                                                            case _ :
                                                                break
                                                    else :
                                                        print("you are block")
                                                        break
                                                    
                                
                                                case "3" :
                                                    if j < 3 :
                                                        print("\n\n" , "1.",name_3_1 ,"..." ,p_3_1, "\n", "2.", name_3_2 ,"..." ,p_3_2, "\n", "3.", name_3_3 ,"..." ,p_3_3, "\n", "4.", name_3_4 ,"..." ,p_3_4, "\n", "5.", name_3_5 ,"..." ,p_3_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                        choice = input()
                                    
                                                        match choice :
                                                            case "1" :
                                                                name = name_3_1
                                                                price = p_3_1
                                                            case "2" :
                                                                name = name_3_2
                                                                price = p_3_2
                                                            case "3" :
                                                                name = name_3_3
                                                                price = p_3_3
                                                            case "4" :
                                                                name = name_3_4
                                                                price = p_3_4
                                                            case "5" :
                                                                name = name_3_5
                                                                price = p_3_5
                                                            case "6" :
                                                                name = sarfas_3
                                                            case _ :
                                                                break


                                                        sub_choice = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match sub_choice :
                                                            case "1" :
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break

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
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break
                                                                
                                                                name = input("please enter new name :\n")
                                                                new_price = input("please enter new price :\n")

                                                                if new_price.isdigit():
                                                                    price = int(new_price)
                                                                    print("new name is :" , name, "and" ,"new price is :" , price )
                                                                else:
                                                                    print("vorodie price eshtebah ast")

                                                        match choice :
                                                            case "1" :
                                                                name_3_1 = name
                                                                p_3_1 = price
                                                            case "2" :
                                                                name_3_2 = name
                                                                p_3_2 = price
                                                            case "3" :
                                                                name_3_3 = name
                                                                p_3_3 = price
                                                            case "4" :
                                                                name_3_4 = name
                                                                p_3_4 = price
                                                            case "5" :
                                                                name_3_5 = name
                                                                p_3_5 = price
                                                            case "6" :
                                                                sarfas_3 = name
                                                            case _ :
                                                                break
                                                    else :
                                                        print("you are block")
                                                        break
                                                        
                                                case "4" :
                                                    if j < 3 :
                                                        print("\n\n" , "1.",name_4_1 ,"..." ,p_4_1, "\n", "2.", name_4_2 ,"..." ,p_4_2, "\n", "3.", name_4_3 ,"..." ,p_4_3, "\n", "4.", name_4_4 ,"..." ,p_4_4, "\n", "5.", name_4_5 ,"..." ,p_4_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                        choice = input()
                                    
                                                        match choice :
                                                            case "1" :
                                                                name = name_4_1
                                                                price = p_4_1
                                                            case "2" :
                                                                name = name_4_2
                                                                price = p_4_2
                                                            case "3" :
                                                                name = name_4_3
                                                                price = p_4_3
                                                            case "4" :
                                                                name = name_4_4
                                                                price = p_4_4
                                                            case "5" :
                                                                name = name_4_5
                                                                price = p_4_5
                                                            case "6" :
                                                                name = sarfas_4
                                                            case _ :
                                                                break


                                                        sub_choice = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match sub_choice :
                                                            case "1" :
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break

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
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break
                                                                
                                                                name = input("please enter new name :\n")
                                                                new_price = input("please enter new price :\n")

                                                                if new_price.isdigit():
                                                                    price = int(new_price)
                                                                    print("new name is :" , name, "and" ,"new price is :" , price )
                                                                else:
                                                                    print("vorodie price eshtebah ast")

                                                        match choice :
                                                            case "1" :
                                                                name_4_1 = name
                                                                p_4_1 = price
                                                            case "2" :
                                                                name_4_2 = name
                                                                p_4_2 = price
                                                            case "3" :
                                                                name_4_3 = name
                                                                p_4_3 = price
                                                            case "4" :
                                                                name_4_4 = name
                                                                p_4_4 = price
                                                            case "5" :
                                                                name_4_5 = name
                                                                p_4_5 = price
                                                            case "6" :
                                                                sarfas_4 = name
                                                            case _ :
                                                                break
                                                    else :
                                                        print("you are block")
                                                        break

                                                        
                                                case "5" :
                                                    if j < 3 :
                                                        print("\n\n" , "1.",name_5_1 ,"..." ,p_5_1, "\n", "2.", name_5_2 ,"..." ,p_5_2, "\n", "3.", name_5_3 ,"..." ,p_5_3, "\n", "4.", name_5_4 ,"..." ,p_5_4, "\n", "5.", name_5_5 ,"..." ,p_5_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                        choice = input()
                                    
                                                        match choice :
                                                            case "1" :
                                                                name = name_5_1
                                                                price = p_5_1
                                                            case "2" :
                                                                name = name_5_2
                                                                price = p_5_2
                                                            case "3" :
                                                                name = name_5_3
                                                                price = p_5_3
                                                            case "4" :
                                                                name = name_5_4
                                                                price = p_5_4
                                                            case "5" :
                                                                name = name_5_5
                                                                price = p_5_5
                                                            case "6" :
                                                                name = sarfas_5
                                                            case _ :
                                                                break


                                                        sub_choice = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match sub_choice :
                                                            case "1" :
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break

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
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break
                                                                
                                                                name = input("please enter new name :\n")
                                                                new_price = input("please enter new price :\n")

                                                                if new_price.isdigit():
                                                                    price = int(new_price)
                                                                    print("new name is :" , name, "and" ,"new price is :" , price )
                                                                else:
                                                                    print("vorodie price eshtebah ast")

                                                        match choice :
                                                            case "1" :
                                                                name_5_1 = name
                                                                p_5_1 = price
                                                            case "2" :
                                                                name_5_2 = name
                                                                p_5_2 = price
                                                            case "3" :
                                                                name_5_3 = name
                                                                p_5_3 = price
                                                            case "4" :
                                                                name_5_4 = name
                                                                p_5_4 = price
                                                            case "5" :
                                                                name_5_5 = name
                                                                p_5_5 = price
                                                            case "6" :
                                                                sarfas_5 = name
                                                            case _ :
                                                                break
                                                    else :
                                                        print("you are block")
                                                        break

                                                case "6" :
                                                    if j < 3 :
                                                        d_servis = input("please enter service percent :\n")
                                                        if d_servis.isdigit():
                                                            d_servis = int(d_servis)
                                                        else:
                                                            print("vorodi eshtebah ast")

                                                        d_servis = d_servis /100

                                                        d_tax = input("please enter tax percent :\n")
                                                        if d_tax.isdigit():
                                                            d_tax = int(d_tax)
                                                        else:
                                                            print("vorodi eshtebah ast")

                                                        d_tax = d_tax /100

                                                        s_peyk = input("please enter peyk price :\n")
                                                        if s_peyk.isdigit():
                                                            s_peyk = int(s_peyk)
                                                        else:
                                                            print("vorodi eshtebah ast")
                                                                        
                                                        break
                                                    else :
                                                        print("you are block")
                                                        break

                                                case "7" :
                                                    if j < 3 :
                                                        gozaresh = input("\n1.amare foroshe mahsoolat \n2.por forosh tarin mahsoolat \n3.kam forosh tarin mahsoolat \n4.amare kole forosh \n5.back to main menu \n")
                                                        match gozaresh :
                                                            case "1" :

                                                                print("\n", sarfas_1 , "...." , total_num_1_1+total_num_1_2+total_num_1_3+total_num_1_4+total_num_1_5 , "adad" , "..." , total_sell_1_1+total_sell_1_2+total_sell_1_3+total_sell_1_4+total_sell_1_5)
                                                                print("\n", sarfas_2 , "...." , total_num_2_1+total_num_2_2+total_num_2_3+total_num_2_4+total_num_2_5 , "adad" , "..." , total_sell_2_1+total_sell_2_2+total_sell_2_3+total_sell_2_4+total_sell_2_5)
                                                                print("\n", sarfas_3 , "...." , total_num_3_1+total_num_3_2+total_num_3_3+total_num_3_4+total_num_3_5 , "adad" , "..." , total_sell_3_1+total_sell_3_2+total_sell_3_3+total_sell_3_4+total_sell_3_5)
                                                                print("\n", sarfas_4 , "...." , total_num_4_1+total_num_4_2+total_num_4_3+total_num_4_4+total_num_4_5 , "adad" , "..." , total_sell_4_1+total_sell_4_2+total_sell_4_3+total_sell_4_4+total_sell_4_5)
                                                                print("\n", sarfas_5 , "...." , total_num_5_1+total_num_5_2+total_num_5_3+total_num_5_4+total_num_5_5 , "adad" , "..." , total_sell_5_1+total_sell_5_2+total_sell_5_3+total_sell_5_4+total_sell_5_5)

                                                                print("\n1.", name_1_1 , "...." , total_num_1_1 , "adad" , "..." , total_sell_1_1)
                                                                print("\n2.", name_1_2 , "...." , total_num_1_2 , "adad" , "..." , total_sell_1_2)
                                                                print("\n3.", name_1_3 , "...." , total_num_1_3 , "adad" , "..." , total_sell_1_3)
                                                                print("\n4.", name_1_4 , "...." , total_num_1_4 , "adad" , "..." , total_sell_1_4)
                                                                print("\n5.", name_1_5 , "...." , total_num_1_5 , "adad" , "..." , total_sell_1_5)

                                                                print("\n6.", name_2_1 , "...." , total_num_2_1 , "adad" , "..." , total_sell_2_1)
                                                                print("\n7.", name_2_2 , "...." , total_num_2_2 , "adad" , "..." , total_sell_2_2)
                                                                print("\n8.", name_2_3 , "...." , total_num_2_3 , "adad" , "..." , total_sell_2_3)
                                                                print("\n9.", name_2_4 , "...." , total_num_2_4 , "adad" , "..." , total_sell_2_4)
                                                                print("\n10.", name_2_5 , "...." , total_num_2_5 , "adad" , "..." , total_sell_2_5)

                                                                print("\n11.", name_3_1 , "...." , total_num_3_1 , "adad" , "..." , total_sell_3_1)
                                                                print("\n12.", name_3_2 , "...." , total_num_3_2 , "adad" , "..." , total_sell_3_2)
                                                                print("\n13.", name_3_3 , "...." , total_num_3_3 , "adad" , "..." , total_sell_3_3)
                                                                print("\n14.", name_3_4 , "...." , total_num_3_4 , "adad" , "..." , total_sell_3_4)
                                                                print("\n15.", name_3_5 , "...." , total_num_3_5 , "adad" , "..." , total_sell_3_5)

                                                                print("\n16.", name_4_1 , "...." , total_num_4_1 , "adad" , "..." , total_sell_4_1)
                                                                print("\n17.", name_4_2 , "...." , total_num_4_2 , "adad" , "..." , total_sell_4_2)
                                                                print("\n18.", name_4_3 , "...." , total_num_4_3 , "adad" , "..." , total_sell_4_3)
                                                                print("\n19.", name_4_4 , "...." , total_num_4_4 , "adad" , "..." , total_sell_4_4)
                                                                print("\n20.", name_4_5 , "...." , total_num_4_5 , "adad" , "..." , total_sell_4_5)

                                                                print("\n21.", name_5_1 , "...." , total_num_5_1 , "adad" , "..." , total_sell_5_1)
                                                                print("\n22.", name_5_2 , "...." , total_num_5_2 , "adad" , "..." , total_sell_5_2)
                                                                print("\n23.", name_5_3 , "...." , total_num_5_3 , "adad" , "..." , total_sell_5_3)
                                                                print("\n24.", name_5_4 , "...." , total_num_5_4 , "adad" , "..." , total_sell_5_4)
                                                                print("\n25.", name_5_5 , "...." , total_num_5_5 , "adad" , "..." , total_sell_5_5)


                                                                
                                                            case "2" :
                                                                print("por forosh tarin mahsool " ,total_por_forosh_name , "...." , total_por_forosh , "adad")
                                                                print("por forosh tarin mahsoole ",sarfas_1 ,por_forosh_name_1 , "...." , por_forosh_1 , "adad")
                                                                print("por forosh tarin mahsoole ",sarfas_2 ,por_forosh_name_2 , "...." , por_forosh_2 , "adad")
                                                                print("por forosh tarin mahsoole ",sarfas_3 ,por_forosh_name_3 , "...." , por_forosh_3 , "adad")
                                                                print("por forosh tarin mahsoole ",sarfas_4 ,por_forosh_name_4 , "...." , por_forosh_4 , "adad")
                                                                print("por forosh tarin mahsoole ",sarfas_5 ,por_forosh_name_5 , "...." , por_forosh_5 , "adad")



                                                            case "3" :
                                                                print("kam forosh tarin mahsool " ,total_kam_forosh_name , "...." , total_kam_forosh , "adad")
                                                                print("kam forosh tarin mahsoole ",sarfas_1 ,kam_forosh_name_1 , "...." , kam_forosh_1 , "adad")
                                                                print("kam forosh tarin mahsoole ",sarfas_2 ,kam_forosh_name_2 , "...." , kam_forosh_2 , "adad")
                                                                print("kam forosh tarin mahsoole ",sarfas_3 ,kam_forosh_name_3 , "...." , kam_forosh_3 , "adad")
                                                                print("kam forosh tarin mahsoole ",sarfas_4 ,kam_forosh_name_4 , "...." , kam_forosh_4 , "adad")
                                                                print("kam forosh tarin mahsoole ",sarfas_5 ,kam_forosh_name_5 , "...." , kam_forosh_5 , "adad")
                                                            case "4" :
                                                                if admin_user == 2 :
                                                                    print("EROR :: user cant")
                                                                    break
                                                                print("\ntedade factor haye sader shode :", tedad_factor ,"\ntedade mahsoolate sefaresh dade shode :" , total_num , "\nmajmooe kole daramd :" , int(total_forosh) , "\ntedade biron bar :", num_peyk , "\ntedade salon :" , num_salon)
                                                        
                                                            case _ :
                                                                break

                                                    else :
                                                        print("you are block")
                                                        break


                                                case "8" :
                                                    if admin_user == 2 :
                                                        print("EROR :: user cant")
                                                        break

                                                    if j < 3 :
                                                        for i in range(3):
                                                            change_password = input("please enter backup password :\n")
                                                            if change_password == backup_password :
                                                                j = 0
                                                                change = input ("1.change admin username \n2.change admin password\n3.change admin username and password\n4.change user username\n5.change user password \n6.change user username and password \n7.change backup password \n")
                                                                match change :
                                                                    case "1" :
                                                                        main_username_admin = input("please enter new username :\n")
                                                                        print("new username is :" , main_username_admin)
                                                                    case "2" :
                                                                        main_password_admin = input("please enter new password :\n")
                                                                        print("new password is :" , main_password_admin)
                                                                    case "3" :
                                                                        main_username_admin = input("please enter new username :\n")
                                                                        main_password_admin = input("please enter new password :\n")
                                                                        print("new username is :" , main_username_admin, "and" ,"new password is :" , main_password_admin )
                                                                    case "4" :
                                                                        main_username_user = input("please enter new username :\n")
                                                                        print("new username is :" , main_username_user)
                                                                    case "5" :
                                                                        main_password_user = input("please enter new password :\n")
                                                                        print("new password is :" , main_password_user)
                                                                    case "6" :
                                                                        main_username_user = input("please enter new username :\n")
                                                                        main_password_user = input("please enter new password :\n")
                                                                        print("new username is :" , main_username_user, "and" ,"new password is :" , main_password_user )
                                                                    case "7" :
                                                                        backup_password = input("please enter new backup password")
                                                                    case _ :
                                                                        break
                                                            else :
                                                                print("backup password wrong")
                                                                j+=1
                                                            if j == 3 :
                                                                print("you are block")
                                                                break
                                                    else :
                                                        print("you are block")
                                                        break
                                                        
                                                case "9" :
                                                    if admin_user == 2 :
                                                        print("EROR :: user cant")
                                                        break
                                                    busines_name = input("please enter new business name")

                                else :
                                    print("username or password wrong")
                                
                                    k +=1
                                    if k == 3 :
                                        print("you are block")
                                        break

                        else :
                            print("you are block")
                            break

                    case _ :
                        
                        break
                        


        else :
            bazyabi = input("1.bazyabi admin \n2.moshtari\n")
            match bazyabi :
                case "1" :
                    b_password = input("please enter bazyabi password :\n")
                    if b_password == bazyabi_password :
                        k = 0
                        print("you are unblocked")
                        while True :
                            new_bazyabi_password = input("lotfan ramze bazyabi ra avaz konid :\n")
                            if new_bazyabi_password == bazyabi_password :
                                print("new bazyabi password wrong")
                                continue
                            else :
                                bazyabi_password = new_bazyabi_password
                                break
                case _:
                    p = 1
                    break
                    
    start = 0        
        
                
    while True :

        if program_exit == 1 :
            break

        print("\n\n *** wellcome to ",business_name.upper(), " *** ")
        
        num_1_1 = 0
        num_1_2 = 0
        num_1_3 = 0
        num_1_4 = 0
        num_1_5 = 0

        num_2_1 = 0
        num_2_2 = 0
        num_2_3 = 0
        num_2_4 = 0
        num_2_5 = 0

        num_3_1 = 0
        num_3_2 = 0
        num_3_3 = 0
        num_3_4 = 0
        num_3_5 = 0

        num_4_1 = 0
        num_4_2 = 0
        num_4_3 = 0
        num_4_4 = 0
        num_4_5 = 0

        num_5_1 = 0
        num_5_2 = 0
        num_5_3 = 0
        num_5_4 = 0
        num_5_5 = 0

        n_1_1 = 0
        n_1_2 = 0
        n_1_3 = 0
        n_1_4 = 0
        n_1_5 = 0

        n_2_1 = 0
        n_2_2 = 0
        n_2_3 = 0
        n_2_4 = 0
        n_2_5 = 0

        n_3_1 = 0
        n_3_2 = 0
        n_3_3 = 0
        n_3_4 = 0
        n_3_5 = 0

        n_4_1 = 0
        n_4_2 = 0
        n_4_3 = 0
        n_4_4 = 0
        n_4_5 = 0

        n_5_1 = 0
        n_5_2 = 0
        n_5_3 = 0
        n_5_4 = 0
        n_5_5 = 0
        
        p_peyk = 0
        servis = 0

        total_price = 0
        total_num = 0

        #ziba sazie menu

        

        while True :
            a = 0
            for i in name_1_1 :
                a+=1
            if a < 30 :
                name_1_1 = name_1_1 +"."
            else :
                break

        while True :
            a = 0
            for i in name_1_2 :
                a+=1
            if a < 30 :
                name_1_2 = name_1_2 +"."
            else :
                break

        while True :
            a = 0
            for i in name_1_3 :
                a+=1
            if a < 30 :
                name_1_3 = name_1_3 +"."
            else :
                break

        while True :
            a = 0
            for i in name_1_4 :
                a+=1
            if a < 30 :
                name_1_4 = name_1_4 +"."
            else :
                break

        while True :
            a = 0
            for i in name_1_5 :
                a+=1
            if a < 30 :
                name_1_5 = name_1_5 +"."
            else :
                break
        
        

        while True :
            a = 0
            for i in name_2_1 :
                a+=1
            if a < 30 :
                name_2_1 = name_2_1 +"."
            else :
                break

        while True :
            a = 0
            for i in name_2_2 :
                a+=1
            if a < 30 :
                name_2_2 = name_2_2 +"."
            else :
                break

        while True :
            a = 0
            for i in name_2_3 :
                a+=1
            if a < 30 :
                name_2_3 = name_2_3 +"."
            else :
                break

        while True :
            a = 0
            for i in name_2_4 :
                a+=1
            if a < 30 :
                name_2_4 = name_2_4 +"."
            else :
                break

        while True :
            a = 0
            for i in name_2_5 :
                a+=1
            if a < 30 :
                name_2_5 = name_2_5 +"."
            else :
                break
        

        while True :
            a = 0
            for i in name_3_1 :
                a+=1
            if a < 30 :
                name_3_1 = name_3_1 +"."
            else :
                break

        while True :
            a = 0
            for i in name_3_2 :
                a+=1
            if a < 30 :
                name_3_2 = name_3_2 +"."
            else :
                break

        while True :
            a = 0
            for i in name_3_3 :
                a+=1
            if a < 30 :
                name_3_3 = name_3_3 +"."
            else :
                break

        while True :
            a = 0
            for i in name_3_4 :
                a+=1
            if a < 30 :
                name_3_4 = name_3_4 +"."
            else :
                break

        while True :
            a = 0
            for i in name_3_5 :
                a+=1
            if a < 30 :
                name_3_5 = name_3_5 +"."
            else :
                break
        

        while True :
            a = 0
            for i in name_4_1 :
                a+=1
            if a < 30 :
                name_4_1 = name_4_1 +"."
            else :
                break

        while True :
            a = 0
            for i in name_4_2 :
                a+=1
            if a < 30 :
                name_4_2 = name_4_2 +"."
            else :
                break

        while True :
            a = 0
            for i in name_4_3 :
                a+=1
            if a < 30 :
                name_4_3 = name_4_3 +"."
            else :
                break

        while True :
            a = 0
            for i in name_4_4 :
                a+=1
            if a < 30 :
                name_4_4 = name_4_4 +"."
            else :
                break

        while True :
            a = 0
            for i in name_4_5 :
                a+=1
            if a < 30 :
                name_4_5 = name_4_5 +"."
            else :
                break

        
        while True :
            a = 0
            for i in name_5_1 :
                a+=1
            if a < 30 :
                name_5_1 = name_5_1 +"."
            else :
                break

        while True :
            a = 0
            for i in name_5_2 :
                a+=1
            if a < 30 :
                name_5_2 = name_5_2 +"."
            else :
                break

        while True :
            a = 0
            for i in name_5_3 :
                a+=1
            if a < 30 :
                name_5_3 = name_5_3 +"."
            else :
                break

        while True :
            a = 0
            for i in name_5_4 :
                a+=1
            if a < 30 :
                name_5_4 = name_5_4 +"."
            else :
                break

        while True :
            a = 0
            for i in name_5_5 :
                a+=1
            if a < 30 :
                name_5_5 = name_5_5 +"."
            else :
                break

   
        order_exit = 0
        no_order = 0
        edite_exit = 0

        while True :

            print("\n" , "\n1.  " , sarfas_1.upper() ,"\n2.  ",sarfas_2.upper() ,"\n3.  ", sarfas_3.upper() , "\n4.  ",sarfas_4.upper() ,"\n5.  ", sarfas_5.upper() , "\n\n6. EDIT ORDER \n\n7. SOORAT HESAB \n\n0. EXIT_0_")
            menu = input()

            if menu == "0" :
                order_exit = 1
                break

            if menu == "7" :

                if total_num == 0 :
                    print("\nshoma sefaresh nadadid")
                    no_order = 1
                    break

                peyk = input("1.salon \n2.outdoor\n")

                match peyk :

                    case "1" :

                        servis = 1
                        p_peyk = 0
                        num_salon += 1

                    case "2" :
                        p_peyk = 1
                        servis = 0
                        num_peyk +=1

                    case _ :
                        print("just 1 or 2\n")

                break

            

            while True :

                match menu :

                    case "1" :
                        print("\n\n" , "1.",name_1_1 ,"..." ,p_1_1, "\n", "2.", name_1_2 ,"..." ,p_1_2, "\n", "3.", name_1_3 ,"..." ,p_1_3, "\n", "4.", name_1_4 ,"..." ,p_1_4, "\n", "5.", name_1_5 ,"..." ,p_1_5, "\n", "\n6.EDIT \n0.back to main menu\n")
                        choice = input()
                        
                        match choice :
                            case "1" :
                                order_num = num_1_1
                                order_n = n_1_1
                                price = p_1_1
                            case "2" :
                                order_num = num_1_2
                                order_n = n_1_2
                                price = p_1_2
                            case "3" :
                                order_num = num_1_3
                                order_n = n_1_3
                                price = p_1_3
                            case "4" :
                                order_num = num_1_4
                                order_n = n_1_4
                                price = p_1_4
                            case "5" :
                                order_num = num_1_5
                                order_n = n_1_5
                                price = p_1_5
                            case "6" :
                                while True :
                                    print("0.enseraf az eslah\nkodam sefaresh ra mikhahid eslah konid :")

                                    if num_1_1 > 0 :
                                        print(name_1_1, "...." ,num_1_1, " enter 1 " )
                                    if num_1_2 > 0 :
                                        print(name_1_2, "...." ,num_1_2, " enter 2 ")
                                    if num_1_3 > 0 :
                                        print(name_1_3, "...." ,num_1_3, " enter 3 ")
                                    if num_1_4 > 0 :
                                        print(name_1_4, "...." ,num_1_4, " enter 4 ")
                                    if num_1_5 > 0 :
                                        print(name_1_5, "...." ,num_1_5, " enter 5 ")
                                    
                                    edit_m = input()

                                    if edit_m == "0" :
                                        edite_exit = 1
                                        break

                                    print("0.enseraf az eslah\n che tedad az sefareshe khod ra mikhahid kam konid :\n")

                                    match edit_m :

                                        case "1" :
                                            number = n_1_1
                                            price = p_1_1
                                        case "2" :
                                            number = n_1_2
                                            price = p_1_2
                                        case "3" :
                                            number = n_1_3
                                            price = p_1_3
                                        case "4" :
                                            number = n_1_4
                                            price = p_1_4
                                        case "5" :
                                            number = n_1_5
                                            price = p_1_5
                                        case _ :
                                            break

                                    if number == 0 :
                                        break

                                    while True :
                                        low_num = input()
                                        if low_num == "0" :
                                            break
                                        if low_num.isdigit() :
                                            low_num = int(e1)
                                            if low_num > 0 and low_num <= number :
                                                number -= low_num
                                                total_num -= low_num
                                                total_price -= (low_num * price)
                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")

                                    match edit_m :

                                        case "1" :
                                            n_1_1 = number
                                        case "2" :
                                            n_1_2 = number
                                        case "3" :
                                            n_1_3 = number
                                        case "4" :
                                            n_1_4 = number
                                        case "5" :
                                            n_1_5 = number
                                            
                                    print("   sefareshe eslah shode shoma\n")

                                    if num_1_1 > 0 :
                                        print(name_1_1, "...." ,num_1_1, " adad " )
                                    if num_1_2 > 0 :
                                        print(name_1_2, "...." ,num_1_2, " adad ")
                                    if num_1_3 > 0 :
                                        print(name_1_3, "...." ,num_1_3, " adad ")
                                    if num_1_4 > 0 :
                                        print(name_1_4, "...." ,num_1_4, " adad ")
                                    if num_1_5 > 0 :
                                        print(name_1_5, "...." ,num_1_5, " adad ")
                                    print("eslahe jadidi darid : 1.yes 2.no va edame sefaresh")
                                    pasokh = input()
                                    match pasokh :
                                        case "1" :
                                            continue
                                        case _ :
                                            break
                            case _ :
                                break
                            
                        while True :

                            if edite_exit == 1 :
                                break

                            new_order = input("num of order : ")
                            if new_order.isdigit() :
                                order_n = int(new_order)
                                order_num = order_num + order_n
                                total_price = total_price + order_n * price
                                total_num = total_num + order_n
                                break
                            else :
                                print("vorodi bayad adad bashad")
                        
                        

                        match choice :

                            case "1" :
                                num_1_1 = order_num
                                n_1_1 = order_n
                                  
                            case "2" :
                                num_1_2 = order_num
                                n_1_2 = order_n

                            case "3" :
                                num_1_3 = order_num
                                n_1_2 = order_n

                            case "4" :
                                num_1_4 = order_num
                                n_1_2 = order_n                         

                            case "5" :
                                num_1_5 = order_num
                                n_1_2 = order_n
                        


                    case "2" :
                        print("\n\n" , "1.",name_2_1 ,"..." ,p_2_1, "\n", "2.", name_2_2 ,"..." ,p_2_2, "\n", "3.", name_2_3 ,"..." ,p_2_3, "\n", "4.", name_2_4 ,"..." ,p_2_4, "\n", "5.", name_2_5 ,"..." ,p_2_5, "\n", "\n6.EDIT \n0.back to main menu\n")
                        choice = input()
                            
                        match choice :
                            case "1" :
                                order_num = num_2_1
                                order_n = n_2_1
                                price = p_2_1
                            case "2" :
                                order_num = num_2_2
                                order_n = n_2_2
                                price = p_2_2
                            case "3" :
                                order_num = num_2_3
                                order_n = n_2_3
                                price = p_2_3
                            case "4" :
                                order_num = num_2_4
                                order_n = n_2_4
                                price = p_2_4
                            case "5" :
                                order_num = num_2_5
                                order_n = n_2_5
                                price = p_2_5
                            case "6" :
                                while True :
                                    print("0.enseraf az eslah\nkodam sefaresh ra mikhahid eslah konid :")

                                    if num_2_1 > 0 :
                                        print(name_2_1, "...." ,num_2_1, " enter 1 " )
                                    if num_2_2 > 0 :
                                        print(name_2_2, "...." ,num_2_2, " enter 2 ")
                                    if num_2_3 > 0 :
                                        print(name_2_3, "...." ,num_2_3, " enter 3 ")
                                    if num_2_4 > 0 :
                                        print(name_2_4, "...." ,num_2_4, " enter 4 ")
                                    if num_2_5 > 0 :
                                        print(name_2_5, "...." ,num_2_5, " enter 5 ")
                                    
                                    edit_m = input()

                                    if edit_m == "0" :
                                        edite_exit = 1
                                        break

                                    print("0.enseraf az eslah\n che tedad az sefareshe khod ra mikhahid kam konid :\n")

                                    match edit_m :

                                        case "1" :
                                            number = n_2_1
                                            price = p_2_1
                                        case "2" :
                                            number = n_2_2
                                            price = p_2_2
                                        case "3" :
                                            number = n_2_3
                                            price = p_2_3
                                        case "4" :
                                            number = n_2_4
                                            price = p_2_4
                                        case "5" :
                                            number = n_2_5
                                            price = p_2_5
                                        case _ :
                                            break

                                    if number == 0 :
                                        break

                                    while True :
                                        low_num = input()
                                        if low_num == "0" :
                                            break
                                        if low_num.isdigit() :
                                            low_num = int(e1)
                                            if low_num > 0 and low_num <= number :
                                                number -= low_num
                                                total_num -= low_num
                                                total_price -= (low_num * price)
                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")

                                    match edit_m :

                                        case "1" :
                                            n_2_1 = number
                                        case "2" :
                                            n_2_2 = number
                                        case "3" :
                                            n_2_3 = number
                                        case "4" :
                                            n_2_4 = number
                                        case "5" :
                                            n_2_5 = number
                                            
                                    print("   sefareshe eslah shode shoma\n")

                                    if num_2_1 > 0 :
                                        print(name_1_1, "...." ,num_2_1, " adad " )
                                    if num_2_2 > 0 :
                                        print(name_1_2, "...." ,num_2_2, " adad ")
                                    if num_2_3 > 0 :
                                        print(name_1_3, "...." ,num_2_3, " adad ")
                                    if num_2_4 > 0 :
                                        print(name_1_4, "...." ,num_2_4, " adad ")
                                    if num_2_5 > 0 :
                                        print(name_1_5, "...." ,num_2_5, " adad ")
                                    print("eslahe jadidi darid : 1.yes 2.no va edame sefaresh")
                                    pasokh = input()
                                    match pasokh :
                                        case "1" :
                                            continue
                                        case _ :
                                            break
                            case _ :
                                break

                        while True :

                            if edite_exit == 1 :
                                break

                            new_order = input("num of order : ")
                            if new_order.isdigit() :
                                order_n = int(new_order)
                                order_num = order_num + order_n
                                total_price = total_price + order_n * price
                                total_num = total_num + order_n
                                break
                            else :
                                print("vorodi bayad adad bashad")

                        match choice :

                            case "1" :
                                num_2_1 = order_num
                                n_2_1 = order_n
                                  
                            case "2" :
                                num_2_2 = order_num
                                n_2_2 = order_n

                            case "3" :
                                num_2_3 = order_num
                                n_2_3 = order_n

                            case "4" :
                                num_2_4 = order_num 
                                n_2_4 = order_n                        

                            case "5" :
                                num_2_5 = order_num
                                n_2_5 = order_n


                    case "3" :
                        print("\n\n" , "1.",name_3_1 ,"..." ,p_3_1, "\n", "2.", name_3_2 ,"..." ,p_3_2, "\n", "3.", name_3_3 ,"..." ,p_3_3, "\n", "4.", name_3_4 ,"..." ,p_3_4, "\n", "5.", name_3_5 ,"..." ,p_3_5, "\n", "\n6.EDIT \n0.back to main menu\n")
                        choice = input()

                        match choice :
                            case "1" :
                                order_num = num_3_1
                                order_n = n_3_1
                                price = p_3_1
                            case "2" :
                                order_num = num_3_2
                                order_n = n_3_2
                                price = p_3_2
                            case "3" :
                                order_num = num_3_3
                                order_n = n_3_3
                                price = p_3_3
                            case "4" :
                                order_num = num_3_4
                                order_n = n_3_4
                                price = p_3_4
                            case "5" :
                                order_num = num_3_5
                                order_n = n_3_5
                                price = p_3_5
                            case "6" :
                                while True :
                                    print("0.enseraf az eslah\nkodam sefaresh ra mikhahid eslah konid :")

                                    if num_3_1 > 0 :
                                        print(name_3_1, "...." ,num_3_1, " enter 1 " )
                                    if num_3_2 > 0 :
                                        print(name_3_2, "...." ,num_3_2, " enter 2 ")
                                    if num_3_3 > 0 :
                                        print(name_3_3, "...." ,num_3_3, " enter 3 ")
                                    if num_3_4 > 0 :
                                        print(name_3_4, "...." ,num_3_4, " enter 4 ")
                                    if num_3_5 > 0 :
                                        print(name_3_5, "...." ,num_3_5, " enter 5 ")
                                    
                                    edit_m = input()

                                    if edit_m == "0" :
                                        edite_exit = 1
                                        break

                                    print("0.enseraf az eslah\n che tedad az sefareshe khod ra mikhahid kam konid :\n")

                                    match edit_m :

                                        case "1" :
                                            number = n_3_1
                                            price = p_3_1
                                        case "2" :
                                            number = n_3_2
                                            price = p_3_2
                                        case "3" :
                                            number = n_3_3
                                            price = p_3_3
                                        case "4" :
                                            number = n_3_4
                                            price = p_3_4
                                        case "5" :
                                            number = n_3_5
                                            price = p_3_5
                                        case _ :
                                            break

                                    if number == 0 :
                                        break

                                    while True :
                                        low_num = input()
                                        if low_num == "0" :
                                            break
                                        if low_num.isdigit() :
                                            low_num = int(e1)
                                            if low_num > 0 and low_num <= number :
                                                number -= low_num
                                                total_num -= low_num
                                                total_price -= (low_num * price)
                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")

                                    match edit_m :

                                        case "1" :
                                            n_3_1 = number
                                        case "2" :
                                            n_3_2 = number
                                        case "3" :
                                            n_3_3 = number
                                        case "4" :
                                            n_3_4 = number
                                        case "5" :
                                            n_3_5 = number
                                            
                                    print("   sefareshe eslah shode shoma\n")

                                    if num_3_1 > 0 :
                                        print(name_3_1, "...." ,num_3_1, " adad " )
                                    if num_3_2 > 0 :
                                        print(name_3_2, "...." ,num_3_2, " adad ")
                                    if num_3_3 > 0 :
                                        print(name_3_3, "...." ,num_3_3, " adad ")
                                    if num_3_4 > 0 :
                                        print(name_3_4, "...." ,num_3_4, " adad ")
                                    if num_3_5 > 0 :
                                        print(name_3_5, "...." ,num_3_5, " adad ")
                                    print("eslahe jadidi darid : 1.yes 2.no va edame sefaresh")
                                    pasokh = input()
                                    match pasokh :
                                        case "1" :
                                            continue
                                        case _ :
                                            break
                            case _ :
                                break

                        while True :

                            if edite_exit == 1 :
                                break
                            new_order = input("num of order : ")
                            if new_order.isdigit() :
                                order_n = int(new_order)
                                order_num = order_num + order_n
                                total_price = total_price + order_n * price
                                total_num = total_num + order_n
                                break
                            else :
                                print("vorodi bayad adad bashad")

                        match choice :

                            case "1" :
                                num_3_1 = order_num
                                n_3_1 = order_n
                                  
                            case "2" :
                                num_3_2 = order_num
                                n_3_2 = order_n

                            case "3" :
                                num_3_3 = order_num
                                n_3_3 = order_n

                            case "4" :
                                num_3_4 = order_num   
                                n_3_4 = order_n                      

                            case "5" :
                                num_3_5 = order_num
                                n_3_5 = order_n

                    case "4" :
                        print("\n\n" , "1.",name_4_1 ,"..." ,p_4_1, "\n", "2.", name_4_2 ,"..." ,p_4_2, "\n", "3.", name_4_3 ,"..." ,p_4_3, "\n", "4.", name_4_4 ,"..." ,p_4_4, "\n", "5.", name_4_5 ,"..." ,p_4_5, "\n", "\n6.EDIT \n0.back to main menu\n")
                        choice = input()

                        match choice :
                            case "1" :
                                order_num = num_4_1
                                order_n = n_4_1
                                price = p_4_1
                            case "2" :
                                order_num = num_4_2
                                order_n = n_4_2
                                price = p_4_2
                            case "3" :
                                order_num = num_4_3
                                order_n = n_4_3
                                price = p_4_3
                            case "4" :
                                order_num = num_4_4
                                order_n = n_4_4
                                price = p_4_4
                            case "5" :
                                order_num = num_4_5
                                order_n = n_4_5
                                price = p_4_5
                            case "6" :
                                while True :
                                    print("0.enseraf az eslah\nkodam sefaresh ra mikhahid eslah konid :")

                                    if num_4_1 > 0 :
                                        print(name_4_1, "...." ,num_4_1, " enter 1 " )
                                    if num_4_2 > 0 :
                                        print(name_4_2, "...." ,num_4_2, " enter 2 ")
                                    if num_4_3 > 0 :
                                        print(name_4_3, "...." ,num_4_3, " enter 3 ")
                                    if num_4_4 > 0 :
                                        print(name_4_4, "...." ,num_4_4, " enter 4 ")
                                    if num_4_5 > 0 :
                                        print(name_4_5, "...." ,num_4_5, " enter 5 ")
                                    
                                    edit_m = input()

                                    if edit_m == "0" :
                                        edite_exit = 1
                                        break

                                    print("0.enseraf az eslah\n che tedad az sefareshe khod ra mikhahid kam konid :\n")

                                    match edit_m :

                                        case "1" :
                                            number = n_4_1
                                            price = p_4_1
                                        case "2" :
                                            number = n_4_2
                                            price = p_4_2
                                        case "3" :
                                            number = n_4_3
                                            price = p_4_3
                                        case "4" :
                                            number = n_4_4
                                            price = p_4_4
                                        case "5" :
                                            number = n_4_5
                                            price = p_4_5
                                        case _ :
                                            break

                                    if number == 0 :
                                        break

                                    while True :
                                        low_num = input()
                                        if low_num == "0" :
                                            break
                                        if low_num.isdigit() :
                                            low_num = int(e1)
                                            if low_num > 0 and low_num <= number :
                                                number -= low_num
                                                total_num -= low_num
                                                total_price -= (low_num * price)
                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")

                                    match edit_m :

                                        case "1" :
                                            n_4_1 = number
                                        case "2" :
                                            n_4_2 = number
                                        case "3" :
                                            n_4_3 = number
                                        case "4" :
                                            n_4_4 = number
                                        case "5" :
                                            n_4_5 = number
                                            
                                    print("   sefareshe eslah shode shoma\n")

                                    if num_4_1 > 0 :
                                        print(name_4_1, "...." ,num_4_1, " adad " )
                                    if num_4_2 > 0 :
                                        print(name_4_2, "...." ,num_4_2, " adad ")
                                    if num_4_3 > 0 :
                                        print(name_4_3, "...." ,num_4_3, " adad ")
                                    if num_4_4 > 0 :
                                        print(name_4_4, "...." ,num_4_4, " adad ")
                                    if num_4_5 > 0 :
                                        print(name_4_5, "...." ,num_4_5, " adad ")
                                    print("eslahe jadidi darid : 1.yes 2.no va edame sefaresh")
                                    pasokh = input()
                                    match pasokh :
                                        case "1" :
                                            continue
                                        case _ :
                                            break
                            case _ :
                                break

                        while True :

                            if edite_exit == 1 :
                                break

                            new_order = input("num of order : ")
                            if new_order.isdigit() :
                                order_n = int(new_order)
                                order_num = order_num + order_n
                                total_price = total_price + order_n * price
                                total_num = total_num + order_n
                                break
                            else :
                                print("vorodi bayad adad bashad")

                        match choice :

                            case "1" :
                                num_4_1 = order_num
                                n_4_1 = order_n
                                  
                            case "2" :
                                num_4_2 = order_num
                                n_4_2 = order_n

                            case "3" :
                                num_4_3 = order_num
                                n_4_3 = order_n

                            case "4" :
                                num_4_4 = order_num  
                                n_4_4 = order_n                       

                            case "5" :
                                num_4_5 = order_num
                                n_4_5 = order_n


                    case "5" :
                        print("\n\n" , "1.",name_5_1 ,"..." ,p_5_1, "\n", "2.", name_5_2 ,"..." ,p_5_2, "\n", "3.", name_5_3 ,"..." ,p_5_3, "\n", "4.", name_5_4 ,"..." ,p_5_4, "\n", "5.", name_5_5 ,"..." ,p_5_5, "\n", "\n6.EDIT \n0.back to main menu\n")
                        choice = input()

                        match choice :
                            case "1" :
                                order_num = num_5_1
                                order_n = n_5_1
                                price = p_5_1
                            case "2" :
                                order_num = num_5_2
                                order_n = n_5_2
                                price = p_5_2
                            case "3" :
                                order_num = num_5_3
                                order_n = n_5_3
                                price = p_5_3
                            case "4" :
                                order_num = num_5_4
                                order_n = n_5_4
                                price = p_5_4
                            case "5" :
                                order_num = num_5_5
                                order_n = n_5_5
                                price = p_5_5
                            case "6" :
                                while True :
                                    print("0.enseraf az eslah\nkodam sefaresh ra mikhahid eslah konid :")

                                    if num_5_1 > 0 :
                                        print(name_5_1, "...." ,num_5_1, " enter 1 " )
                                    if num_5_2 > 0 :
                                        print(name_5_2, "...." ,num_5_2, " enter 2 ")
                                    if num_5_3 > 0 :
                                        print(name_5_3, "...." ,num_5_3, " enter 3 ")
                                    if num_5_4 > 0 :
                                        print(name_5_4, "...." ,num_5_4, " enter 4 ")
                                    if num_5_5 > 0 :
                                        print(name_5_5, "...." ,num_5_5, " enter 5 ")
                                    
                                    edit_m = input()

                                    if edit_m == "0" :
                                        edite_exit = 1
                                        break

                                    print("0.enseraf az eslah\n che tedad az sefareshe khod ra mikhahid kam konid :\n")

                                    match edit_m :

                                        case "1" :
                                            number = n_5_1
                                            price = p_5_1
                                        case "2" :
                                            number = n_5_2
                                            price = p_5_2
                                        case "3" :
                                            number = n_5_3
                                            price = p_5_3
                                        case "4" :
                                            number = n_5_4
                                            price = p_5_4
                                        case "5" :
                                            number = n_5_5
                                            price = p_5_5
                                        case _ :
                                            break

                                    if number == 0 :
                                        break

                                    while True :
                                        low_num = input()
                                        if low_num == "0" :
                                            break
                                        if low_num.isdigit() :
                                            low_num = int(e1)
                                            if low_num > 0 and low_num <= number :
                                                number -= low_num
                                                total_num -= low_num
                                                total_price -= (low_num * price)
                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")

                                    match edit_m :

                                        case "1" :
                                            n_5_1 = number
                                        case "2" :
                                            n_5_2 = number
                                        case "3" :
                                            n_5_3 = number
                                        case "4" :
                                            n_5_4 = number
                                        case "5" :
                                            n_5_5 = number
                                            
                                    print("   sefareshe eslah shode shoma\n")

                                    if num_5_1 > 0 :
                                        print(name_5_1, "...." ,num_5_1, " adad " )
                                    if num_5_2 > 0 :
                                        print(name_5_2, "...." ,num_5_2, " adad ")
                                    if num_5_3 > 0 :
                                        print(name_5_3, "...." ,num_5_3, " adad ")
                                    if num_5_4 > 0 :
                                        print(name_5_4, "...." ,num_5_4, " adad ")
                                    if num_5_5 > 0 :
                                        print(name_5_5, "...." ,num_5_5, " adad ")
                                    print("eslahe jadidi darid : 1.yes 2.no va edame sefaresh")
                                    pasokh = input()
                                    match pasokh :
                                        case "1" :
                                            continue
                                        case _ :
                                            break
                            case _ :
                                break

                        while True :

                            if edite_exit == 1 :
                                break
                            
                            new_order = input("num of order : ")
                            if new_order.isdigit() :
                                order_n = int(new_order)
                                order_num = order_num + order_n
                                total_price = total_price + order_n * price
                                total_num = total_num + order_n
                                break
                            else :
                                print("vorodi bayad adad bashad")

                        match choice :

                            case "1" :
                                num_5_1 = order_num
                                n_5_1 = order_n
                                  
                            case "2" :
                                num_5_2 = order_num
                                n_5_2 = order_n


                            case "3" :
                                num_5_3 = order_num
                                n_5_3 = order_n

                            case "4" :
                                num_5_4 = order_num  
                                n_5_4 = order_n                       

                            case "5" :
                                num_5_5 = order_num
                                n_5_5 = order_n

                    case "6" :

                        while True :

                            sh = 0
                    
                            print("0.enseraf az eslah\nkodam sefaresh ra mikhahid eslah konid :")
                            if num_1_1 > 0 :
                                sh += 1
                                print(sh, "." ,name_1_1, "...." ,num_1_1, " enter 1 " )
                            if num_1_2 > 0 :
                                sh += 1
                                print(sh, "." ,name_1_2, "...." ,num_1_2, " enter 2 " )                               
                            if num_1_3 > 0 :
                                sh += 1
                                print(sh, "." ,name_1_3, "...." ,num_1_3, " enter 3 " )                               
                            if num_1_4 > 0 :
                                sh += 1
                                print(sh, "." ,name_1_4, "...." ,num_1_4, " enter 4 " )
                            if num_1_5 > 0 :
                                sh += 1
                                print(sh, "." ,name_1_5, "...." ,num_1_5, " enter 5 " )
                                

                            if num_2_1 > 0 :
                                sh += 1
                                print(sh, "." ,name_2_1, "...." ,num_2_1, " enter 6 " )
                            if num_2_2 > 0 :
                                sh += 1
                                print(sh, "." ,name_2_2, "...." ,num_2_2, " enter 7 ")
                            if num_2_3 > 0 :
                                sh += 1
                                print(sh, "." ,name_2_3, "...." ,num_2_3, " enter 8 ")
                            if num_2_4 > 0 :
                                sh += 1
                                print(sh, "." ,name_2_4, "...." ,num_2_4, " enter 9 ")
                            if num_2_5 > 0 :
                                sh += 1
                                print(sh, "." ,name_2_5, "...." ,num_2_5, " enter 10 ")


                            if num_3_1 > 0 :
                                sh += 1
                                print(sh, "." ,name_3_1, "...." ,num_3_1, " enter 11 " )
                            if num_3_2 > 0 :
                                sh += 1
                                print(sh, "." ,name_3_2, "...." ,num_3_2, " enter 12 ")
                            if num_3_3 > 0 :
                                sh += 1
                                print(sh, "." ,name_3_3, "...." ,num_3_3, " enter 13 ")
                            if num_3_4 > 0 :
                                sh += 1
                                print(sh, "." ,name_3_4, "...." ,num_3_4, " enter 14 ")
                            if num_3_5 > 0 :
                                sh += 1
                                print(sh, "." ,name_3_5, "...." ,num_3_5, " enter 15 ")

                            if num_4_1 > 0 :
                                sh += 1
                                print(sh, "." ,name_4_1, "...." ,num_4_1, " enter 16 " )
                            if num_4_2 > 0 :
                                sh += 1
                                print(sh, "." ,name_4_2, "...." ,num_4_2, " enter 17 ")
                            if num_4_3 > 0 :
                                sh += 1
                                print(sh, "." ,name_4_3, "...." ,num_4_3, " enter 18 ")
                            if num_4_4 > 0 :
                                sh += 1
                                print(sh, "." ,name_4_4, "...." ,num_4_4, " enter 19 ")
                            if num_4_5 > 0 :
                                sh += 1
                                print(sh, "." ,name_4_5, "...." ,num_4_5, " enter 20 ")

                            if num_5_1 > 0 :
                                sh += 1
                                print(sh, "." ,name_5_1, "...." ,num_5_1, " enter 21 " )
                            if num_5_2 > 0 :
                                sh += 1
                                print(sh, "." ,name_5_2, "...." ,num_5_2, " enter 22 ")
                            if num_5_3 > 0 :
                                sh += 1
                                print(sh, "." ,name_5_3, "...." ,num_5_3, " enter 23 ")
                            if num_5_4 > 0 :
                                sh += 1
                                print(sh, "." ,name_5_4, "...." ,num_5_4, " enter 24 ")
                            if num_5_5 > 0 :
                                sh += 1
                                print(sh, "." ,name_5_5, "...." ,num_5_5, " enter 25 ")
                            
                            edit_m = input()

                            if edit_m == "0" :
                                break

                            print("0.enseraf az eslah\n che tedad az sefareshe khod ra mikhahid kam konid :\n")

                            match edit_m :

                                case "1" :
                                    number = n_1_1
                                    price = p_1_1
                                case "2" :
                                    number = n_1_2
                                    price = p_1_2
                                case "3" :
                                    number = n_1_3
                                    price = p_1_3
                                case "4" :
                                    number = n_1_4
                                    price = p_1_4
                                case "5" :
                                    number = n_1_5
                                    price = p_1_5
                                case "6" :
                                    number = n_2_1
                                    price = p_2_1
                                case "7" :
                                    number = n_2_2
                                    price = p_2_2
                                case "8" :
                                    number = n_2_3
                                    price = p_2_3
                                case "9" :
                                    number = n_2_4
                                    price = p_2_4
                                case "10" :
                                    number = n_2_5
                                    price = p_2_5
                                case "11" :
                                    number = n_3_1
                                    price = p_3_1
                                case "12" :
                                    number = n_3_2
                                    price = p_3_2
                                case "13" :
                                    number = n_3_3
                                    price = p_3_3
                                case "14" :
                                    number = n_3_4
                                    price = p_3_4
                                case "15" :
                                    number = n_3_5
                                    price = p_3_5
                                case "16" :
                                    number = n_4_1
                                    price = p_4_1
                                case "17" :
                                    number = n_4_2
                                    price = p_4_2
                                case "18" :
                                    number = n_4_3
                                    price = p_4_3
                                case "19" :
                                    number = n_4_4
                                    price = p_4_4
                                case "20" :
                                    number = n_4_5
                                    price = p_4_5
                                case "21" :
                                    number = n_5_1
                                    price = p_5_1
                                case "22" :
                                    number = n_5_2
                                    price = p_5_2
                                case "23" :
                                    number = n_5_3
                                    price = p_5_3
                                case "24" :
                                    number = n_5_4
                                    price = p_5_4
                                case "25" :
                                    number = n_5_5
                                    price = p_5_5


                            if number == 0 :
                                break

                            while True :
                                low_num = input()
                                if low_num == "0" :
                                    break
                                if low_num.isdigit() :
                                    low_num = int(e1)
                                    if low_num > 0 and low_num <= number :
                                        number -= low_num
                                        total_num -= low_num
                                        total_price -= (low_num * price)
                                        break
                                    else :
                                        print("vorodi sahih nist")
                                else :
                                    print("vorodi bayad adad bashad")

                            match edit_m :

                                case "1" :
                                    n_1_1 = number
                                case "2" :
                                    n_1_2 = number
                                case "3" :
                                    n_1_3 = number
                                case "4" :
                                    n_1_4 = number
                                case "5" :
                                    n_1_5 = number
                                case "6" :
                                    n_2_1 = number
                                case "7" :
                                    n_2_2 = number
                                case "8" :
                                    n_2_3 = number
                                case "9" :
                                    n_2_4 = number
                                case "10" :
                                    n_2_5 = number
                                case "11" :
                                    n_3_1 = number
                                case "12" :
                                    n_3_2 = number
                                case "13" :
                                    n_3_3 = number
                                case "14" :
                                    n_3_4 = number
                                case "15" :
                                    n_3_5 = number
                                case "16" :
                                    n_4_1 = number
                                case "17" :
                                    n_4_2 = number
                                case "18" :
                                    n_4_3 = number
                                case "19" :
                                    n_4_4 = number
                                case "20" :
                                    n_4_5 = number
                                case "21" :
                                    n_5_1 = number
                                case "22" :
                                    n_5_2 = number
                                case "23" :
                                    n_5_3 = number
                                case "24" :
                                    n_5_4 = number
                                case "25" :
                                    n_5_5 = number

                            print("   sefareshe eslah shode shoma\n")

                            if num_1_1 > 0 :
                                print(name_1_1, "...." ,num_1_1, " adad " )
                            if num_1_2 > 0 :
                                print(name_1_2, "...." ,num_1_2, " adad ")
                            if num_1_3 > 0 :
                                print(name_1_3, "...." ,num_1_3, " adad ")
                            if num_1_4 > 0 :
                                print(name_1_4, "...." ,num_1_4, " adad ")
                            if num_1_5 > 0 :
                                print(name_1_5, "...." ,num_1_5, " adad ")


                            if num_2_1 > 0 :
                                print(name_2_1, "...." ,num_2_1, " adad " )
                            if num_2_2 > 0 :
                                print(name_2_2, "...." ,num_2_2, " adad ")
                            if num_2_3 > 0 :
                                print(name_2_3, "...." ,num_2_3, " adad ")
                            if num_2_4 > 0 :
                                print(name_2_4, "...." ,num_2_4, " adad ")
                            if num_2_5 > 0 :
                                print(name_2_5, "...." ,num_2_5, " adad ")


                            if num_3_1 > 0 :
                                print(name_3_1, "...." ,num_3_1, " adad " )
                            if num_3_2 > 0 :
                                print(name_3_2, "...." ,num_3_2, " adad ")
                            if num_3_3 > 0 :
                                print(name_3_3, "...." ,num_3_3, " adad ")
                            if num_3_4 > 0 :
                                print(name_3_4, "...." ,num_3_4, " adad ")
                            if num_3_5 > 0 :
                                print(name_3_5, "...." ,num_3_5, " adad ")

                            if num_4_1 > 0 :
                                print(name_4_1, "...." ,num_4_1, " adad " )
                            if num_4_2 > 0 :
                                print(name_4_2, "...." ,num_4_2, " adad ")
                            if num_4_3 > 0 :
                                print(name_4_3, "...." ,num_4_3, " adad ")
                            if num_4_4 > 0 :
                                print(name_4_4, "...." ,num_4_4, " adad ")
                            if num_4_5 > 0 :
                                print(name_4_5, "...." ,num_4_5, " adad ")

                            if num_5_1 > 0 :
                                print(name_5_1, "...." ,num_5_1, " adad " )
                            if num_5_2 > 0 :
                                print(name_5_2, "...." ,num_5_2, " adad ")
                            if num_5_3 > 0 :
                                print(name_5_3, "...." ,num_5_3, " adad ")
                            if num_5_4 > 0 :
                                print(name_5_4, "...." ,num_5_4, " adad ")
                            if num_5_5 > 0 :
                                print(name_5_5, "...." ,num_5_5, " adad ")

                            print("eslahe jadidi darid : 1.yes 2.no va edame sefaresh")
                            pasokh = input()
                            match pasokh :
                                case "1" :
                                    continue
                                case _ :
                                    break
                            break

                    case _ :
                        break
                        

                print("   sefareshe shoma ta konon\n")

                if num_1_1 > 0 :
                    print(name_1_1, "...." ,num_1_1, " adad " )
                if num_1_2 > 0 :
                    print(name_1_2, "...." ,num_1_2, " adad ")
                if num_1_3 > 0 :
                    print(name_1_3, "...." ,num_1_3, " adad ")
                if num_1_4 > 0 :
                    print(name_1_4, "...." ,num_1_4, " adad ")
                if num_1_5 > 0 :
                    print(name_1_5, "...." ,num_1_5, " adad ")


                if num_2_1 > 0 :
                    print(name_2_1, "...." ,num_2_1, " adad " )
                if num_2_2 > 0 :
                    print(name_2_2, "...." ,num_2_2, " adad ")
                if num_2_3 > 0 :
                    print(name_2_3, "...." ,num_2_3, " adad ")
                if num_2_4 > 0 :
                    print(name_2_4, "...." ,num_2_4, " adad ")
                if num_2_5 > 0 :
                    print(name_2_5, "...." ,num_2_5, " adad ")


                if num_3_1 > 0 :
                    print(name_3_1, "...." ,num_3_1, " adad " )
                if num_3_2 > 0 :
                    print(name_3_2, "...." ,num_3_2, " adad ")
                if num_3_3 > 0 :
                    print(name_3_3, "...." ,num_3_3, " adad ")
                if num_3_4 > 0 :
                    print(name_3_4, "...." ,num_3_4, " adad ")
                if num_3_5 > 0 :
                    print(name_3_5, "...." ,num_3_5, " adad ")

                if num_4_1 > 0 :
                    print(name_4_1, "...." ,num_4_1, " adad " )
                if num_4_2 > 0 :
                    print(name_4_2, "...." ,num_4_2, " adad ")
                if num_4_3 > 0 :
                    print(name_4_3, "...." ,num_4_3, " adad ")
                if num_4_4 > 0 :
                    print(name_4_4, "...." ,num_4_4, " adad ")
                if num_4_5 > 0 :
                    print(name_4_5, "...." ,num_4_5, " adad ")

                if num_5_1 > 0 :
                    print(name_5_1, "...." ,num_5_1, " adad " )
                if num_5_2 > 0 :
                    print(name_5_2, "...." ,num_5_2, " adad ")
                if num_5_3 > 0 :
                    print(name_5_3, "...." ,num_5_3, " adad ")
                if num_5_4 > 0 :
                    print(name_5_4, "...." ,num_5_4, " adad ")
                if num_5_5 > 0 :
                    print(name_5_5, "...." ,num_5_5, " adad ")


        if no_order == 1 :
            break
                 
        if order_exit == 1 :
            break

        
        print ("\n     *** soorat hesab ***\n")    
            
        if num_1_1 > 0 :
            print(name_1_1, "...." ,num_1_1, " adad ", num_1_1 * p_1_1 )
        if num_1_2 > 0 :
            print(name_1_2, "...." ,num_1_2, " adad ", num_1_2 * p_1_2)
        if num_1_3 > 0 :
            print(name_1_3, "...." ,num_1_3, " adad ", num_1_3 * p_1_3)
        if num_1_4 > 0 :
            print(name_1_4, "...." ,num_1_4, " adad ", num_1_4 * p_1_4)
        if num_1_5 > 0 :
            print(name_1_5, "...." ,num_1_5, " adad ", num_1_5 * p_1_5)


        if num_2_1 > 0 :
            print(name_2_1, "...." ,num_2_1, " adad ", num_2_1 * p_2_1 )
        if num_2_2 > 0 :
            print(name_2_2, "...." ,num_2_2, " adad ", num_2_2 * p_2_2 )
        if num_2_3 > 0 :
            print(name_2_3, "...." ,num_2_3, " adad ", num_2_3 * p_2_3 )
        if num_2_4 > 0 :
            print(name_2_4, "...." ,num_2_4, " adad ", num_2_4 * p_2_4 )
        if num_2_5 > 0 :
            print(name_2_5, "...." ,num_2_5, " adad ", num_2_5 * p_2_5 )


        if num_3_1 > 0 :
            print(name_3_1, "...." ,num_3_1, " adad ", num_3_1 * p_3_1  )
        if num_3_2 > 0 :
            print(name_3_2, "...." ,num_3_2, " adad ", num_3_2 * p_3_2 )
        if num_3_3 > 0 :
            print(name_3_3, "...." ,num_3_3, " adad ", num_3_3 * p_3_3 )
        if num_3_4 > 0 :
            print(name_3_4, "...." ,num_3_4, " adad ", num_3_4 * p_3_4 )
        if num_3_5 > 0 :
            print(name_3_5, "...." ,num_3_5, " adad ", num_3_5 * p_3_5 )

        if num_4_1 > 0 :
            print(name_4_1, "...." ,num_4_1, " adad ", num_4_1 * p_4_1  )
        if num_4_2 > 0 :
            print(name_4_2, "...." ,num_4_2, " adad ", num_4_2 * p_4_2 )
        if num_4_3 > 0 :
            print(name_4_3, "...." ,num_4_3, " adad ", num_4_3 * p_4_3 )
        if num_4_4 > 0 :
            print(name_4_4, "...." ,num_4_4, " adad ", num_4_4 * p_4_4 )
        if num_4_5 > 0 :
            print(name_4_5, "...." ,num_4_5, " adad ", num_4_5 * p_4_5 )

        if num_5_1 > 0 :
            print(name_5_1, "...." ,num_5_1, " adad ", num_5_1 * p_5_1  )
        if num_5_2 > 0 :
            print(name_5_2, "...." ,num_5_2, " adad ", num_5_2 * p_5_2 )
        if num_5_3 > 0 :
            print(name_5_3, "...." ,num_5_3, " adad ", num_5_3 * p_5_3 )
        if num_5_4 > 0 :
            print(name_5_4, "...." ,num_5_4, " adad ", num_5_4 * p_5_4 )
        if num_5_5 > 0 :
            print(name_5_5, "...." ,num_5_5, " adad ", num_5_5 * p_5_5 )
                
            
        print("majmoo..............." ,total_num, " adad ", total_price)
        if servis > 0 :    
            print("servis..................." , int(total_price*d_servis/100))
            servis = total_price*d_servis
            s_peyk = 0
        if p_peyk > 0 :

            if total_num > 20 or total_price > 3000000 :
                print("...*** ersal rayegan ***...")
                s_peyk = 0
            else :
                print("hazine ersal.................." , s_peyk)

        tax = total_price*d_tax
        print("tax......................." , int(tax))

        total_price = total_price  +  tax + servis + s_peyk

        print("\nmablaghe ghabele pardakht ....." , int(total_price))

        ex_co = input("\n1.sefareshe dobare \n2.khoroj \n")

        match ex_co :
            case "1" :
                continue
            case _ :
                print("thank you bye")
                break
    
    if program_exit == 1 :
        break


    #gozaresh

    #majmooe forosh

    total_forosh += total_price

    #tedade forosh kol

    tedad_factor +=1

    total_num_forosh += total_num

    #tedade foroshe har mahsool

    total_num_1_1 += num_1_1
    total_num_1_2 += num_1_2
    total_num_1_3 += num_1_3
    total_num_1_4 += num_1_4
    total_num_1_5 += num_1_5

    total_num_2_1 += num_2_1
    total_num_2_2 += num_2_2
    total_num_2_3 += num_2_3
    total_num_2_4 += num_2_4
    total_num_2_5 += num_2_5

    total_num_3_1 += num_3_1
    total_num_3_2 += num_3_2
    total_num_3_3 += num_3_3
    total_num_3_4 += num_3_4
    total_num_3_5 += num_3_5

    total_num_4_1 += num_4_1
    total_num_4_2 += num_4_2
    total_num_4_3 += num_4_3
    total_num_4_4 += num_4_4
    total_num_4_5 += num_4_5

    total_num_5_1 += num_5_1
    total_num_5_2 += num_5_2
    total_num_5_3 += num_5_3
    total_num_5_4 += num_5_4
    total_num_5_5 += num_5_5

#daramde hasel az har mahsool

    total_sell_1_1 += p_1_1 * num_1_1 
    total_sell_1_2 += p_1_2 * num_1_2 
    total_sell_1_3 += p_1_3 * num_1_3 
    total_sell_1_4 += p_1_4 * num_1_4 
    total_sell_1_5 += p_1_5 * num_1_5 

    total_sell_2_1 += p_2_1 * num_2_1 
    total_sell_2_2 += p_2_2 * num_2_2 
    total_sell_2_3 += p_2_3 * num_2_3 
    total_sell_2_4 += p_2_4 * num_2_4 
    total_sell_2_5 += p_2_5 * num_2_5 

    total_sell_3_1 += p_3_1 * num_3_1 
    total_sell_3_2 += p_3_2 * num_3_2 
    total_sell_3_3 += p_3_3 * num_3_3 
    total_sell_3_4 += p_3_4 * num_3_4 
    total_sell_3_5 += p_3_5 * num_3_5 

    total_sell_4_1 += p_4_1 * num_4_1 
    total_sell_4_2 += p_4_2 * num_4_2 
    total_sell_4_3 += p_4_3 * num_4_3 
    total_sell_4_4 += p_4_4 * num_4_4 
    total_sell_4_5 += p_4_5 * num_4_5 

    total_sell_5_1 += p_5_1 * num_5_1 
    total_sell_5_2 += p_5_2 * num_5_2 
    total_sell_5_3 += p_5_3 * num_5_3 
    total_sell_5_4 += p_5_4 * num_5_4 
    total_sell_5_5 += p_5_5 * num_5_5


    #por tarafdar tarin mahsol

    por_forosh_1 = total_num_1_1
    por_forosh_name_1 = name_1_1


    if total_num_1_2 > por_forosh_1 :
        por_forosh_1 = total_num_1_2
        por_forosh_name_1 = name_1_2

    if total_num_1_3 > por_forosh_1 :
        por_forosh_1 = total_num_1_3
        por_forosh_name_1 = name_1_3

    if total_num_1_4 > por_forosh_1 :
        por_forosh_1 = total_num_1_4
        por_forosh_name_1 = name_1_4

    if total_num_1_5 > por_forosh_1 :
        por_forosh_1 = total_num_1_5
        por_forosh_name_1 = name_1_5

    por_forosh_2 = total_num_2_1
    por_forosh_name_2 = name_2_1

    if total_num_2_2 > por_forosh_2 :
        por_forosh_2 = total_num_2_2
        por_forosh_name_2 = name_2_2

    if total_num_2_3 > por_forosh_2 :
        por_forosh_2 = total_num_2_3
        por_forosh_name_2 = name_2_3

    if total_num_2_4 > por_forosh_2 :
        por_forosh_2 = total_num_2_4
        por_forosh_name_2 = name_2_4

    if total_num_2_5 > por_forosh_2 :
        por_forosh_2 = total_num_2_5
        por_forosh_name_2 = name_2_5

    por_forosh_3 = total_num_3_1
    por_forosh_name_3 = name_3_1
    
    if total_num_3_2 > por_forosh_3 :
        por_forosh_3 = total_num_3_2
        por_forosh_name_3 = name_3_2

    if total_num_3_3 > por_forosh_3 :
        por_forosh_3 = total_num_3_3
        por_forosh_name_3 = name_3_3

    if total_num_3_4 > por_forosh_3 :
        por_forosh_3 = total_num_3_4
        por_forosh_name_3 = name_3_4

    if total_num_3_5 > por_forosh_3 :
        por_forosh_3 = total_num_3_5
        por_forosh_name_3 = name_3_5

    por_forosh_4 = total_num_4_1
    por_forosh_name_4 = name_4_1
    
    if total_num_4_2 > por_forosh_4 :
        por_forosh_4 = total_num_4_2
        por_forosh_name_4 = name_4_2

    if total_num_4_3 > por_forosh_4 :
        por_forosh_4 = total_num_4_3
        por_forosh_name_4 = name_4_3

    if total_num_4_4 > por_forosh_4 :
        por_forosh_4 = total_num_4_4
        por_forosh_name_4 = name_4_4

    if total_num_4_5 > por_forosh_4 :
        por_forosh_4 = total_num_4_5
        por_forosh_name_4 = name_4_5

    por_forosh_5 = total_num_5_1
    por_forosh_name_5 = name_5_1
    
    if total_num_5_2 > por_forosh_5 :
        por_forosh_5 = total_num_5_2
        por_forosh_name_5 = name_5_2

    if total_num_5_3 > por_forosh_5 :
        por_forosh_5 = total_num_5_3
        por_forosh_name_5 = name_5_3

    if total_num_5_4 > por_forosh_5 :
        por_forosh_5 = total_num_5_4
        por_forosh_name_5 = name_5_4

    if total_num_5_5 > por_forosh_5 :
        por_forosh_5 = total_num_5_5
        por_forosh_name_5 = name_5_5


    total_por_forosh = por_forosh_1
    total_por_forosh_name = por_forosh_name_1

    if por_forosh_2 > total_por_forosh :
        total_por_forosh = por_forosh_2
        total_por_forosh_name = por_forosh_name_2
    if por_forosh_3 > total_por_forosh :
        total_por_forosh = por_forosh_3
        total_por_forosh_name = por_forosh_name_3
    if por_forosh_4 > total_por_forosh :
        total_por_forosh = por_forosh_4
        total_por_forosh_name = por_forosh_name_4
    if por_forosh_5 > total_por_forosh :
        total_por_forosh = por_forosh_5
        total_por_forosh_name = por_forosh_name_5


        #kam tarafdar tarin mahsool


        kam_forosh_1 = total_num_1_1
        kam_forosh_name_1 = name_1_1
        total_kam_forosh = total_num_1_1

        if total_num_1_2 < kam_forosh_1 :
            kam_forosh_1 = total_num_1_2
            kam_forosh_name_1 = name_1_2

        if total_num_1_3 < kam_forosh_1 :
            kam_forosh_1 = total_num_1_3
            kam_forosh_name_1 = name_1_3

        if total_num_1_4 < kam_forosh_1 :
            kam_forosh_1 = total_num_1_4
            kam_forosh_name_1 = name_1_4

        if total_num_1_5 < kam_forosh_1 :
            kam_forosh_1 = total_num_1_5
            kam_forosh_name_1 = name_1_5

        kam_forosh_2 = total_num_2_1
        kam_forosh_name_2 = name_2_1

        if total_num_2_2 < kam_forosh_2 :
            kam_forosh_2 = total_num_2_2
            kam_forosh_name_2 = name_2_2

        if total_num_2_3 < kam_forosh_2 :
            kam_forosh_2 = total_num_2_3
            kam_forosh_name_2 = name_2_3

        if total_num_2_4 < kam_forosh_2 :
            kam_forosh_2 = total_num_2_4
            kam_forosh_name_2 = name_2_4

        if total_num_2_5 < kam_forosh_2 :
            kam_forosh_2 = total_num_2_5
            kam_forosh_name_2 = name_2_5

        kam_forosh_3 = total_num_3_1
        kam_forosh_name_3 = name_3_1
        
        if total_num_3_2 < kam_forosh_3 :
            kam_forosh_3 = total_num_3_2
            kam_forosh_name_3 = name_3_2

        if total_num_3_3 < kam_forosh_3 :
            kam_forosh_3 = total_num_3_3
            kam_forosh_name_3 = name_3_3

        if total_num_3_4 < kam_forosh_3 :
            kam_forosh_3 = total_num_3_4
            kam_forosh_name_3 = name_3_4

        if total_num_3_5 < kam_forosh_3 :
            kam_forosh_3 = total_num_3_5
            kam_forosh_name_3 = name_3_5

        kam_forosh_4 = total_num_4_1
        kam_forosh_name_4 = name_4_1
        
        if total_num_4_2 < kam_forosh_4 :
            kam_forosh_4 = total_num_4_2
            kam_forosh_name_4 = name_4_2

        if total_num_4_3 < kam_forosh_4 :
            kam_forosh_4 = total_num_4_3
            kam_forosh_name_4 = name_4_3

        if total_num_4_4 < kam_forosh_4 :
            kam_forosh_4 = total_num_4_4
            kam_forosh_name_4 = name_4_4

        if total_num_4_5 < kam_forosh_4 :
            kam_forosh_4 = total_num_4_5
            kam_forosh_name_4 = name_4_5

        kam_forosh_5 = total_num_5_1
        kam_forosh_name_5 = name_5_1
        
        if total_num_5_2 < kam_forosh_5 :
            kam_forosh_5 = total_num_5_2
            kam_forosh_name_5 = name_5_2

        if total_num_5_3 < kam_forosh_5 :
            kam_forosh_5 = total_num_5_3
            kam_forosh_name_5 = name_5_3

        if total_num_5_4 < kam_forosh_5 :
            kam_forosh_5 = total_num_5_4
            kam_forosh_name_5 = name_5_4

        if total_num_5_5 < kam_forosh_5 :
            kam_forosh_5 = total_num_5_5
            kam_forosh_name_5 = name_5_5


        total_kam_forosh = kam_forosh_1
        total_kam_forosh_name = kam_forosh_name_1

        if kam_forosh_2 < total_kam_forosh :
            total_kam_forosh = kam_forosh_2
            total_kam_forosh_name = kam_forosh_name_2
        if kam_forosh_3 < total_kam_forosh :
            total_kam_forosh = kam_forosh_3
            total_kam_forosh_name = kam_forosh_name_3
        if kam_forosh_4 < total_kam_forosh :
            total_kam_forosh = kam_forosh_4
            total_kam_forosh_name = kam_forosh_name_4
        if kam_forosh_5 < total_kam_forosh :
            total_kam_forosh = kam_forosh_5
            total_kam_forosh_name = kam_forosh_name_5

         

    
 

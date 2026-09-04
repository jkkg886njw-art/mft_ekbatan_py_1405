


print("wellcome to my program")

#عدد اول مربوط به سرفصل منو و عدد دوم مربوط به زیرمجموعه منو است
#منظور از name نام زیرمجموعه مورد نظر است
#منظور از p قیمت پایه است که خلاصه شده price است

sarfas_1 = "pish ghaza"

name_1_1 = "soup"

name_p_1_1 = name_1_1
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
tax = 0.09
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

main_username = "admin"
main_password = "admin"
backup_password = "12345"
j = 0
k = 0

while True :

    while True :
        
        start = input("1.administrator \n2.moshtari\n")
        match start :
            case "1" :

                if k < 3 :

                    for l in range(3):

                        username = input("please enter username :")
                        password = input("please enter password :")

                        

                        if username == main_username and password == main_password :

                        
                            while True :

                                print("\n" , "\n1.edit" , sarfas_1 ,"\n2.edit",sarfas_2,"\n3.edit", sarfas_3, "\n4.edit",sarfas_4,"\n5.edit", sarfas_5, "\n6.edit service/tax/peyk \n7.gozareshat \n8.change username and password \n9.exit\n")
                                menu = input()
                                
                                if menu == "9" :
                                    break

                                while True :

                                    match menu :
                                        case "1" :
                                            if j < 3 :
                                                print("\n\n" , "1.",name_1_1 ,"..." ,p_1_1, "\n", "2.", name_1_2 ,"..." ,p_1_2, "\n", "3.", name_1_3 ,"..." ,p_1_3, "\n", "4.", name_1_4 ,"..." ,p_1_4, "\n", "5.", name_1_5 ,"..." ,p_1_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                m_cafe = input()
                            
                                                match m_cafe :
                                                    case "1" :

                                                        cafe_1 = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match cafe_1 :
                                                            case "1" :
                                                                name_1_1 = input("please enter new name :\n")
                                                                print("new name is :" , name_1_1)
                                                            case "2" :
                                                                p_1_1 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_1_1)
                                                            case "3" :
                                                                name_1_1 = input("please enter new name :\n")
                                                                p_1_1 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_1_1, "and" ,"new price is :" , p_1_1 )
                                                                    
                                                            case _ :
                                                                break
                                                        
                                                        
                                                    case "2" :
                                                        cafe_2 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match cafe_2 :
                                                            case "1" :
                                                                name_1_2 = input("please enter new name :\n")
                                                                print("new name is :" , name_1_2)
                                                            case "2" :
                                                                p_1_2 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_1_2)
                                                            case "3" :
                                                                name_1_2 = input("please enter new name :\n")
                                                                p_1_2 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_1_2, "and" ,"new price is :" , p_1_2 )
                                                            case _ :
                                                                break
                            
                                                    case "3" :
                                                        cafe_3 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match cafe_3 :
                                                            case "1" :
                                                                name_1_3 = input("please enter new name :\n")
                                                                print("new name is :" , name_1_3)
                                                            case "2" :
                                                                p_1_3 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_1_3)
                                                            case "3" :
                                                                name_1_3 = input("please enter new name :\n")
                                                                p_1_3 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_1_3, "and" ,"new price is :" , p_1_3 )
                                                            case _ :
                                                                break
                            
                                                    case "4" :
                                                        cafe_4 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match cafe_4 :
                                                            case "1" :
                                                                name_1_4 = input("please enter new name :\n")
                                                                print("new name is :" , name_1_4)
                                                            case "2" :
                                                                p_1_4 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_1_4)
                                                            case "3" :
                                                                name_1_4 = input("please enter new name :\n")
                                                                p_1_4 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_1_4, "and" ,"new price is :" , p_1_4 )
                                                            case _ :
                                                                break
                            
                                                    case "5" :
                                                        cafe_5 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match cafe_5 :
                                                            case "1" :
                                                                name_1_5 = input("please enter new name :\n")
                                                                print("new name is :" , name_1_5)
                                                            case "2" :
                                                                p_1_5 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_1_5)
                                                            case "3" :
                                                                name_1_5 = input("please enter new name :\n")
                                                                p_1_5 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_1_5, "and" ,"new price is :" , p_1_5 )

                                                            case _ :
                                                                break
                                                    case "6" :
                                                        sarfas_1 = input("please enter new name for sarfasl_1 :\n")
                                
                                                    case _ :
                                                        break
                                            else :
                                                print("you are block")
                                                break


                                
                                        case "2" :
                                            if j < 3 :
                                                print("\n\n" , "1.",name_2_1 ,"..." ,p_2_1, "\n", "2.", name_2_2 ,"..." ,p_2_2, "\n", "3.", name_2_3 ,"..." ,p_2_3, "\n", "4.", name_2_4 ,"..." ,p_2_4, "\n", "5.", name_2_5 ,"..." ,p_2_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                m_fast = input()
                            
                                                match m_fast :
                                                    case "1" :

                                                        fast_1 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match fast_1 :
                                                            case "1" :
                                                                name_2_1 = input("please enter new name :\n")
                                                                print("new name is :" , name_2_1)
                                                            case "2" :
                                                                p_2_1 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_2_1)
                                                            case "3" :
                                                                name_2_1 = input("please enter new name :\n")
                                                                p_2_1 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_2_1, "and" ,"new price is :" , p_2_1 )
                                                            case _ :
                                                                break
                                                        
                                                        
                                                    case "2" :
                                                        fast_2 = input ("1.edit name \n2.edit price \n3.edit name and price\n")
                                                        match fast_2 :
                                                            case "1" :
                                                                name_2_2 = input("please enter new name :\n")
                                                                print("new name is :" , name_2_2)
                                                            case "2" :
                                                                p_2_2 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_2_2)
                                                            case "3" :
                                                                name_2_2 = input("please enter new name :\n")
                                                                p_2_2 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_2_2, "and" ,"new price is :" , p_2_2 )
                                                            case _ :
                                                                break
                            
                                                    case "3" :
                                                        fast_3 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match fast_3 :
                                                            case "1" :
                                                                name_2_3 = input("please enter new name :\n")
                                                                print("new name is :" , name_2_3)
                                                            case "2" :
                                                                p_2_3 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_2_3)
                                                            case "3" :
                                                                name_2_3 = input("please enter new name :\n")
                                                                p_2_3 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_2_3, "and" ,"new price is :" , p_2_3 )
                                                            case _ :
                                                                break
                            
                                                    case "4" :
                                                        fast_4 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match fast_4 :
                                                            case "1" :
                                                                name_2_4 = input("please enter new name :\n")
                                                                print("new name is :" , name_2_4)
                                                            case "2" :
                                                                p_2_4 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_2_4)
                                                            case "3" :
                                                                name_2_4 = input("please enter new name :\n")
                                                                p_2_4 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_2_4, "and" ,"new price is :" , p_2_4 )
                                                            case _ :
                                                                break
                            
                                                    case "5" :
                                                        fast_5 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match fast_5 :
                                                            case "1" :
                                                                name_2_5 = input("please enter new name :\n")
                                                                print("new name is :" , name_2_5)
                                                            case "2" :
                                                                p_2_5 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_2_5)
                                                            case "3" :
                                                                name_2_5 = input("please enter new name :\n")
                                                                p_2_5 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_2_5, "and" ,"new price is :" , p_2_5 )
                                                            case _ :
                                                                break
                                                    case "6" :
                                                        sarfas_2 = input("please enter new name for sarfasl_2 :\n")
                                
                                                    case _ :
                                                        break     
                                            else :
                                                print("you are block")
                                                break
                                            
                        
                                        case "3" :
                                            if j < 3 :
                                                print("\n\n" , "1.",name_3_1 ,"..." ,p_3_1, "\n", "2.", name_3_2 ,"..." ,p_3_2, "\n", "3.", name_3_3 ,"..." ,p_3_3, "\n", "4.", name_3_4 ,"..." ,p_3_4, "\n", "5.", name_3_5 ,"..." ,p_3_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                m_irani = input()
                            
                                                match m_irani :
                                                    case "1" :

                                                        irani_1 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match irani_1 :
                                                            case "1" :
                                                                name_3_1 = input("please enter new name :\n")
                                                                print("new name is :" , name_3_1)
                                                            case "2" :
                                                                p_3_1 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_3_1)
                                                            case "3" :
                                                                name_3_1 = input("please enter new name :\n")
                                                                p_3_1 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_3_1, "and" ,"new price is :" , p_3_1 )
                                                            case _ :
                                                                break
                                                        
                                                        
                                                    case "2" :
                                                        irani_2 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match irani_2 :
                                                            case "1" :
                                                                name_3_2 = input("please enter new name :\n")
                                                                print("new name is :" , name_3_2)
                                                            case "2" :
                                                                p_3_2 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_3_2)
                                                            case "3" :
                                                                name_3_2 = input("please enter new name :\n")
                                                                p_3_2 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_3_2, "and" ,"new price is :" , p_3_2 )
                                                            case _ :
                                                                break
                            
                                                    case "3" :
                                                        irani_3 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match irani_3 :
                                                            case "1" :
                                                                name_3_3 = input("please enter new name :\n")
                                                                print("new name is :" , name_3_3)
                                                            case "2" :
                                                                p_3_3 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_3_3)
                                                            case "3" :
                                                                name_3_3 = input("please enter new name :\n")
                                                                p_3_3 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_3_3, "and" ,"new price is :" , p_3_3 )
                                                            case _ :
                                                                break
                            
                                                    case "4" :
                                                        irani_4 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match irani_4 :
                                                            case "1" :
                                                                name_3_4 = input("please enter new name :\n")
                                                                print("new name is :" , name_3_4)
                                                            case "2" :
                                                                p_3_4 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_3_4)
                                                            case "3" :
                                                                name_3_4 = input("please enter new name :\n")
                                                                p_3_4 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_3_4, "and" ,"new price is :" , p_3_4 )
                                                            case _ :
                                                                break
                            
                                                    case "5" :
                                                        irani_5 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match irani_5 :
                                                            case "1" :
                                                                name_3_5 = input("please enter new name :\n")
                                                                print("new name is :" , name_3_5)
                                                            case "2" :
                                                                p_3_5 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_3_5)
                                                            case "3" :
                                                                name_3_5 = input("please enter new name :\n")
                                                                p_3_5 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_3_5, "and" ,"new price is :" , p_3_5 )
                                                            case _ :
                                                                break
                                                    case "6" :
                                                        sarfas_3 = input("please enter new name for sarfasl_3 :\n")
                                
                                                    case _ :
                                                        break
                                            else :
                                                print("you are block")
                                                break
                                                
                                        case "4" :
                                            if j < 3 :
                                                print("\n\n" , "1.",name_4_1 ,"..." ,p_4_1, "\n", "2.", name_4_2 ,"..." ,p_4_2, "\n", "3.", name_4_3 ,"..." ,p_4_3, "\n", "4.", name_4_4 ,"..." ,p_4_4, "\n", "5.", name_4_5 ,"..." ,p_4_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                m_bar = input()
                            
                                                match m_bar :
                                                    case "1" :

                                                        bar_1 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match bar_1 :
                                                            case "1" :
                                                                name_4_1 = input("please enter new name :\n")
                                                                print("new name is :" , name_4_1)
                                                            case "2" :
                                                                p_4_1 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_4_1)
                                                            case "3" :
                                                                name_4_1 = input("please enter new name :\n")
                                                                p_4_1 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_4_1, "and" ,"new price is :" , p_4_1 )
                                                            case _ :
                                                                break
                                                        
                                                        
                                                    case "2" :
                                                        bar_2 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match bar_2 :
                                                            case "1" :
                                                                name_4_2 = input("please enter new name :\n")
                                                                print("new name is :" , name_4_2)
                                                            case "2" :
                                                                p_4_2 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_4_2)
                                                            case "3" :
                                                                name_4_2 = input("please enter new name :\n")
                                                                p_4_2 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_4_2, "and" ,"new price is :" , p_4_2 )
                                                            case _ :
                                                                break
                            
                                                    case "3" :
                                                        bar_3 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match bar_3 :
                                                            case "1" :
                                                                name_4_3 = input("please enter new name :\n")
                                                                print("new name is :" , name_4_3)
                                                            case "2" :
                                                                p_4_3 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_4_3)
                                                            case "3" :
                                                                name_4_3 = input("please enter new name :\n")
                                                                p_4_3 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_4_3, "and" ,"new price is :" , p_4_3 )
                                                            case _ :
                                                                break
                            
                                                    case "4" :
                                                        bar_4 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match bar_4 :
                                                            case "1" :
                                                                name_4_4 = input("please enter new name :\n")
                                                                print("new name is :" , name_4_4)
                                                            case "2" :
                                                                p_4_4 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_4_4)
                                                            case "3" :
                                                                name_4_4 = input("please enter new name :\n")
                                                                p_4_4 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_4_4, "and" ,"new price is :" , p_4_4 )
                                                            case _ :
                                                                break
                            
                                                    case "5" :
                                                        bar_5 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match bar_5 :
                                                            case "1" :
                                                                name_4_5 = input("please enter new name :\n")
                                                                print("new name is :" , name_4_5)
                                                            case "2" :
                                                                p_4_5 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_4_5)
                                                            case "3" :
                                                                name_4_5 = input("please enter new name :\n")
                                                                p_4_5 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_4_5, "and" ,"new price is :" , p_4_5 )
                                                            
                                                            case _ :
                                                                break
                                                    case "6" :
                                                        sarfas_4 = input("please enter new name for sarfasl_4 :\n")
                                
                                                    case _ :
                                                        break
                                            else :
                                                print("you are block")
                                                break

                                                
                                        case "5" :
                                            if j < 3 :
                                                print("\n\n" , "1.",name_5_1 ,"..." ,p_5_1, "\n", "2.", name_5_2 ,"..." ,p_5_2, "\n", "3.", name_5_3 ,"..." ,p_5_3, "\n", "4.", name_5_4 ,"..." ,p_5_4, "\n", "5.", name_5_5 ,"..." ,p_5_5, "\n", "6.sarfasl name edite \n7.back to main menu\n")
                                                m_boardgame = input()
                            
                                                match m_boardgame :
                                                    case "1" :

                                                        boardgame_1 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match boardgame_1 :
                                                            case "1" :
                                                                name_5_1 = input("please enter new name :\n")
                                                                print("new name is :" , name_5_1)
                                                            case "2" :
                                                                p_5_1 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_5_1)
                                                            case "3" :
                                                                name_5_1 = input("please enter new name :\n")
                                                                p_5_1 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_5_1, "and" ,"new price is :" , p_5_1 )
                                                            case _ :
                                                                break
                                                        
                                                        
                                                    case "2" :
                                                        boardgame_2 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match boardgame_2 :
                                                            case "1" :
                                                                name_5_2 = input("please enter new name :\n")
                                                                print("new name is :" , name_5_2)
                                                            case "2" :
                                                                p_5_2 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_5_2)
                                                            case "3" :
                                                                name_5_2 = input("please enter new name :\n")
                                                                p_5_2 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_5_2, "and" ,"new price is :" , p_5_2 )
                                                            case _ :
                                                                break
                            
                                                    case "3" :
                                                        boardgame_3 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match boardgame_3 :
                                                            case "1" :
                                                                name_5_3 = input("please enter new name :\n")
                                                                print("new name is :" , name_5_3)
                                                            case "2" :
                                                                p_5_3 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_5_3)
                                                            case "3" :
                                                                name_5_3 = input("please enter new name :\n")
                                                                p_5_3 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_5_3, "and" ,"new price is :" , p_5_3 )
                                                            case _ :
                                                                break
                            
                                                    case "4" :
                                                        boardgame_4 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match boardgame_4 :
                                                            case "1" :
                                                                name_5_4 = input("please enter new name :\n")
                                                                print("new name is :" , name_5_4)
                                                            case "2" :
                                                                p_5_4 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_5_4)
                                                            case "3" :
                                                                name_5_4 = input("please enter new name :\n")
                                                                p_5_4 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_5_4, "and" ,"new price is :" , p_5_4 )
                                                            case _ :
                                                                break
                            
                                                    case "5" :
                                                        boardgame_5 = input ("1.edit name \n2.edit price\n3.edit name and price\n")
                                                        match boardgame_5 :
                                                            case "1" :
                                                                name_5_5 = input("please enter new name :\n")
                                                                print("new name is :" , name_5_5)
                                                            case "2" :
                                                                p_5_5 = int(input("please enter new price :\n"))
                                                                print("new price is :" , p_5_5)
                                                            case "3" :
                                                                name_5_5 = input("please enter new name :\n")
                                                                p_5_5 = int(input("please enter new price :\n"))
                                                                print("new name is :" , name_5_5, "and" ,"new price is :" , p_5_5 )
                                                            case _ :
                                                                break
                                                    case "6" :
                                                        sarfas_5 = input("please enter new name for sarfasl_5 :\n")
                                
                                                    case _ :
                                                        break
                                            else :
                                                print("you are block")
                                                break

                                        case "6" :
                                            if j < 3 :
                                                d_servis = float(input("please enter service percent :\n"))
                                                d_servis = d_servis /100
                                                tax = float(input("please enter tax percent :\n"))
                                                tax = tax /100
                                                s_peyk = int(input("please enter peyk price :\n"))
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
                                                        print("\ntedade factor haye sader shode :", tedad_factor ,"\ntedade mahsoolate sefaresh dade shode :" , total_num , "\nmajmooe kole daramd :" , int(total_forosh) , "\ntedade biron bar :", num_peyk , "\ntedade salon :" , num_salon)
                                                
                                                    case _ :
                                                        break

                                            else :
                                                print("you are block")
                                                break


                                        case "8" :
                                            if j < 3 :
                                                for i in range(3):
                                                    change_password = input("please enter backup password :\n")
                                                    if change_password == backup_password :
                                                        change = input ("1.change username \n2.change password\n3.change username and password\n4.change backup password \n")
                                                        match change :
                                                            case "1" :
                                                                main_username = input("please enter new username :\n")
                                                                print("new username is :" , main_username)
                                                            case "2" :
                                                                main_password = input("please enter new password :\n")
                                                                print("new password is :" , main_password)
                                                            case "3" :
                                                                main_username = input("please enter new username :\n")
                                                                main_password = input("please enter new password :\n")
                                                                print("new username is :" , main_username, "and" ,"new password is :" , main_password )
                                                            case "4" :
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

                
    while True :

        print("\n\n *** wellcome to my resturant *** ")
        
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

   

        while True :

            print("\n" , "\n1." , sarfas_1 ,"\n2.",sarfas_2,"\n3.", sarfas_3, "\n4.",sarfas_4,"\n5.", sarfas_5, "\n\n6. soorat hesab \n")
            menu = input()

            if menu == "6" :

                if total_num == 0 :
                    print("shoma sefaresh nadadid, bye")
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
                        print("\n\n" , "1.",name_p_1_1 ,"..." ,p_1_1, "\n", "2.", name_1_2 ,"..." ,p_1_2, "\n", "3.", name_1_3 ,"..." ,p_1_3, "\n", "4.", name_1_4 ,"..." ,p_1_4, "\n", "5.", name_1_5 ,"..." ,p_1_5, "\n", "\n6.back to main menu\n")
                        m_sarfasl_1 = input()
                        
                        match m_sarfasl_1 :
                            case "1" :
                                while True :
                                    n_1_1 = input("num of order : ")
                                    if n_1_1.isdigit()==True :
                                        n_1_1 = int(n_1_1)
                                        if n_1_1 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                    
                                
                                num_1_1 = num_1_1 + n_1_1

                                total_price = total_price + n_1_1 * p_1_1

                                total_num = total_num + n_1_1
                                
                            case "2" :
                                while True :
                                    n_1_2 = input("num of order : ")
                                    if n_1_2.isdigit()==True :
                                        n_1_2 = int(n_1_2)
                                        if n_1_2 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                            
                                num_1_2 = num_1_2 + n_1_2

                                total_price = total_price + n_1_2 * p_1_2

                                total_num = total_num + n_1_2

                            case "3" :
                                while True :
                                    n_1_3 = input("num of order : ")
                                    if n_1_3.isdigit()==True :
                                        n_1_3 = int(n_1_3)
                                        if n_1_3 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                            
                                num_1_3 = num_1_3 + n_1_3

                                total_price = total_price + n_1_3 * p_1_3

                                total_num = total_num + n_1_3

                            case "4" :
                                while True :
                                    n_1_4 = input("num of order : ")
                                    if n_1_4.isdigit()==True :
                                        n_1_4 = int(n_1_4)
                                        if n_1_4 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_1_4 = num_1_4 + n_1_4

                                total_price = total_price + n_1_4 * p_1_4

                                total_num = total_num + n_1_4

                            case "5" :
                                while True :
                                    n_1_5 = input("num of order : ")
                                    if n_1_5.isdigit()==True :
                                        n_1_5 = int(n_1_5)
                                        if n_1_5 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_1_5 = num_1_5 + n_1_5

                                total_price = total_price + n_1_5 * p_1_5

                                total_num = total_num + n_1_5

                                
                            case _ :
                                break


                    case "2" :
                        print("\n\n" , "1.",name_2_1 ,"..." ,p_2_1, "\n", "2.", name_2_2 ,"..." ,p_2_2, "\n", "3.", name_2_3 ,"..." ,p_2_3, "\n", "4.", name_2_4 ,"..." ,p_2_4, "\n", "5.", name_2_5 ,"..." ,p_2_5, "\n", "\n6.back to main menu\n")
                        m_sarfasl_2 = input()
                            
                        match m_sarfasl_2 :
                            case "1" :
                                while True :
                                    n_2_1 = input("num of order : ")
                                    if n_2_1.isdigit()==True :
                                        n_2_1 = int(n_2_1)
                                        if n_2_1 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                
                                num_2_1 = num_2_1 + n_2_1

                                total_price = total_price + n_2_1 * p_2_1

                                total_num = total_num + n_2_1
                                
                            case "2" :
                                while True :
                                    n_2_2 = input("num of order : ")
                                    if n_2_2.isdigit()==True :
                                        n_2_2 = int(n_2_2)
                                        if n_2_2 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_2_2 = num_2_2 + n_2_2

                                total_price = total_price + n_2_2 * p_2_2

                                total_num = total_num + n_2_2

                            case "3" :
                                while True :
                                    n_2_3 = input("num of order : ")
                                    if n_2_3.isdigit()==True :
                                        n_2_3 = int(n_2_3)
                                        if n_2_3 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_2_3 = num_2_3 + n_2_3

                                total_price = total_price + n_2_3 * p_2_3

                                total_num = total_num + n_2_3

                            case "4" :
                                while True :
                                    n_2_4 = input("num of order : ")
                                    if n_2_4.isdigit()==True :
                                        n_2_4 = int(n_2_4)
                                        if n_2_4 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_2_4 = num_2_4 + n_2_4

                                total_price = total_price + n_2_4 * p_2_4

                                total_num = total_num + n_2_4

                            case "5" :
                                while True :
                                    n_2_5 = input("num of order : ")
                                    if n_2_5.isdigit()==True :
                                        n_2_5 = int(n_2_5)
                                        if n_2_5 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_2_5 = num_2_5 + n_2_5

                                total_price = total_price + n_2_5 * p_2_5

                                total_num = total_num + n_2_5

                                
                            case _ :
                                break


                    case "3" :
                        print("\n\n" , "1.",name_3_1 ,"..." ,p_3_1, "\n", "2.", name_3_2 ,"..." ,p_3_2, "\n", "3.", name_3_3 ,"..." ,p_3_3, "\n", "4.", name_3_4 ,"..." ,p_3_4, "\n", "5.", name_3_5 ,"..." ,p_3_5, "\n", "\n6.back to main menu\n")
                        m_sarfasl_3 = input()

                        match m_sarfasl_3 :
                            case "1" :
                                while True :
                                    n_3_1 = input("num of order : ")
                                    if n_3_1.isdigit()==True :
                                        n_3_1 = int(n_3_1)
                                        if n_3_1 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                
                                num_3_1 = num_3_1 + n_3_1

                                total_price = total_price + n_3_1 * p_3_1

                                total_num = total_num + n_3_1
                                
                            case "2" :
                                while True :
                                    n_3_2 = input("num of order : ")
                                    if n_3_2.isdigit()==True :
                                        n_3_2 = int(n_3_2)
                                        if n_3_2 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_3_2 = num_3_2 + n_3_2

                                total_price = total_price + n_3_2 * p_3_2

                                total_num = total_num + n_3_2

                            case "3" :
                                while True :
                                    n_3_3 = input("num of order : ")
                                    if n_3_3.isdigit()==True :
                                        n_3_3 = int(n_3_3)
                                        if n_3_3 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_3_3 = num_3_3 + n_3_3

                                total_price = total_price + n_3_3 * p_3_3

                                total_num = total_num + n_3_3

                            case "4" :
                                while True :
                                    n_3_4 = input("num of order : ")
                                    if n_3_4.isdigit()==True :
                                        n_3_4 = int(n_3_4)
                                        if n_3_4 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_3_4 = num_3_4 + n_3_4

                                total_price = total_price + n_3_4 * p_3_4

                                total_num = total_num + n_3_4

                            case "5" :
                                while True :
                                    n_3_5 = input("num of order : ")
                                    if n_3_5.isdigit()==True :
                                        n_3_5 = int(n_3_5)
                                        if n_3_5 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_3_5 = num_3_5 + n_3_5

                                total_price = total_price + n_3_5 * p_3_5

                                total_num = total_num + n_3_5


                            case _ :
                                break


                    case "4" :
                        print("\n\n" , "1.",name_4_1 ,"..." ,p_4_1, "\n", "2.", name_4_2 ,"..." ,p_4_2, "\n", "3.", name_4_3 ,"..." ,p_4_3, "\n", "4.", name_4_4 ,"..." ,p_4_4, "\n", "5.", name_4_5 ,"..." ,p_4_5, "\n", "\n6.back to main menu\n")
                        m_sarfasl_4 = input()

                        match m_sarfasl_4 :
                            case "1" :
                                while True :
                                    n_4_1 = input("num of order : ")
                                    if n_4_1.isdigit()==True :
                                        n_4_1 = int(n_4_1)
                                        if n_4_1 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                
                                num_4_1 = num_4_1 + n_4_1

                                total_price = total_price + n_4_1 * p_4_1

                                total_num = total_num + n_4_1
                                
                            case "2" :
                                while True :
                                    n_4_2 = input("num of order : ")
                                    if n_4_2.isdigit()==True :
                                        n_4_2 = int(n_4_2)
                                        if n_4_2 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_4_2 = num_4_2 + n_4_2

                                total_price = total_price + n_4_2 * p_4_2

                                total_num = total_num + n_4_2

                            case "3" :
                                while True :
                                    n_4_3 = input("num of order : ")
                                    if n_4_3.isdigit()==True :
                                        n_4_3 = int(n_4_3)
                                        if n_4_3 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_4_3 = num_4_3 + n_4_3

                                total_price = total_price + n_4_3 * p_4_3

                                total_num = total_num + n_4_3

                            case "4" :
                                while True :
                                    n_4_4 = input("num of order : ")
                                    if n_4_4.isdigit()==True :
                                        n_4_4 = int(n_4_4)
                                        if n_4_4 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_4_4 = num_4_4 + n_4_4

                                total_price = total_price + n_4_4 * p_4_4

                                total_num = total_num + n_4_4

                            case "5" :
                                while True :
                                    n_4_5 = input("num of order : ")
                                    if n_4_5.isdigit()==True :
                                        n_4_5 = int(n_4_5)
                                        if n_4_5 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_4_5 = num_4_5 + n_4_5

                                total_price = total_price + n_4_5 * p_4_5

                                total_num = total_num + n_4_5

                                
                            case _ :
                                break
                    case "5" :
                        print("\n\n" , "1.",name_5_1 ,"..." ,p_5_1, "\n", "2.", name_5_2 ,"..." ,p_5_2, "\n", "3.", name_5_3 ,"..." ,p_5_3, "\n", "4.", name_5_4 ,"..." ,p_5_4, "\n", "5.", name_5_5 ,"..." ,p_5_5, "\n", "\n6.back to main menu\n")
                        m_sarfasl_5 = input()

                        match m_sarfasl_5 :
                            case "1" :
                                while True :
                                    n_5_1 = input("num of order : ")
                                    if n_5_1.isdigit()==True :
                                        n_5_1 = int(n_5_1)
                                        if n_5_1 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                
                                num_5_1 = num_5_1 + n_5_1

                                total_price = total_price + n_5_1 * p_5_1

                                total_num = total_num + n_5_1
                                
                            case "2" :
                                while True :
                                    n_5_2 = input("num of order : ")
                                    if n_5_2.isdigit()==True :
                                        n_5_2 = int(n_5_2)
                                        if n_5_2 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_5_2 = num_5_2 + n_5_2

                                total_price = total_price + n_5_2 * p_5_2

                                total_num = total_num + n_5_2

                            case "3" :
                                while True :
                                    n_5_3 = input("num of order : ")
                                    if n_5_3.isdigit()==True :
                                        n_5_3 = int(n_5_3)
                                        if n_5_3 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_5_3 = num_5_3 + n_5_3

                                total_price = total_price + n_5_3 * p_5_3

                                total_num = total_num + n_5_3

                            case "4" :
                                while True :
                                    n_5_4 = input("num of order : ")
                                    if n_5_4.isdigit()==True :
                                        n_5_4 = int(n_5_4)
                                        if n_5_4 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_5_4 = num_5_4 + n_5_4

                                total_price = total_price + n_5_4 * p_5_4

                                total_num = total_num + n_5_4

                            case "5" :
                                while True :
                                    n_5_5 = input("num of order : ")
                                    if n_5_5.isdigit()==True :
                                        n_5_5 = int(n_5_5)
                                        if n_5_5 > 0 :
                                            break
                                        else :
                                            print("voroodi sahih nist")
                                    else :
                                        print("vorodi bayad adad bashad")
                                                            
                                num_5_5 = num_5_5 + n_5_5

                                total_price = total_price + n_5_5 * p_5_5

                                total_num = total_num + n_5_5

                                
                            case _ :
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

                
                while True :
                    edit = input ("baraye eslahe sefaresh 0 ra vared namayid : \n dar gheyre in soorat baraye edame sefaresh enter ra bezanid\n")

                    match edit :
                        case "0" :
                            print("kodam sefaresh ra mikhahid eslah konid :")
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


                            if num_2_1 > 0 :
                                print(name_2_1, "...." ,num_2_1, " enter 6 " )
                            if num_2_2 > 0 :
                                print(name_2_2, "...." ,num_2_2, " enter 7 ")
                            if num_2_3 > 0 :
                                print(name_2_3, "...." ,num_2_3, " enter 8 ")
                            if num_2_4 > 0 :
                                print(name_2_4, "...." ,num_2_4, " enter 9 ")
                            if num_2_5 > 0 :
                                print(name_2_5, "...." ,num_2_5, " enter 10 ")


                            if num_3_1 > 0 :
                                print(name_3_1, "...." ,num_3_1, " enter 11 " )
                            if num_3_2 > 0 :
                                print(name_3_2, "...." ,num_3_2, " enter 12 ")
                            if num_3_3 > 0 :
                                print(name_3_3, "...." ,num_3_3, " enter 13 ")
                            if num_3_4 > 0 :
                                print(name_3_4, "...." ,num_3_4, " enter 14 ")
                            if num_3_5 > 0 :
                                print(name_3_5, "...." ,num_3_5, " enter 15 ")

                            if num_4_1 > 0 :
                                print(name_4_1, "...." ,num_4_1, " enter 16 " )
                            if num_4_2 > 0 :
                                print(name_4_2, "...." ,num_4_2, " enter 17 ")
                            if num_4_3 > 0 :
                                print(name_4_3, "...." ,num_4_3, " enter 18 ")
                            if num_4_4 > 0 :
                                print(name_4_4, "...." ,num_4_4, " enter 19 ")
                            if num_4_5 > 0 :
                                print(name_4_5, "...." ,num_4_5, " enter 20 ")

                            if num_5_1 > 0 :
                                print(name_5_1, "...." ,num_5_1, " enter 21 " )
                            if num_5_2 > 0 :
                                print(name_5_2, "...." ,num_5_2, " enter 22 ")
                            if num_5_3 > 0 :
                                print(name_5_3, "...." ,num_5_3, " enter 23 ")
                            if num_5_4 > 0 :
                                print(name_5_4, "...." ,num_5_4, " enter 24 ")
                            if num_5_5 > 0 :
                                print(name_5_5, "...." ,num_5_5, " enter 25 ")
                            
                            edit_m = input()
                            match edit_m :
                                case "1" :

                                    if n_1_1 == 0 :
                                        break
            
                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_1_1 :
                                        
                                                num_1_1 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_1_1)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "2" :

                                    if n_1_2 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_1_2:
                                        
                                                num_1_2 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_1_2)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "3" :

                                    if n_1_3 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_1_3:
                                        
                                                num_1_3 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_1_3)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "4" :

                                    if n_1_4 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_1_4:
                                        
                                                num_1_4 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_1_4)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "5" :

                                    if n_1_5 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_1_5:
                                        
                                                num_1_5 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_1_5)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "6" :

                                    if n_2_1 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_2_1:
                                        
                                                num_2_1 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_2_1)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "7" :

                                    if n_2_2 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_2_2:
                                        
                                                num_2_2 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_2_2)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "8" :

                                    if n_2_3 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_2_3:
                                        
                                                num_2_3 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_2_3)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "9" :

                                    if n_2_4 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_2_4:
                                        
                                                num_2_4 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_2_4)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "10" :

                                    if n_2_5 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_2_5:
                                        
                                                num_2_5 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_2_5)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "11" :

                                    if n_3_1 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_3_1:
                                        
                                                num_3_1 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_3_1)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "12" :

                                    if n_3_2 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_3_2:
                                        
                                                num_3_2 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_3_2)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "13" :

                                    if n_3_3 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_3_3:
                                        
                                                num_3_3 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_3_3)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "14" :

                                    if n_3_4 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_3_4:
                                        
                                                num_3_4 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_3_4)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "15" :

                                    if n_3_5 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_3_5:
                                        
                                                num_3_5 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_3_5)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "16" :

                                    if n_4_1 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_4_1:
                                        
                                                num_4_1 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_4_1)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "17" :

                                    if n_4_2 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_4_2:
                                        
                                                num_4_2 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_4_2)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "18" :

                                    if n_4_3 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_4_3:
                                        
                                                num_4_3 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_4_3)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "19" :

                                    if n_4_4 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_4_4:
                                        
                                                num_4_4 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_4_4)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "20" :

                                    if n_4_5 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_4_5:
                                        
                                                num_4_5 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_4_4)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "21" :

                                    if n_5_1 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_5_1:
                                        
                                                num_5_1 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_5_1)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "22" :

                                    if n_5_2 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_5_2:
                                        
                                                num_5_2 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_5_2)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "23" :

                                    if n_5_3 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_5_3:
                                        
                                                num_5_3 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_5_3)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "24" :

                                    if n_5_4 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_5_4:
                                        
                                                num_5_4 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_5_4)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                                case "25" :

                                    if n_55 == 0 :
                                        break

                                    while True :

                                        e1 = input("tedade morede nazar baraye eslah ra vared konid :\n")
                                        if e1 == "0" :
                                            break
                                        if e1.isdigit()==True :
                                            e1 = int(e1)
                                            if e1 > 0 and e1 <= n_5_5:
                                        
                                                num_5_5 -= e1
                                                total_num -= e1
                                                total_price -= (e1*p_5_5)

                                                break
                                            else :
                                                print("vorodi sahih nist")
                                        else :
                                            print("vorodi bayad adad bashad")
                        case _ :
                            break

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

            if total_num > 20 or total_price > 3000 :
                print("...*** ersal rayegan ***...")
                s_peyk = 0
            else :
                print("hazine ersal.................." , s_peyk)


        print("tax......................." , int(total_price*tax/100))

        total_price = total_price  * (1 + tax) + servis + s_peyk

        print("\nmablaghe ghabele pardakht ....." , int(total_price))

        ex_co = input("\n1.sefareshe dobare \n2.khoroj \n")

        match ex_co :
            case "1" :
                continue
            case _ :
                print("thank you bye")
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
    total_por_forosh = total_num_1_1

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
    por_forosh_name = name_2_1

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
    por_forosh_name = name_3_1
    
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
    por_forosh_name = name_4_1
    
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
    por_forosh_name = name_5_1
    
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

         

    
 

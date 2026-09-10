

saved_username = ""
saved_password = ""
saved_first_name = ""
saved_last_name = ""
saved_phone = ""
saved_address = ""
saved_postal_code = ""
p = 0
while True:

    if p == 1 :
        break

    choice = input("\n---MAIN MENU--- \n1.Sign In \n2.Sign Up \n3.Exit: \n")

    while True :
    
        match choice :

        
            case "1":
                
                if saved_username == "":
                    print("\n No registered user found! Please Sign Up first")
                    break
                else:
                    print("\n---  SIGN IN ---")
                    login_user = input("Enter Username: ").strip()
                    login_pass = input("Enter Password: ").strip()
                    
                    if login_user == saved_username and login_pass == saved_password:
                        print("\n Sign In Successful!")
                        
                        while True:
                        
                            print(" Welcome,", saved_first_name, saved_last_name)
                            login_suc = input("1.View Profile Info \n2.Edit Profile Info \n3.log out\n")
                            while True :
                                match login_suc :
                                    case "1":
                                        print("\n--- Profile Details ---","\nUsername:   ", saved_username,"\nFirst Name: ", saved_first_name,"\nLast Name:  ", saved_last_name,"\nMobile:     ", saved_phone,"\nAddress:    ", saved_address,"\nPostal Code:", saved_postal_code)
                                    case "2":
                                        edit =input("\n--- Profile Details Edite ---\n1.Username:\n2.password :\n3.First Name:\n4.Last Name:\n5.Mobile:\n6.Address:\n7.Postal Code: \n8.Exit")
                                        match edit :
                                            case "1" :
                                                while True:
                                                    saved_username = input("Enter Username: ").strip()
                                                    if saved_username == "" :
                                                        print(" Username cannot be empty!")
                                                    else :
                                                        break
                                            case "2" :
                                                while True :
                                                    digit_num = 0
                                                    upper_num = 0
                                                    char_num = 0
                                                    other_char = 0
                                                    if b == 0 :
                                                        saved_password = input("Enter Password: \n***The password must be at least 8 characters long and contain at least one uppercase letter, one number, and one special character(@,_,#,...)***\n").strip()
                                                    else :
                                                        saved_password = input("Enter Password: \n")
                                                    if len(new_saved_password) < 8 :
                                                        print(" Password must be at least 8 characters!")
                                                    else :
                                        
                                                        for i in new_saved_password :
                                                            if i.isdigit() :
                                                                digit_num +=1
                                                            elif i.isupper() :
                                                                upper_num +=1
                                                            elif i.islower() :
                                                                char_num +=1
                                                            else :
                                                                other_char +=1
                                                                if i == " " or i == "=" or i == "*" or i == "-" :
                                                                    other_char -=1
                                                        
                                                        if digit_num == 0 or upper_num == 0 or char_num == 0 or other_char == 0 :
                                                            print("password type wrong \n ***Reminder: ***\nThe password must be at least 8 characters long and contain at least one uppercase letter, one number, and one special character(sapace , - , = , * not avaibale).")
                                                            
                                                            b+=1

                                                        else :
                                                            saved_password = new_saved_password
                                                            break
                                                    
                                            case "3" :
                                                saved_first_name = input("Enter First Name: ").strip().capitalize()
                                            case "4" :
                                                saved_last_name = input("Enter Last Name: ").strip().title()
                                            case "5" :
                                                while True:
                                                    new_saved_phone = input("Enter Mobile: ").strip()
                                                    if new_saved_phone.isdigit()== False :

                                                        print(" Mobile must contain digits only!")
                                                    else : 
                                                        if len(new_saved_phone) != 11 :
                                                            print("The mobile number must consist of 11 digits ")    
                                                        else :
                                                            saved_phone = new_saved_phone
                                                            break
                                            case "6" :
                                                saved_address = input("Enter Home Address: ").strip().replace(" ","-")
                                            case "7" :
                                                while True:
                                                    new_saved_postal_code = input("Enter Postal Code: ").strip()
                                                    if new_saved_postal_code.isdigit()== False :
                                                        print(" Postal code must contain digits only!")
                                                    else :
                                                        if len(new_saved_postal_code) != 10 :
                                                            print("The postal code must consist of 10 digits")
                                                        else :
                                                            saved_postal_code = new_saved_postal_code
                                                            break
                                            case _ :
                                                break

                                    case "3":
                                        print("\n Logged out successfully!")
                                        break
                                
                    else:
                        print(" Wrong username or password")

            case "2":

                if len(saved_username) > 0 :
                    break 

                print("\n--- SIGN UP ---")
                
                while True:
                    saved_username = input("Enter Username: ").strip()
                    if saved_username == "" :
                        print(" Username cannot be empty!")
                    else :
                        break
                b = 0    
                while True:
                    digit_num = 0
                    upper_num = 0
                    char_num = 0
                    other_char = 0
                    if b == 0 :
                        saved_password = input("Enter Password: \n***The password must be at least 8 characters long and contain at least one uppercase letter, one number, and one special character(@,_,#,...)***\n").strip()
                    else :
                        saved_password = input("Enter Password: \n")

                    if len(saved_password) < 8 :
                        print(" Password must be at least 8 characters!")
                    else :
                        
                        for i in saved_password :
                            if i.isdigit() :
                                digit_num +=1
                            elif i.isupper() :
                                upper_num +=1
                            elif i.islower() :
                                char_num +=1
                            else :
                                other_char +=1
                                if i == " " or i == "=" or i == "*" or i == "-" :
                                    other_char -=1
                        
                        if digit_num == 0 or upper_num == 0 or char_num == 0 or other_char == 0 :
                            print("password type wrong \n ***Reminder: ***\nThe password must be at least 8 characters long and contain at least one uppercase letter, one number, and one special character(sapace , - , = , * not avaibale).")
                            
                            b+=1
                        else :
                            break
                        
                    
                saved_first_name = input("Enter First Name: ").strip().capitalize()
                
                saved_last_name = input("Enter Last Name: ").strip().title()
                
                while True:
                    saved_phone = input("Enter Mobile: ").strip()
                    if saved_phone.isdigit()== False :

                        print(" Mobile must contain digits only!")
                    else : 
                        if len(saved_phone) != 11 :
                            print("The mobile number must consist of 11 digits ")
                            
                        else :
                            break
                    
                saved_address = input("Enter Home Address: ").strip().replace(" ","-")
                
                while True:
                    saved_postal_code = input("Enter Postal Code: ").strip()
                    if saved_postal_code.isdigit()== False :
                        print(" Postal code must contain digits only!")
                    else :
                        if len(saved_postal_code) != 10 :
                            print("The postal code must consist of 10 digits")
                        else :
                            break
                    
                print(" Sign Up completed! Now you can Sign In.")
                

            
            case _ :
                print("\n Goodbye! Have a great day.")
                p = 1
                break
    
    

            
    

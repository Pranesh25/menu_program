import os

os.system("tput setaf 7")
os.system("tput setab 4")
print("""------------------------------------------------------------

	                                                   
 ,__ __                      
/|  |  |                     
 |  |  |   _   _  _          
 |  |  |  |/  / |/ |  |   |  
 |  |  |_/|__/  |  |_/ \_/|_/
                             
                             
   _            , __                              _     
  | |          /|/  \                            | |    
  | |           |___/ ,_    __,   _  _    _   ,  | |    
  |/ \_|   |    |    /  |  /  |  / |/ |  |/  / \_|/ \   
   \_/  \_/|/   |       |_/\_/|_/  |  |_/|__/ \/ |   |_/
          /|                                            
          \|                                            
 , __                  _                    
/|/  \                | |                   
 |___/ ,_    __,   ,  | |     __,   ,_      
 |    /  |  /  |  / \_|/ \   /  |  /  |     
 |       |_/\_/|_/ \/ |   |_/\_/|_/   |_/ooo
                                            
	


""")

print(""" --------------------------------------------------------------""")
print(" \n ")

os.system("tput setaf 7")
os.system("tput setab 0")

print(""" enter your choice for the following commmand to run.
	 
	 1. RUN LINUX COMMAND  \n
	 2. RUN HADOOP COMMAND \n
	 3. RUN AMAZON COMMAND \n
---------------------------------------- """)

main_menu =int( input(" enter your choice from the following menu \n"))

os.system("clear")


if main_menu == 1:
	print(" \n ------------------------------------------------------------------------\n")
	print(" you chose linux command \n ")
	print(""" where do you want to run your linux command "LOCALLY " or " REMOTE "  \n """)
	choice = int(input("press \n 1. for local and \n 2. for remote \n"))
	print("------------------------------------------------------------------------------- \n ")
	
	os.system("clear")
	
	#till 1 tab            <------------------------------
	if choice == 1 :
		#till 2 tab    <-------------------------------
		
		while 1 :
			#till 3 tabs <--------------------------
			os.system("clear")
			print("Enter the choice from the given menu")
			print("""
				  1. Date
				  2. Calender 
				  3. create yum repository
				  4.create user 
				  5. add password to user
				  6. verify user create		""")
			ch =int(input("enter your choice \n"))
			
			if  ch == 1 :
				#till 4 tabs <----------------------
				os.system("clear")
				os.system("date")
			elif ch == 2 :
				os.system("clear")
				os.system("cal")
			elif ch == 3 :
				os.system("clear")
				os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")

			elif ch == 4 :	
				os.system("clear")
				user_add = input("enter the user name that you wnat to create :- ")
				os.system("user {}".format(user_add))

			elif ch == 5 :	
				os.system("clear")
				user_check =input("enter the user id :-")
				os.system = ("passwd {}".format(user_check))
			elif ch == 6 :
				os.system("clear")
				user_check = input("enter the user id name to check if the user has been created or not")
				os.system("id {}".format(user_check))
			else :
				os.system("clear")
				print("bad choice try again")
				
	elif choice == 2 :
		#till 2 tabs <-----------------------------------------------
		print(" you choose to remotly run the commands \n \n ")
		ip =(input("enter ip \n"))
		while 1:
			# till 3 tabs <<-----------------------------------------
			
			print(" choose from the menu \n")
			print("""
				 1. date 
				 2. calender \n
				 3. work 
						""")
			ch = int(input("\n enter your choice\n"))
			if ch == 1 :
				#till 4 tabs <-----------------------------------------
				os.system("clear")
				os.system("ssh {} date" .format(ip) )
			elif ch == 2 :
				os.system("clear")
				os.system(" cal ")
			else :
				print("bad choice try again ")
	
	
elif main_menu ==2 :
	#till 1 tab <<--------------------------------------------------------
	os.system("tput setaf 7")
	os.system("tput setab 5")
	print("WELCOME TO HADOOP COMMAND ")
	print("---------------------------------------------------------")
	print("""
	choose from the following
	press 1: setup name node
	press 2: setup data node
	press 3: run name node
	press 4: run data node
	press 5: to see report of name node
	""")
	ch = int(input("enter your choice :- "))
	if(ch ==1)
		#till 2 tahs
		print("setting up the name node")
	
elif main_menu == 3 :
	print(" you choose the amazon command ")
else :
	print("bad choice ")







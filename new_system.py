n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    fuel = 100
    consumption = 10
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    loading = 0
    while loading < 5:
        loading += 1 # loop was not finished
        print("Loading module " + str(loading))
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #syntax error should be == instead of =
            print("Current Crew List:")
            
            for i in range(len(n)): #range should be n not 10
                print(n[i] + " - " + r[i] + " - " + d[i]) #logical error should have added print d[i]
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank) #issue with adding new rank to lists
            d.append(new_div)  #issue with adding new div to lists
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": #logical error should be rank == inbetween or and "commander"
                    count = count + 1
            print("High ranking officers: " + str(count)) #type error count should be a string
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        if fuel > 5: #logical error should be fuel > 5 instead of x as linking system activity to fuel levels
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
       
        if fuel > 0:            #fuel function was not called upon so fixed and now working
            
            print("Running... ")
            print(fuel)
            fuel = fuel - consumption
        else :
            print("Out of fuel...")
            print ("Shutting down!!")
            break
        print("End of cycle.")

run_system_monolith()       #error closed brackets were not placed
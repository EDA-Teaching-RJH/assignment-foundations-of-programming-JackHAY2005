n = ["Picard", "Riker", "Data", "Worf", "Spock"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Science Officer"]
d = ["Command", "Command", "Operations", "Security", "Science"]
s = ["ID001", "ID002", "ID003", "ID004", "ID005"]

def run_system():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")

    loading = 0
    while loading < 10:
        loading += 1 # loop was not finished
        print("Loading module " + str(loading))

    while True:
        display_menu()
        
        opt = input("Select option: ")

        if opt == "1": 
            display_roster(n, r, d, s)
       
        elif opt == "2":
            add_member(n, r, d, s)
        
        elif opt == "3":
            remove_member(n, r, d, s)
        
        elif opt == "4":
            update_rank(n, r, s)
                       
        elif opt == "5":
            search_crew(n, r, d, s)
        
        elif opt == "6":
            filter_by_division(n, d)
        
        elif opt == "7":
            calculate_payroll(r)
        
        elif opt == "8":
            count_officers(r)
        
        elif opt == "9":
            print("Exiting system...")
            break
        
        else:
            print("Invalid option. Please try again.")

def display_roster(n, r, d, i):
        print("Viewing Database...")
        for i in range(len(n)):
            print(n[i] + " - " + r[i] + " - " + d[i] + " - " + s[i])
def display_menu():
    print("\n--- MENU ---")
    print("1. View Database")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
def add_member(n, r, d, s):
    print("Adding Crew Member...")
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_div = input("Division: ")
    new_id = input("ID: ")

    n.append(new_name)
    r.append(new_rank)
    d.append(new_div)
    s.append(new_id)
    
    print("Crew member added.")
def remove_member(n, r, d, s):
    print("Removing Crew Member...")
    rem = input("Name to remove: ")

    if rem in n:
        idx = n.index(rem)
        n.pop(idx)
        r.pop(idx)
        d.pop(idx)
        s.pop(idx)
        print("Crew member removed.")
    else:
        print("Crew member not found.")
def update_rank(n, r, s):
    print("Updating Rank...")
    name = input("Name: ")

    if name in n:
        idx = n.index(name)
        new_rank = input("New Rank: ")
        r[idx] = new_rank
        print("Rank updated.")
    else:
        print("Crew member not found.")
def search_crew(n, r, d, s):
    print("Searching Crew...")
    query = input("Search by name: ")

    for i in range(len(n)):
        if n[i].lower() == query.lower():
            print(n[i] + " - " + r[i] + " - " + d[i] + " - " + s[i])
            return
    print("Crew member not found.")
def filter_by_division(n, d):
    print("Filtering by Division...")
    division = input("Enter division: ")

    print("Crew members in " + division + " division:")
    for i in range(len(n)):
        if d[i].lower() == division.lower():
            print(n[i] + " - " + r[i])
def calculate_payroll(r):
    print("Calculating Payroll...")
    payroll = 0

    for rank in r:
        if rank == "Captain":
            payroll += 100000
        elif rank == "Commander":
            payroll += 75000
        elif rank == "Lt. Commander":
            payroll += 50000
        elif rank == "Lieutenant":
            payroll += 30000
        else:
            payroll += 20000

    print("Total Payroll: $" + str(payroll))
def count_officers(r):
    print("Counting Officers...")
    count = 0

    for rank in r:
        if rank == "Captain" or rank == "Commander":
            count += 1
    print("High ranking officers: " + str(count))
run_system()
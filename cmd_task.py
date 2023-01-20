import json

with open('users.json') as jsonfile:
    users = json.load(jsonfile)

with open('tickets.json') as jsonfile:
    tickets = json.load(jsonfile)

with open('organizations.json') as jsonfile:
    organizations = json.load(jsonfile)

searchOptionValue = {1:'Users', 2:'Tickets', 3:'Organizations'}
searchOptiondic = {1:users, 2:tickets, 3:organizations }

def searchDesk(searchOptionInt, searchOptionValue, searchOptiondic, SearchTerm, SearchValue):
    if SearchTerm in searchOptiondic[searchOptionInt][0].keys():
        print(f"SearchTerm  {SearchTerm} is right!.\nSearching {searchOptionValue[searchOptionInt]} for {SearchTerm} with a value of {SearchValue}\n")
        try:
            if searchOptionInt == 1:
                fst = searchOptiondic[searchOptionInt][SearchValue]
                fst['organization_name'] = [org for org in organizations if org['_id']==fst['organization_id']][0]['name']
                fst = searchOptiondic[searchOptionInt][SearchValue]
                fst['organization_name'] = [org for org in organizations if org['_id']==fst['organization_id']][0]['name']
                ticketsSubjects = [ticks['subject'] for ticks in tickets if 'organization_id' in ticks and ticks['organization_id']==fst['organization_id']]
                for i in range(len(ticketsSubjects)):
                    fst[f'ticket_{i}'] = ticketsSubjects[i]
                return fst
            return searchOptiondic[searchOptionInt][SearchValue]
        except Exception as e:
            return "No results found"
    else:
        return f"Please Enter Correct {SearchTerm} for {searchOptionValue[searchOptionInt]}"


def showResult(result):
    if type(result)==dict:
        for key, value in result.items():
            # print(key, value)
            print("{:20} {:}".format(key, value))
    else:
        print(result)

def SearchList(searchOptiondic, searchOptionValue):
    for key, value in searchOptionValue.items():
        columns = (searchOptiondic[key][0].keys())
        dash = "------"
        print(f"{dash*4}\nSearch {searchOptionValue[key]} with")
        for value in columns:
            print(value)
    print(dash*4)

while True:
    print(
        """
    Welcome to Test Search-Desk
    Type 'quit' to exit at any time, Press 'Enter' to continue

        Select search options:
        - Press 1 to use Search-Desk
        - Press 2 to view a list of searchable fields
        - Type 'quit' to exit
    """)

    try:
        firstOption = input('')

        if firstOption == str(1):
            print("Welcome to Search-Desk\n")
            searchOptionInt = input("Select \n1) To search in 'Users' \n2) To search in 'Tickets' \n3) To search in 'Organizations\n")

            if searchOptionInt == 'quit':
                break

            if int(searchOptionInt) in searchOptionValue.keys():
                print(f"You are Searching in {searchOptionValue[int(searchOptionInt)]}")

                SearchTerm = input("Please Enter Search term\n")
                if SearchTerm == 'quit':
                    break
                SearchValue = input("Please Enter Seach value\n")
                if SearchValue == 'quit':
                    break
                result = searchDesk(int(searchOptionInt), searchOptionValue, searchOptiondic, SearchTerm, int(SearchValue))
                showResult(result)



        elif firstOption==str(2):
            SearchList(searchOptiondic, searchOptionValue)

        elif firstOption == 'quit':
            break
        else:
            raise(ValueError)

        if input("\n\nPress Enter for New Search...") =='quit': break

    except (ValueError, NameError):
        print("*******************\nPlease Input the right value.\n*******************")


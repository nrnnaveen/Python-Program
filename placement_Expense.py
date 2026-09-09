filename = "expenses.txt"

choice = -1

while choice != 0:

    print("""
=========================
     EXPENSE TRACKER
=========================

1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Total Expense
0. Exit
""")

    choice = int(input("Enter Your Choice : "))

    # ---------------- ADD EXPENSE ---------------- #

    if choice == 1:

        expense_id = 1

        file = open(filename, "a+")
        file.seek(0)

        lines = file.readlines()

        for line in lines:
            if "ID:" in line:
                parts = line.split(":")
                expense_id = int(parts[1]) + 1

        name = input("Enter Expense Name : ")
        amount = input("Enter Amount : ")

        print("""
1. Travel
2. Entertainment
3. Shopping
4. Rent
""")

        category = int(input("Choose Category : "))

        if category == 1:
            category_name = "Travel"

        elif category == 2:
            category_name = "Entertainment"

        elif category == 3:
            category_name = "Shopping"

        elif category == 4:
            category_name = "Rent"

        else:
            print("Invalid Category")
            file.close()
            continue

        file.write("ID:" + str(expense_id) + "\n")
        file.write("Name:" + name + "\n")
        file.write("Category:" + category_name + "\n")
        file.write("Amount:" + amount + "\n")
        file.write("--------------------\n")

        file.close()

        print("Expense Added Successfully.")

    # ---------------- VIEW EXPENSE ---------------- #

    elif choice == 2:

        file = open(filename, "r")

        data = file.read()

        print(data)

        file.close()

    # ---------------- SEARCH EXPENSE ---------------- #

    elif choice == 3:

        search_id = input("Enter Expense ID : ")

        file = open(filename, "r")

        lines = file.readlines()

        found = False

        for i in range(len(lines)):

            if lines[i].strip() == "ID:" + search_id:

                print(lines[i].strip())
                print(lines[i + 1].strip())
                print(lines[i + 2].strip())
                print(lines[i + 3].strip())

                found = True
                break

        if found == False:
            print("Expense Not Found.")

        file.close()

    # ---------------- DELETE EXPENSE ---------------- #

    elif choice == 4:

        delete_id = input("Enter Expense ID : ")

        file = open(filename, "r")

        lines = file.readlines()

        file.close()

        new_lines = []

        delete = False

        i = 0

        while i < len(lines):

            if lines[i].strip() == "ID:" + delete_id:

                delete = True
                i = i + 5

            else:
                new_lines.append(lines[i])
                i = i + 1

        file = open(filename, "w")

        for line in new_lines:
            file.write(line)

        file.close()

        if delete:
            print("Expense Deleted Successfully.")
        else:
            print("Expense ID Not Found.")

    # ---------------- TOTAL EXPENSE ---------------- #

    elif choice == 5:

        total = 0

        file = open(filename, "r")

        lines = file.readlines()

        file.close()

        for line in lines:

            if "Amount:" in line:

                parts = line.split(":")
                total = total + int(parts[1])

        print("Total Expense =", total)

    # ---------------- EXIT ---------------- #

    elif choice == 0:

        print("Thank You...")

    else:

        print("Invalid Choice")

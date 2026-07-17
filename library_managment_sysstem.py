# Library Management System

Library = {}   # Empty dictionary to store books

print("**Welcome to the Library Management System**")

# Infinite loop to keep the program running
while True:

    # Display menu
    print("\nSelect an option:")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Exit")

    # Take user's choice
    choice = int(input("Select an option between 1 to 5: "))

    # ---------------- Add Book ----------------
    if choice == 1:

        # Take book details
        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        # Store book details in dictionary
        Library[book_id] = {
            "name": book_name,
            "author": author,
            "Issued": False
        }

        print("Book added successfully!")

    # ---------------- Issue Book ----------------
    elif choice == 2:

        # Ask for book ID
        book_id = int(input("Enter Book ID: "))

        # Check if book exists
        if book_id in Library:

            # Check if book is available
            if not Library[book_id]["Issued"]:
                Library[book_id]["Issued"] = True
                print("Book issued successfully!")

            else:
                print("Book is already issued.")

        else:
            print("Book not found.")

    # ---------------- Return Book ----------------
    elif choice == 3:

        # Ask for book ID
        book_id = int(input("Enter Book ID: "))

        # Check if book exists
        if book_id in Library:

            # Check if book is issued
            if Library[book_id]["Issued"]:
                Library[book_id]["Issued"] = False
                print("Book returned successfully!")

            else:
                print("This book was not issued.")

        else:
            print("Book not found.")

    # ---------------- Search Book ----------------
    elif choice == 4:

        # Take book name to search
        search_name = input("Enter Book Name: ").lower()

        found = False

        # Search all books
        for book_id, details in Library.items():

            if search_name in details["name"].lower():

                print("\nBook Found")
                print("Book ID :", book_id)
                print("Book Name :", details["name"])
                print("Author :", details["author"])

                # Show book status
                if details["Issued"]:
                    print("Status : Issued")
                else:
                    print("Status : Available")

                found = True

        # If no book found
        if not found:
            print("Book not found.")

    # ---------------- Exit Program ----------------
    elif choice == 5:

        print("Exiting Library Management System...")
        break

    # ---------------- Invalid Choice ----------------
    else:
        print("Invalid choice! Please try again.")
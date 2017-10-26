# input
# UI functions (write instructions to screen)
# show books
# add books
# search for a book
# exit

# add a book:
#  - take input from the user
#  - load a list into memory
#  - add it to the list
#  - return what you added



def add_book(books):
    # """Add a new book and return the title"""
#    book = raw_input("Title > ")
#    book = book.title()
    prompt = "Title > "
    book, found = found_in_list(books,prompt)
    if found == False:
        books.append(book)
        books.sort()
        return book
    else:
        print "We already have that book!"

# print add_book([])

def print_list(list):
    """Takes a list, iterate over the list and show contents"""
    for item in list:
        print item

#print print_list(["book A", "book B"])

# find in a list: needs a list, and a term to find, returns t/f
def found_in_list(list,prompt):
    """Take a list, prompt for input, check if it appears in the list, return what was entered if it was found, otherwise return None"""
    query = raw_input(prompt)
    query = query.strip()
    query = query.title()
    if query in list:
        return query, True
    return query, False

#print found_in_list(books)

# partial find in a list: take user input, load a list item into a string, check input against string, return the string if found, if not, load next list item and check again.
def find_partial(list):  # returns string and bool
    """Take a list, get use query, compare query to each list item. Returns the query string and a bool"""
    query = raw_input("Search for this word > ")
    query = query.title()
    query = query.strip()
    # i = 0
    # while i <= len(list):
    #     list_item = list[i]
    #     if query in list_item:
    #         return query, True
    #     else:
    #         i = i + 1
    # return query, False
    found = False
    for item in list:
        if query in item:
            print query, "matches", item + "."
            found = True
    if found == False:
        print query, "did not match any titles in the library."


def get_command():
    """Show menu. Prompt user for a command, returns the command"""
    print "You can enter Add, view, check, search, or exit."
    command = raw_input("Enter a command > ")
    command = command.lower()
    command = command.strip()
    return command

#print get_command()



def library():
    """This is our main function wooo :) """

    books = ["Harry Potter", "The Secret", "The Secret Garden", "Snow Crash", "Good Omens"]

    print "This is my library!"
    print "-------ASCII Art woo ----------"

    while True:

        command = get_command()
        print "Action:", command

        if command == "exit":
            print "Bye now!"
            break

        elif command == "add":
            print "Add a book"
            book = add_book(books)
            if book != None:
                print "Added", book

        elif command == "view":
            print "View the list of books in the library"
            print_list(books)
            print "[End of listing.]"

        elif command == "search":
            print "Look for a partial match to a title"
            find_partial(books)
            #query, found, match_item = find_partial(books)
            # if found == True:
            #     print query, "matches", match_item, "in the library."
            # else:
            #     print query, "did not match any titles in the library."

        elif command == "check":
            print "Find out if a book is in the library"
            prompt = "Thing to search for > "
            book_to_find,result = found_in_list(books,prompt)
            if result == False:
                print "We didn't find that title."
            else:
                print "We found", book_to_find, "in the library."

        else:
            print "I'm sorry, I didn't understand that. Try again?"


library()

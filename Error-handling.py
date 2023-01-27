def open_file(file_name):
    try:
        # file = open(file_name, "r")
        # file_lines = file.readlines()
        # for line in file_lines:
        #     print(line.rstrip('\n'))
        # file.close()

        with open(file_name, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print("File cannot be found", errmsg)
        raise

open_file("order.txt")


# errmsg carries through the OG error message
# raise - brings up the red error msg
# open() - opens it but doesn't close
# close() - closes the text file, prevents mistakes
# with open() - opens and closes it itself.
# w - overwrites file, if file exists already. if you want to add to file, use a to append.
# a - to append and add to file. 

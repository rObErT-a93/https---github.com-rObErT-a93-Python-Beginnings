# This program reads the contents of the
# philosophers.txt file one line at a time.

def main():
    # Open a file named philosophers.txt.
    infile = open('Philosophers.txt', 'r')

    # Read three lines from file's contents.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Close the file.
    infile.close()

    # Print the data that was read into memory.
    print(line1)
    print(line2)
    print(line3)

    # Call the main function.
main()
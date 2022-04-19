# This program writes three lines of data
# to a file
def main():
    # Open a file named philosophers.txt.
    outfile = open('Philosophers.txt', 'w')

    # Write the names of three philosophers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('Aristotle\n')
    outfile.write('Nicholas Flamel\n')

    # Close the file.
    outfile.close()

    # Call the main function.
main()
# CS175L-50
# Vincent Tuberion
# AverageFromInput.py
# Last Modified 3/27/2022 22:17 EST

def main():
    # Open a file named numbers.txt.
    try:
        infile = open('numbers.txt', 'r')
        # Read lines from the file
        total = 0
        lines_read = 0
        for line in infile.readlines():
            line = line.strip()
            try:
                line = float(line)
                total += line
                lines_read += 1
                # Print the data that was read into memory.
                print(f"I read {lines_read} number(s) Current number is: {line:.2f} Total is: {total:.2f}")
            except ValueError:
                print("I/O ERROR: Data in file 'numbers.txt' is not of valid type, skipping data")
        print("Average:", total/lines_read)
        # Close the file.
        infile.close()
    except NameError:
        print("READ ERROR: Required file does not exist. 'numbers.txt' is missing")


# Call the main function.
if __name__ == '__main__':
    main()

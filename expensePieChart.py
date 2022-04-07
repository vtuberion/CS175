# CS175L-50
# Vincent Tuberion
# expensePieChart.py
# Last Modified 4/7/2022 19:02 EST

import matplotlib.pyplot as plt


def main():
    # Open a file named expenses.txt.
    try:
        file = open('expenses.txt', 'r')
        dataList = []
        lines_read = 0
        total = 0
        # Read each line from the file
        for line in file.readlines():  # Iterate through every line in the file
            newIndex = line.strip('\n')  # Remove any newline characters
            # Split each piece of data into its own list (the data is separated by tabs)
            newIndex = newIndex.split("\t")
            print(newIndex)
            dataList.append(newIndex)
            dataList[lines_read][1] = int(dataList[lines_read][1])
            total += dataList[lines_read][1]
            lines_read += 1
        # Close the open text file. If the user suddenly quits the program during the menu, the data will be safe
        file.close()
    except FileNotFoundError:  # Inform the user that the file was not found and the program cannot continue
        print("FileNotFoundError: Required file does not exist. 'expenses.txt' is missing")
    print(dataList)

    print(total)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = []
    sizes = []
    explode = []  # only "explode" the 2nd slice (i.e. 'Hogs')
    for i in range(len(dataList)):
        labels.append(dataList[i][0])
        sizes.append(dataList[i][1]/total)
        explode.append(0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


# Call the main function.
if __name__ == '__main__':
    main()

class fileHandler:

    @staticmethod
    def readFile():
        try:
            with open(r"C:\Users\kavin\OneDrive\Documents\Pycharm\demo.txt", "r", encoding='utf-8') as file:
                txtFile = file.read()
                print(txtFile)
        except FileNotFoundError:
            print("File not found. Make sure the file path is correct.")

        fileHandler.countStars()


    @staticmethod
    def countStars():
        try:
            with open(r"C:\Users\kavin\OneDrive\Documents\Pycharm\demo.txt", "r", encoding='utf-8') as file:
                txtFile = file.read()
                star_count = txtFile.count("*")
                print(f"Number of '*' characters in file: {star_count}")
        except FileNotFoundError:
            print("File not found. Make sure the file path is correct.")

        fileHandler.addLinetoEnd()

    @staticmethod
    def addLinetoEnd():
        try:
            with open(r"C:\Users\kavin\OneDrive\Documents\Pycharm\demo.txt", "r", encoding='utf-8') as file:
                txtFile = file.read()
                lines = txtFile.splitlines()  # split into list of lines
                if lines and lines[-1].strip() == "End of File":
                    print("Last line is: End of File")
                else:
                    with open(r"C:\Users\kavin\OneDrive\Documents\Pycharm\demo.txt", "a", encoding='utf-8') as file:

                            file.write("End of File")

        except FileNotFoundError:
            print("File not found. Make sure the file path is correct.")


if __name__ == '__main__':
    fileHandler.readFile()
    #fileHandler.countStars()

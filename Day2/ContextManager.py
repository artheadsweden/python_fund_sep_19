class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.file_name, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print("Closing")
        self.open_file.close()
        return True


def main():
    with open("file1.txt", "w") as text_file:
        text_file.write("First line\n")
        text_file.write("Second line\n")

    with File("file2.txt", "w") as text_file:
        text_file.write("First line\n")
        raise RuntimeError
        text_file.write("Second line\n")


if __name__ == '__main__':
    main()

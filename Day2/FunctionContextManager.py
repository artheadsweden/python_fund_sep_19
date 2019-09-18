from contextlib import contextmanager


@contextmanager
def open_file(file_name, mode):
    # This section is like __enter__
    print("Start of context manager")
    the_file = open(file_name, mode)
    try:
        yield the_file
        # This section is like __exit__
    except Exception:
        print("Error")
    finally:
        print("Resuming")
        # This section is like __exit__
        the_file.close()



def main():
    with open_file("file3.txt", "w") as text_file:
        text_file.write("First line\n")
        raise RuntimeError
        text_file.write("Second line\n")
        print("Done writing to file")
    print("Bye")


if __name__ == '__main__':
    main()

def my_gen(n):
    print("Starting")
    i = 0
    while i < n:
        yield i
        i += 1

def seq_generate(n):
    seq = []
    i = 0
    while i < n:
        seq.append(i)
        i += 1
    return seq


def main():
    g = my_gen(10)
    for i in g:
        print(i)

    for i in g:
        print(i)


if __name__ == '__main__':
    main()

import math
import math as m
from math import sqrt
from math import sqrt as sq


def main():
    print(math.sqrt(9))  # Uses import math
    print(m.sqrt(9))     # Uses import math as m
    print(sqrt(9))       # Uses from math import sqrt
    print(sq(9))         # Uses from math import sqrt as sq


if __name__ == '__main__':
    main()

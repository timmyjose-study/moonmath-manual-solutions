# Compute the binary representation of a non-negative integer.

from typing import List

def d2b(n: int) -> List[int]:
    b = []

    while n > 0:
        b.append(str(n % 2))
        n //= 2
    b.reverse()

    return ''.join(b)

def main():
    for n in range(21):
        print(f'{n} in binary = {d2b(n)}')

if __name__ == "__main__":
    main()
import sys


def decrypt(text):
    result: list = []
    dots: int = 0
    for symbol in text:
        if symbol != '.':
            result.append(symbol)
            dots = 0
            continue

        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0

    return ''.join(result)


if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    print(decrypt(input_text))
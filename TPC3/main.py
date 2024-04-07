import re

def adder(file, n):
    with open(file, "r", encoding='utf-8') as f:
        lines = f.readlines()

    state = True

    for line in lines:
        text = re.findall(r"(on|off|=|[+-]?\d+)", line, re.IGNORECASE)

        for chars in text:
            if chars.lower() == "on":
                state = True
            elif chars.lower() == "off":
                state = False
            elif chars == "=":
                print(f'Soma: {n}')
            elif state:
                n += int(chars)            

def main():
    n = 0
    adder("input.txt", n)

if __name__ == "__main__":
    main()
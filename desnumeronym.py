import re
import sys

def desnumeronym(numeronym: str) -> str:
    match = re.fullmatch(r"(\w)(\d+)(\w)", numeronym)
    if not match:
        return numeronym
    first, num, last = match.groups()
    return first + "_" * int(num) + last

def main():
    for input_text in sys.argv[1:]:
        output = []
        parts = re.findall(r"\w+|\W+", input_text)

        for part in parts:
            output.append(desnumeronym(part))
        
        print("".join(output), end="")

if __name__ == "__main__":
    main()
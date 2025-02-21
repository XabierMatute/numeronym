import sys
import re

def numeronym(word: str) -> str:
    if len(word) <= 3: # Comenta estas dos lineas para hacerlo aún mejor
        return word
    return f"{word[0]}{len(word) - 2}{word[-1]}"

def main():
    for input_text in sys.argv[1:]:
        output = []
        parts = re.findall(r"\w+|\W+", input_text)
        
        for part in parts:
            if part.isalpha():
                output.append(numeronym(part))
            else:
                output.append(part)
        
        print("".join(output), end="")

if __name__ == "__main__":
    main()
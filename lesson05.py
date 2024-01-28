from pathlib import Path

number_of_words = []
number_of_lines = []
src_root = Path(__file__).parent
filename = src_root / "rockyou.txt"
print(filename)
with open(filename, mode="rt", encoding="utf-8") as file:
    lines = file.read()
    lines_split = lines.split()
    input_word = input("write any word: ").lower()
    for number, i in enumerate(lines_split):
        if i == input_word:
            number_of_words.append(i)
            number_of_lines.append(number + 1)
    print(
        f"word {input_word} found {len(number_of_words)} times in these lines : {number_of_lines}"
    )
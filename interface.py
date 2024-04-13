from text_summarize import text_summarizer

print("Enter the text you want to summarize:")
text_lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    text_lines.append(line)

text = "\n".join(text_lines)

try:
    n = int(input("\nEnter the number of sentences: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

summary = text_summarizer(text, n)
print(summary)

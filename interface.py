from text_summarize import text_summarizer
text=input("\nEnter the text u want to summarize:\n")
n=int(input("\nEnter the no. of sentences: "))
summary = text_summarizer(text)
print(summary)
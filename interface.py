from fetch_summarize_news import fetch_and_summarize_news

query = input("Enter a topic to search for news articles: ")
num_sentences = int(input("Enter the number of sentences for each summary: "))
titles,urls,contents,summaries= fetch_and_summarize_news(query, num_sentences)
for i in range(len(titles)):
    print(f"""\nTitle ->{titles[i]}:\n
            \nURL ->{urls[i]}\n
            \nContent ->{contents[i]}\n
            \nSummaries ->{summaries[i]}\n\n""")

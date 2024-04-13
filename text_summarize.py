import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist


def text_summarizer(text, num_sentences=3):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)

    # Tokenize words and remove stopwords
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words and word.isalnum()]

    # Calculate word frequency
    freq_dist = FreqDist(words)

    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist: 
                if sentence not in sentence_scores:            
                    sentence_scores[sentence] = freq_dist[word] 
                else:                                           
                    sentence_scores[sentence] += freq_dist[word]

    # Select the required no. of sentences from the top
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences] 

    # Generate summary
    summary = ' '.join(top_sentences)
    return summary


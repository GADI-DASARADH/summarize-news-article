import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article 

def summarize():
    
    url = utext.get('1.0', "end").strip()

    # Create an Article object
    article = Article(url)

    # Download, parse, and apply NLP to the article
    article.download()
    article.parse()
    article.nlp()

    # Enable the text boxes
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)
    
    # Clear and insert author
    author.delete('1.0', 'end')
    author.insert('1.0', ", ".join(article.authors))

    # Clear and insert publication date (if applicable)
    publication.delete('1.0', 'end')
    publication.insert('1.0', str(article.publish_date))

    # Clear and insert summary
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Perform sentiment analysis
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.sentiment.polarity}, Sentiment: {"positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"}')

    # Disable text boxes after inserting data
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

# Create root window
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

# Label for Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()

# Text box for Title
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Label for Author
alabel = tk.Label(root, text='Author')
alabel.pack()

# Text box for Author
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# Label for Publication Date
plabel = tk.Label(root, text='Publication Date')
plabel.pack()

# Text box for Publication Date
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# Label for Summary
slabel = tk.Label(root, text='Summary')
slabel.pack()

# Text box for Summary
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Label for Sentiment Analysis
selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()

# Text box for Sentiment Analysis
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# Label for URL
url_label = tk.Label(root, text='URL')
url_label.pack()

# Text box for URL input
utext = tk.Text(root, height=1, width=140)
utext.pack()

# Button to trigger summarization
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

# Start the Tkinter main loop
root.mainloop()



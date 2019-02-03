import pandas as pd
from sentence_parse import parse_sentences

df = pd.read_csv('filings_2013_2016_complete.csv', index_col=False)

years = [2014, 2015, 2016]

filing_tickers = []
filing_years = []
filing_sentences = []
filing_old_sentence = []
filing_sentence_numbers = []

for ticker in df['ticker'].unique():
    filings = df[(df['ticker'] == ticker)]
    for year in years:
        current_file = filings[(filings['filing_year'] == year)]['file_location'].values[0]
        current_sentences = parse_sentences(current_file)

        previous_file = filings[(filings['filing_year'] == year-1)]['file_location'].values[0]
        previous_sentences = parse_sentences(previous_file)

        sentence_number = 0
        for sentence in current_sentences:
            filing_tickers.append(ticker)
            filing_years.append(year)
            filing_sentence_numbers.append(sentence_number)
            filing_sentences.append(sentence)
            filing_old_sentence.append(sentence in previous_sentences)
            sentence_number += 1

data = list(zip(filing_tickers, filing_years, filing_sentence_numbers, filing_sentences, filing_old_sentence))
columns = ['ticker', 'year', 'sentence_number', 'sentence', 'old']

df = pd.DataFrame(data=data, columns=columns)
df.to_csv('labeled_sentences.csv')

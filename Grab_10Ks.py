import time
from SECEdgar.crawler import SecCrawler


def get_ciks_tickers(cik_tickers_csv):

    ciks = []
    tickers = []

    import csv

    with open(cik_tickers_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
           ciks.append(row[0])
           tickers.append(row[1])

    print('{0} CIKs and {1} Tickers found'.format(len(ciks), len(tickers)))

    return ciks, tickers


def get_filings(cik, ticker):
    t1 = time.time()

    # create object
    seccrawler = SecCrawler()

    companyCode = ticker
    cik = cik
    date = '20170101'
    count = '10'

    seccrawler.filing_10K(str(companyCode), str(cik), str(date), str(count))

    t2 = time.time()
    print ("Total Time taken: "),
    print (t2-t1)

cik_tickers_csv = 'NYSE_Manufacturing_CIKs_Tickers.csv'

ciks = []
tickers = []

ciks, tickers = get_ciks_tickers(cik_tickers_csv)

for i in range(len(ciks)):
    get_filings(ciks[i], tickers[i])


if __name__ == '__main__':
    get_filings()


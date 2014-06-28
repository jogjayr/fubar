#will parse trades
from collections import defaultdict
from datetime import datetime
from datetime import date
import csv

strptime = datetime.strptime
portfolio_file_name = 'Jayraj Portfolio.csv'
trades_file_name = 'Jayraj_portfolio_trades.csv'
portfolio_initial_name = 'Jayraj_portfolio_initial.csv'

f_portfolio = open(portfolio_file_name)
f_trades = open(trades_file_name)

portfolio = csv.reader(f_portfolio)
trades = csv.reader(f_trades)

#establish portfolio state before all the trades

#find total buys of each security
transactions = [] 
buy_totals = defaultdict(int)
rownum, colnum = 0, 0

for trade in trades:
    if not trade:
        continue
    if rownum > 0:
        stock = trade[1]
        quantity = trade[3]
        date = trade[0]
        transactions.append({'stock': stock, 'quantity': int(quantity), 'date': strptime(date, '%d-%b-%Y')})
        buy_totals[stock] += int(quantity)
    rownum += 1

#build dict of each position in the portfolio
portfolio_dict = defaultdict(int)
rownum = 0
for holding in portfolio:
    if not holding:
        continue
    if rownum > 0:
        stock = holding[0]
        quantity = int(holding[1])
        portfolio_dict[stock] += quantity
    rownum += 1

#output portfolio at start of the year
for ticker, quantity in buy_totals.iteritems():
    portfolio_dict[ticker] -= quantity

print portfolio_dict
initial_f = open(portfolio_initial_name, 'w+')
initial_writer = csv.writer(initial_f, delimiter=',', quotechar='"')
 
#import pdb; pdb.set_trace()
for (k, v) in portfolio_dict.iteritems():
   initial_writer.writerow((k,v))

initial_f.close()


#for each trade, create a snapshot of the portfolio



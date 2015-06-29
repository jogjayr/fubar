#will parse trades
from collections import defaultdict
from datetime import datetime, timedelta
from datetime import date
import csv
import copy


def write_portfolio(p_dict, filename):
    initial_f = open(filename, 'w+')
    initial_writer = csv.writer(initial_f, delimiter=',', quotechar='"')

    for (k, v) in p_dict.iteritems():
        initial_writer.writerow((k, v))

    initial_f.close()


def strtofloat(string):
    return float(string.replace(',', ''))


def import_prices(tickers):
    prices = {}
    strptime = datetime.strptime
    google_date_format = '%b %d, %Y'
    date_format = '%d-%b-%Y'

    for ticker in tickers:
        file_handle = open('2014/%s.csv' % ticker, 'r')
        file_csv_handle = csv.reader(file_handle, delimiter=',')
        for row in file_csv_handle:
            date_key = strptime(row[3], google_date_format).strftime(date_format)
            prices.setdefault(date_key, {})
            prices[date_key][ticker] = {
                'high': strtofloat(row[1])
            }

        file_handle.close()
    return prices


def calculate_portfolio_value(portfolio, date):
    date = date.strftime(date_format)
    if date not in prices_by_day:
        return 0
    prices_on_day = prices_by_day[date]
    high = 0
    for ticker, quantity in portfolio.iteritems():
        high += prices_on_day[ticker]['high'] * quantity
    return high


def import_portfolio(fname):
    portfolio_dict = defaultdict(int)
    with open(fname) as fd:
        portfolio = csv.reader(fd)

        for holding in portfolio:
            if not holding:
                continue

            stock = holding[0]
            quantity = int(holding[1])
            portfolio_dict[stock] += quantity
    return portfolio_dict

if __name__ == '__main__':
    date_format = '%d-%b-%Y'
    google_date_format = '%b %d, %Y'

    strptime = datetime.strptime

    portfolio_file_name = 'Jayraj_portfolio.csv'
    trades_file_name = 'Jayraj_portfolio_trades.csv'
    portfolio_initial_name = 'Jayraj_portfolio_initial.csv'

    f_portfolio = open(portfolio_file_name)
    f_trades = open(trades_file_name)

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
            transactions.append({'stock': stock, 'quantity': int(quantity), 'date': strptime(date,  date_format)})
            buy_totals[stock] += int(quantity)
        rownum += 1

    portfolio_dict = import_portfolio(portfolio_file_name)

    #output portfolio at start of the year
    for ticker, quantity in buy_totals.iteritems():
        portfolio_dict[ticker] -= quantity

    write_portfolio(portfolio_dict, portfolio_initial_name)

    sorted_transactions = sorted(transactions, key=lambda k: k['date'])

    portfolios_by_date = {'02-Jan-2013': copy.deepcopy(portfolio_dict)}

    #for each trade, create a snapshot of the portfolio
    for trade in sorted_transactions:
        ticker = trade['stock']
        portfolio_dict[ticker] += trade['quantity']
        portfolio_snapshot_name = 'portfolio-' + trade['date'].strftime(date_format) + '.csv'

        #contains the state of the portfolio in a dict, keyed by date
        portfolios_by_date[trade['date'].strftime(date_format)] = copy.deepcopy(portfolio_dict)
        write_portfolio(portfolio_dict, portfolio_snapshot_name)


    portfolio_snapshot_dates = sorted([strptime(k, date_format) for k in portfolios_by_date.keys()])

    year_start = date


    single_day = timedelta(days=1)
    start_date = strptime('02-Jan-2014', date_format)
    end_date = strptime('31-Dec-2014', date_format)

    d = start_date
    next_portfolio_date_index = 1
    next_portfolio_date = portfolio_snapshot_dates[next_portfolio_date_index]
    current_portfolio_date_index = next_portfolio_date_index - 1
    current_portfolio_date = portfolio_snapshot_dates[current_portfolio_date_index]
    current_portfolio = portfolios_by_date[current_portfolio_date.strftime(date_format)]

    prices_by_day = import_prices(portfolio_dict.keys())


    all_values = []
    while d <= end_date:
        if d > next_portfolio_date:
            next_portfolio_date_index += 1
            if next_portfolio_date_index < len(portfolio_snapshot_dates):
                current_portfolio_date_index = next_portfolio_date_index - 1
                current_portfolio_date = portfolio_snapshot_dates[current_portfolio_date_index]
                current_portfolio = portfolios_by_date[current_portfolio_date.strftime(date_format)]
                next_portfolio_date = portfolio_snapshot_dates[next_portfolio_date_index]
                print "current date: %s nextdate: %s" % (current_portfolio_date.strftime(date_format), next_portfolio_date.strftime(date_format))
            elif next_portfolio_date_index == len(portfolio_snapshot_dates):
                current_portfolio_date = next_portfolio_date
                current_portfolio = portfolios_by_date[current_portfolio_date.strftime(date_format)]
        value_on_date = calculate_portfolio_value(current_portfolio, d)
        all_values.append({"date": d.strftime(date_format), "value": value_on_date})
        d += single_day


    sorted_values = sorted(all_values, key=lambda k: k['value'])
    # sorted_values = all_values

    for item in sorted_values:
        print "Date: %s High: %s" % (item['date'], item['value'])

    f_portfolio.close()
    f_trades.close()


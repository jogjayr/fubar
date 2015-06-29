from parse_trades import import_prices, import_portfolio, calculate_portfolio_value

portfolio = import_portfolio('Jayraj_portfolio.csv')
prices_by_day = import_prices(portfolio.keys())
max_val = 0

for dt, prices in prices_by_day.iteritems():
    val = sum([ portfolio[ticker] * prices_high['high'] for ticker, prices_high in prices.iteritems()])
    if max_val < val:
        max_val = val
        max_date = dt

print max_val, max_date

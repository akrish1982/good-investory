UPDATE options
SET 
    LOT_SIZE = (SELECT MARKET_LOTS.APR_17 from MARKET_LOTS where MARKET_LOTS.SYMBOL = options.SYMBOL)
where exists(
    SELECT * from MARKET_LOTS where MARKET_LOTS.SYMBOL = options.SYMBOL and options.timestamp = '06-APR-2017'
);

UPDATE options
SET premium = LOT_SIZE * CLOSE
where timestamp = '06-APR-2017';

UPDATE options
SET 
    underlying_price = (SELECT stocks.close from stocks where stocks.SYMBOL = options.SYMBOL and stocks.TIMESTAMP = '06-APR-2017')
where exists(
    SELECT options.SYMBOL from stocks where stocks.SYMBOL = options.SYMBOL
    AND options.timestamp = '06-APR-2017'
    AND options.INSTRUMENT='OPTSTK'
) ;

UPDATE options
    set percent_move = 100*(underlying_price - strike_pr - close)/underlying_price
where underlying_price is not NULL
        and timestamp = '06-APR-2017';
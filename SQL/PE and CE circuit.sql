select symbol, strike_pr, close, high, low, contracts, percent_move, premium, lot_size, underlying_price,  volatility.annualized_volatility from options inner join volatility on options.SYMBOL = volatility.Symbol  
where
    option_typ = 'PE' 
    and percent_move > 8
    and premium > 2000
    and contracts > 1 
    and expiry_dt = '23-Feb-2017'
    and timestamp = '08-FEB-2017';

    
select options.symbol, strike_pr, close, high, low, contracts, percent_move, premium, lot_size, underlying_price, volatility.annualized_volatility from options inner join volatility on options.SYMBOL = volatility.Symbol 
where
 option_typ = 'CE' 
    and percent_move < -10
    and premium > 2000
    and contracts > 1 
    and expiry_dt = '23-Feb-2017'
    and timestamp = '08-FEB-2017';  
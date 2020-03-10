#FIRST QUESTION

portfolio_value = 16000000
mean_returns = 1/100
vol_returns = 3/100
mean_spread = round(0.35/100,4)
vol_spread = 1.5/100
factor = 2.32635

VAR = portfolio_value*(-mean_returns + factor * vol_returns)
LVAR = portfolio_value*(-mean_returns + factor * vol_returns + 0.5*(mean_spread + factor*vol_spread))
LVAR_MINUS_VAR = LVAR - VAR

print('====== PARAMETRIC VAR - Question A ======')
print('portfolio_value: ' + str(portfolio_value))
print('mean_returns: ' + str(mean_returns))
print('vol_returns: ' + str(vol_returns))
print('mean_spread: ' + str(mean_spread))
print('vol_spread: ' + str(vol_spread))
print('factor: ' + str(factor))
print('VAR: ' + str(VAR))
print('LVAR: ' + str(LVAR))
print('LVAR_MINUS_VAR: ' + str(LVAR_MINUS_VAR))


#NOW SECOND QUESTION - UK GILTS

portfolio_value = 40000000
mean_returns = 0/100
vol_returns = 3/100
mean_spread = round(0.15/100,4)
vol_spread = 0/100
factor = 2.32635

VAR = portfolio_value*(-mean_returns + factor * vol_returns)
LVAR = portfolio_value*(-mean_returns + factor * vol_returns + 0.5*(mean_spread + factor*vol_spread))
LVAR_MINUS_VAR = LVAR - VAR

print('====== PARAMETRIC VAR - Question B.1 ======')
print('portfolio_value: ' + str(portfolio_value))
print('mean_returns: ' + str(mean_returns))
print('vol_returns: ' + str(vol_returns))
print('mean_spread: ' + str(mean_spread))
print('vol_spread: ' + str(vol_spread))
print('factor: ' + str(factor))
print('VAR: ' + str(VAR))
print('LVAR: ' + str(LVAR))
print('LVAR_MINUS_VAR: ' + str(LVAR_MINUS_VAR))


portfolio_value = 40000000
mean_returns = 0/100
vol_returns = 3/100
mean_spread = round(1.25/100,4)
vol_spread = 0/100
factor = 2.32635

VAR = portfolio_value*(-mean_returns + factor * vol_returns)
LVAR = portfolio_value*(-mean_returns + factor * vol_returns + 0.5*(mean_spread + factor*vol_spread))
LVAR_MINUS_VAR = LVAR - VAR

print('====== PARAMETRIC VAR - Question B.2 ======')
print('portfolio_value: ' + str(portfolio_value))
print('mean_returns: ' + str(mean_returns))
print('vol_returns: ' + str(vol_returns))
print('mean_spread: ' + str(mean_spread))
print('vol_spread: ' + str(vol_spread))
print('factor: ' + str(factor))
print('VAR: ' + str(VAR))
print('LVAR: ' + str(LVAR))
print('LVAR_MINUS_VAR: ' + str(LVAR_MINUS_VAR))

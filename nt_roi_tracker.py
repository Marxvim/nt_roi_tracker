# Online Python - IDE, Editor, Compiler, Interpreter
def get_return(returns, investment, days):
    for i in range(days):
        if (i % 7 == 0):
            print(f'\nDay {i} = {returns}')
        returns = (returns * (investment/100)) + returns
    return returns
    

capital = float(input('Capital investment: '))
interest_rate = float(input('Compounding interest: '))
total_time = int(input('number of days: '))

print(f'\nThe total return for a compounding interest rate of {interest_rate}% starting with an initial capital investment of ${capital} is ${get_return(capital, interest_rate, total_time)}')

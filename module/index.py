def compute_outstanding_load_balance(mortgage_characteristics):
    '''
    Compute the outstanding load balance after a given number of months
    '''
    try:
        numerator = (((1 + mortgage_characteristics["r"])**mortgage_characteristics["n"]) \
                    - ((1 + mortgage_characteristics["r"])**mortgage_characteristics["m"]))
        denominator = (((1 + mortgage_characteristics["r"])**mortgage_characteristics["n"]) - 1)
        outstanding_load_balance = round(mortgage_characteristics["P"] \
                                   * (numerator / denominator), 2)
    except:
        outstanding_load_balance = None
        print("Sorry, we were unable to compute your outstanding load balance.")
    return outstanding_load_balance

def compute_monthly_paiement(mortgage_characteristics):
    '''
    Compute the average monthly payment for the loan
    '''
    try:
        monthly_paiements = round(mortgage_characteristics["P"] * mortgage_characteristics["r"] \
                            * ((1 + mortgage_characteristics["r"])**mortgage_characteristics["n"] \
                            / ((1 + mortgage_characteristics["r"])**mortgage_characteristics["n"] - 1)), 2)
    except:
        monthly_paiements = None
        print("Sorry, we were unable to compute your average monthly payment.")
    return monthly_paiements

def set_interest_rate():
    '''
    Recover the interest rate applied to the loan in the CLI
    '''
    while True:
        try:
            interest_rate = float(input('Enter the interest rate applied to the loan :\n')) / 100
            if interest_rate <= 0:
                print('Error, the value must be a float.\n')
                continue
        except ValueError:
            print("Error, enter a float number please.\n")
            continue
        else:
            break
    return interest_rate

def set_characteristic(instruction):
    '''
    Recover the total amount of the loan in the CLI
    '''
    while True:
        try:
            characteristic = int(input(instruction))
            if characteristic <= 0:
                print("Error, the value can't be equal or inferior to zero.\n")
                continue
        except ValueError:
            print("Error, enter a number please.\n")
            continue
        else:
            break
    return characteristic

def set_mortgage_characteristics():
    '''
    Insert the mortgage characteristics inside a dictionnary
    '''
    mortgage_characteristics = {
        "P": None,
        "r": None,
        "n": None,
        "m": None,
        "M": None,
        "L": None
    }
    mortgage_characteristics["P"] = set_characteristic(instruction='Enter the total amount of the mortgage loan :\n')
    mortgage_characteristics["r"] = set_interest_rate()
    mortgage_characteristics["n"] = set_characteristic(instruction='Enter the number of months :\n')
    mortgage_characteristics["m"] = set_characteristic(instruction='Check the outstanding loan balance after :\n')
    return mortgage_characteristics

def display_mortgage_informations(mortgage_characteristics):
    print("If you borrow ${} at an interest rate of {}% over a {} months period :\n"
          .format(mortgage_characteristics["P"], mortgage_characteristics["r"] * 100, mortgage_characteristics["n"]))
    print("\t- you monthly payment will be equal to ${}\n".format(mortgage_characteristics["M"]))
    print("After {} months, your outstanding load balance will be equal to ${}".format(mortgage_characteristics["m"], mortgage_characteristics["L"]))

def compute_mortgage():
    '''
    Execute Mortgage Formulas once the dictionnary is set
    '''
    mortgage_characteristics = set_mortgage_characteristics()
    mortgage_characteristics["M"] = compute_monthly_paiement(mortgage_characteristics)
    mortgage_characteristics["L"] = compute_outstanding_load_balance(mortgage_characteristics)
    display_mortgage_informations(mortgage_characteristics)
    return mortgage_characteristics

if __name__ == '__main__':
    compute_mortgage()

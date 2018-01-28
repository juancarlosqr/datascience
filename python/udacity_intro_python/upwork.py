#/usr/bin/env python3

import sys

def calculate_earnings():
    if len(sys.argv) < 2:
        print('No balance provided')
    else:
        balance = float(sys.argv[1])
        earning_after_comission = balance * .8
        earning_after_vat = earning_after_comission * .953
        earning_dollars = earning_after_vat - 2
        earning_euros = earning_dollars / 1.25
        print(f'''Balance: {balance}
Earnings USD: {earning_dollars:.2f}
Earnings EUR: {earning_euros:.2f}''')

if __name__ == '__main__':
    calculate_earnings()

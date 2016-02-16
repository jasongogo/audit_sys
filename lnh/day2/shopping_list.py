#! /usr/bin/python

# author = 'jason'
import sys


products = ['apple','watch','coffee','car']
price = [30,1000,30,100000]
salary = raw_input('Please input your salary: ')
while True:
    
    print 'Here is the shopping lists!\n'
    for product in products:
        print product, ' '.ljust(10),price[products.index(product)]
    buy_product = raw_input('Please input product you want to buy: ')
    if buy_product in products:
        if int(salary) < price[products.index(buy_product)]:
            print 'You salary is not enough for buying %s, please re-buy again ' % buy_product
            sys.exit()
        else:
            salary = int(salary) - price[products.index(buy_product)]
            print 'You left %s now' % salary
    else:
        print 'Please input again!'
        continue
    



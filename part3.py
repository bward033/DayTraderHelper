"""
    Program:project 1
    Author: Bryan Ward
    Description: Helps day traders keep tabs on there money
"""





def main():

    balance = float(input('Starting cash amount?')) #float!!!
    starting_balance = balance



    num_trades = int(input('Number of trades for today? ')) # int!!

    print("You do not own any shares, but have $%s in cash." % balance)

    shares_bt=int(0)
    shares_st=int(0)
    Tsharesowned= shares_bt - shares_st
    Totaltradesb=float(0.0)
    trade_sellv=float(0.0)
    TradeSellV=float(0.0)
    value_s = float(0.0)


    min_price_sold = None
    max_price_sold = None




    for i in range(num_trades,):




        if shares_bt == 0:                      #starts trade with a buy
            num_shares = int(input('\nNumber of shares to buy? '))      # asks for shares
            value_b = float(input('Price per share? '))                 #value for shares
            trade_v = value_b * num_shares                              #calulates dollars spent or earned

            if balance < trade_v:
                    print('You do not have sufficient funds to purchase shares %s for $%s per share.' % (num_shares, value_b))
                    print('Your current balance is $%s but %s x $%s = %s' %(balance, num_shares, value_s, trade_v))

            else:
                shares_bt = shares_bt+num_shares #saves share bought
                Tsharesowned = Tsharesowned + num_shares  #save total shares bought
                trade_v = value_b*num_shares                #total trade value in dollars
                Totaltradesb = Totaltradesb + trade_v       #total trade value in dollars
                balance = balance-trade_v                   #finds balance
                min_price_bought = value_b                  #insilizes min_price_bought
                max_price_bought = value_b                  #insulizes max_price

                print(num_shares,' shares for $',value_b,' per share worth $', trade_v,sep='')





        else:
            prompt = "\ntrade number " + str(i +1) + ' (buy or sell)? '
            action = input(prompt)


            if action == ("buy"):
                num_shares = int(input('Number of shares to buy?'))
                value_b = float(input('Price per share?'))
                trade_v = value_b*num_shares

                if balance < trade_v:
                    print('You do not have sufficient funds to purchase %s shares for $%s per share.' % (num_shares, value_b))
                    print('Your current balance is $%s but %s x $%s = %s' %(balance, num_shares, value_s, trade_v))

                else:
                    shares_bt = shares_bt + num_shares          #saves share bought
                    Tsharesowned = Tsharesowned + num_shares    #save total shares bought
                    trade_v = value_b*num_shares                #total trade value in dollars
                    Totaltradesb = Totaltradesb + trade_v       #total trade value in dollars
                    balance = balance-trade_v                   #finds balance

                    if max_price_bought < value_b:              #finds highest stock price
                        max_price_bought = value_b              #saves price

                    if min_price_bought > value_b:              #finds the lowest
                        min_price_bought = value_b              #saves value

                    print(num_shares,' shares for $',value_b,' per share worth $', trade_v,sep='')



            else:

                shares_s = int(input('Number of shares to sell? '))  #user inputs shares sold


                if Tsharesowned < shares_s:  #checks to see
                    print('You can’t sell %s shares as you only have %s.' %(shares_s, Tsharesowned))  #yells at user

                else:

                    value_s = float(input('Sale price? '))  #finds how muck stock is sold for

                    shares_st = shares_st+shares_s      #saves total shares sold
                    trade_sellv = value_s*shares_s      #finds value of trade
                    TradeSellV = TradeSellV + trade_sellv  #saves value of trades
                    balance = balance + trade_sellv         #finds new balance
                    Tsharesowned = Tsharesowned - shares_s      #finds current shares owned

                    if max_price_sold == None or max_price_sold < value_s:  #finds highest sold stock
                        max_price_sold = value_s                            #saves
                    if min_price_sold == None or min_price_sold > value_s:  #finds lowest stock sold
                        min_price_sold = value_s                            #saves stock price


                    print(shares_s,' shares for $',value_s,' per share worth $', trade_sellv,sep='')        #prents trade info




        if i + 1 == num_trades:     # to creat zero balance at end of day

            print('\nTrading day is almost over and you are left with %s shares and $%s cash.'%(Tsharesowned,balance))
            value_s = float(input('Enter the price to sell these shares:'))

            shares_s = Tsharesowned        # convers all shares owned to sell saved me time
            shares_st = shares_st + shares_s    #saves total shares sold
            trade_sellv = value_s * shares_s    #saves value of trades
            TradeSellV = TradeSellV + trade_sellv      #saves value of trades
            balance = balance + trade_sellv         #finds new balance
            Tsharesowned = Tsharesowned - shares_s      #finds current shares owned

            if max_price_sold == None or max_price_sold < value_s:  #finds highest sold stock
                max_price_sold = value_s                            #saves
            if min_price_sold == None or min_price_sold > value_s:  #finds lowest stock sold
                min_price_sold = value_s                            #saves stock price


            print(shares_s,' shares for $',value_s,' per share worth $', trade_sellv,sep='')

        else:

            print("Currently holding ",Tsharesowned," shares and have $",balance,' in cash.',sep='')






    average_shares_bouget = Totaltradesb / shares_bt           # finds average shares bought
    average_shares_sold = TradeSellV/shares_st                  #finds average shares sold

    print('\nTotal shares bought for the day is ',shares_bt,' with an average of $',average_shares_bouget, ' per share.',sep='',)
    print('Minimum and maximum price per share bought are $',min_price_bought,' and $',max_price_bought,', respectively.',sep='')
    print('Total shares sold for the day is ',shares_st,' with an average of $',average_shares_sold,' per share.',sep='')
    print('Minimun and maximum sale price per share are $',min_price_sold,'and $',max_price_sold,', respectively',sep='')

    if starting_balance > balance:          #looks to see if loss money
        balance_loss = starting_balance - balance       #calulates loss
        print('End of day balance is $',balance, ' a loss of $',balance_loss,sep='')

    elif starting_balance < balance:            #looks to see if gain money
        balance_gain = balance - starting_balance   #calulates gain
        print('End of day balance is $',balance, ' a gain of $',balance_gain,sep='')

    else:               #zero gain/loss
        print('End of day balance ended with no change in account $',balance,sep='')

main()
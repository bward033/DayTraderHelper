
"""
    Program:project 1
    Author: Bryan Ward
    Description: Helps day traders keep tabs on there money
"""





def main():

    balance = float(input('Starting cash amount?')) #float!!!



    num_trades = int(input('Number of trades for today? ')) # int!!

    shares_bt=int(0)
    shares_st=int(0)
    Tsharesowned= shares_bt - shares_st
    Totaltradesb=float(0.0)
    trade_sellv=float(0.0)
    TradeSellV=float(0.0)







    print('\nCurrently holding ',Tsharesowned,' shares and have $',balance, ' in cash.',sep='',)
    print('Shares owned',Tsharesowned,)
    print('Cumulative shares purchased',shares_bt)
    print('Cumulative purchase amount',Totaltradesb)
    print('Cumulative shares sold',shares_st)
    print('Cumulative sales amount ',trade_sellv)


    for i in range(num_trades,):
        print("\ntrade number",i+1,)



        if shares_bt == 0:
            num_shares = int(input('Number of shares to buy? '))
            value_b = float(input('Price per share? '))
            shares_bt = shares_bt+num_shares
            trade_v = value_b*num_shares
            Totaltradesb = Totaltradesb + trade_v
            balance = balance-trade_v

            print('\n',num_shares,' shares for $',value_b,'per share worth $', trade_v,sep='')
            print('Transaction',i+1,'\nTransaction Type is buy ')
            print("Currently holding ",shares_bt," shares and have $",balance,' in cash.',sep='')
            print('Cumulative shares purchased',shares_bt)
            print('Cumulative purchase amount',Totaltradesb)
            print('Cumulative shares sold',shares_st)
            print('Cumulative sales amount ',TradeSellV)


        else:
            prompt = "trade number " + str(i +1) + ' buy or sell? '
            action = input(prompt)

            if action == ("buy"):
                num_shares = int(input('Number of shares to buy?'))
                value_b = float(input('Price per share?'))
                shares_bt = shares_bt + num_shares
                trade_v = value_b*num_shares
                Totaltradesb = Totaltradesb + trade_v
                balance = balance-trade_v

                print('\n',num_shares,' shares for $',value_b,'per share worth $', trade_v,sep='')
                print('Transaction',i+1,'\nTransaction Type is buy ')
                print("\nCurrently holding ",shares_bt," shares and have $",balance,'in cash.',sep='')
                print('Cumulative shares purchased',shares_bt)
                print('Cumulative purchase amount',Totaltradesb)
                print('Cumulative shares sold',shares_st)
                print('Cumulative sales amount ',TradeSellV)

            else:

                shares_s = int(input('Number of shares to sell? '))
                value_s = float(input('Sale price? '))
                shares_st = shares_st+shares_s
                trade_sellv = value_s*shares_s
                TradeSellV = TradeSellV + trade_sellv
                balance = balance + trade_sellv
                Tsharesowned= shares_bt - shares_st


                print('\n',shares_s,' shares for $',value_s,'per share worth $', trade_sellv,sep='')
                print('Transaction',i+1,'\nTransaction Type is sell ')
                print("\nCurrently holding ",Tsharesowned," shares and have $",balance,' in cash.',sep='')
                print('Cumulative shares purchased',shares_bt)
                print('Cumulative purchase amount',Totaltradesb)
                print('Cumulative shares sold',shares_st)
                print('Cumulative sales amount ',TradeSellV)







main()



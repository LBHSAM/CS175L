commission_rate_purchase = float(input("Enter commission rate percentage on stock purchase (ex. 0.03): "))
commission_rate_sale = float(input("Enter commission rate percentage on stock sale (ex. 0.03): "))
num_shares_purchased = int(input("Enter number of shares purchased: "))
num_shares_sold = int(input("Enter number of shares sold: "))
purchase_price_per_share = float(input("Enter purchase price per share: "))
sell_price_per_share = float(input("Enter sell price per share: "))

amount_paid_for_stock = num_shares_purchased * purchase_price_per_share
purchase_commission = commission_rate_purchase * amount_paid_for_stock
total_paid = amount_paid_for_stock + purchase_commission
stock_sold_for = num_shares_sold * sell_price_per_share
selling_commission = commission_rate_sale * stock_sold_for
total_received = stock_sold_for - selling_commission
profit_or_loss = total_received - total_paid

print("Amount paid for the stock: ${:,.2f}".format(amount_paid_for_stock))
print("Commission paid on the purchase: ${:,.2f}".format(purchase_commission))
print("Amount the stock sold for: ${:,.2f}".format(stock_sold_for))
print("Commission paid on the sale: ${:,.2f}".format(selling_commission))
print("Profit (or loss if negative): ${:,.2f}".format(profit_or_loss))

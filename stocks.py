# CS175L-50
# Vincent Tuberion
# stocks.py
# Last Modified 1/26/2022 19:20 EST

# Input
COMMISSION_RATE = float(input("What was the commission rate? (Use 'float' type): "))
NUM_SHARES = int(input("How many shares did you purchase? (Use 'int' type): "))
PURCHASE_PRICE = float(input("What was the purchase price? (Use 'float' type): "))
SELLING_PRICE = float(input("What was the selling price? (Use 'float' type): "))

# Calculations
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

# Output
print("\n------------TOTAL------------")
print("Amount paid for stock: $", amountPaidForStock)
print("Commission paid on the purchase: $", purchaseCommission)
print("Amount the stock sold for: $", stockSoldFor)
print("Commission paid on the sale: $", sellingCommission)
print("Total recieved: $", totalReceived)
print("Total commission payment: $", (purchaseCommission + sellingCommission))
print("Amount after commission: $", stockSoldFor - (purchaseCommission + sellingCommission))
print("Profit (or loss if negative): $", profitOrLoss)

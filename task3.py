# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400
}

total = 0

print("📈 Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        value = stock_prices[stock] * quantity
        total += value

        print("Investment in", stock, "=", value)

    else:
        print("❌ Stock not found.")

print("\n💰 Total Investment =", total)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment = " + str(total))

print("Result saved in portfolio.txt")
"""
Python Program that can do following:
You Have 50$
You Buy An Item Of 15$ With 3% Tax
How Much Money Left After Purchasing
"""
Money=50
Item=15
Tax=(Item/100)*3
Total=Money-(Item+Tax)
print(f"If I have {Money}$ and bought an item for {Item}$ with 3% Tax Then {Total}$ are left")
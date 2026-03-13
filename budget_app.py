# Budget App - Spending Tracker and Visualizer
# --------------------------------------------
# This module provides a Category class to manage deposits, withdrawals, and 
# transfers between budget categories. It also includes a utility function 
# to generate a vertical bar chart representing the percentage of total 
# spending across all categories.

class Category:
    def __init__(self, name):
        self.ledger = list()
        self.name = name 
    
    def __str__(self):
        #Returns a formatted string representation of the budget ledger.
        output = self.name.center(30,"*") + "\n"

        for item in self.ledger:
            description = item['description'][:23]
            amount_str = "{:.2f}".format(item['amount'])
            spaces = " " * (30 - len(description) - len(amount_str))
            output += description[:23] + spaces + amount_str+"\n"
        
        output += "Total: " + "{:.2f}".format(self.get_balance()) +"\n"
                  
        return output
    
    # The transaction steps 
    def deposit(self, amount,description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        balance = sum(item['amount'] for item in self.ledger)
        return balance
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def transfer(self, amount, new_category):
        if self.withdraw(amount,"Transfer to "+ new_category.name):
            new_category.deposit(amount,"Transfer from "+self.name)
            return True
        else:
            return False
    
    

def create_spend_chart(categories):
    withdrawal_totals = []
    total_spent_all_categories = 0

    #Gathers each withdrawal data
    for cat in categories:
        spent_in_this_cat = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                spent_in_this_cat += abs(item['amount'])
        
        withdrawal_totals.append(spent_in_this_cat)
        total_spent_all_categories += spent_in_this_cat
    
    # Calculate percentages rounded down to the nearest 10
    formatted_list = list()
    for percent in withdrawal_totals:
        formatted_list.append((percent * 100 / total_spent_all_categories) // 10 * 10)
    

    line = 'Percentage spent by category\n'

    #Writes the "o" in place of the percent
    for i in range(100,-1,-10):
        line += f"{i:3}|"
        for percent in formatted_list:
            if percent >= i:
                line += " o "
            else:
                line += ("   ")
        line += " \n"
       
    
    line += 4*" " + "-" * (len(categories) * 3 + 1) +"\n"

    # Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line += "     " 
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            line += "\n"

    return line

if __name__ == "__main__":
    food = Category('Food')
    clothing = Category('Clothing')

    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    food.transfer(50, clothing)
    print(food)

    clothing.withdraw(20,'maintenance')
    categories = [food,clothing]
    print(create_spend_chart(categories))


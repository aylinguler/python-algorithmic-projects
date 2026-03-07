class Category:
    def __init__(self, name):
        self.ledger = list()
        self.name = name # Don't forget I need this to refer to the name later!
    
    def __str__(self):
        output = self.name.center(30,"*") + "\n"

        for item in self.ledger:
            description = item['description'][:23]
            amount_str = "{:.2f}".format(item['amount'])
            spaces = " " * (30 - len(description) - len(amount_str))
            output += description[:23] + spaces + amount_str+"\n"
        
        output += "Total: " + "{:.2f}".format(self.get_balance())
                  
        return output
    
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
    
    def transfer(self, amount, new_category): #The parameter new_category is a full on class in itself so you need to call it as new_category.name to reach its name
        if self.withdraw(amount,"Transfer to "+ new_category.name):
            new_category.deposit(amount,"Transfer from "+self.name)
            return True
        else:
            return False
    
    

def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
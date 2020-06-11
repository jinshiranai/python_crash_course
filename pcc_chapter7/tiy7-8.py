# PCC Try It Yourself 7-8. Deli.

# 7-9. No Pastrami.
print("Sorry, Azaziel's Sandwiches just ran out of pastrami! Sadness.")

sandwich_orders = ['pastrami', 'ham and cheese', 'grilled cheese', 'pastrami',
    'blt', 'pastrami', 'turkey', 'chicken', 'pastrami', 'tuna']
finished_sandwiches = []

# Gotta remove that pastrami since we're out.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"\nMaking your {current_sandwich} sandwich...")
    
    # This is to simulate time making the sandwich.
    wait_time = [value for value in range(1, 15000000)]
    print(f"Your {current_sandwich} sandwich is ready!")

    finished_sandwiches.append(current_sandwich)

print("\n\nToday's sandwiches were:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
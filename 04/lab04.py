# 1. Name:
#      Parker Morgan
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program simulates a game of Monopoly which informs the user if
#      they are able to build a hotel on Pennsylvania avenue. It asks the user
#      multiple questions to determine how many properties they own, how many
#      houses/hotels they have, how many they need, how much money it would
#      cost them.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out they best way to format the 
#      the program that wasn't just a bunch of nested 'if' statements. I 
#      figured that putting it in a main function followed PEP8 guidelines and
#      allowed me to return from statements instead of having to break. 
#       
#      I also had particular difficulty with keeping track of which properties 
#      had which number of houses/hotels. After researching online I found that
#      the best way seemed to be to put the values into a dictionary and then 
#      use a for loop to find the specific values/names. This program really 
#      made me think outside of the box and improve my design techniques. 
# 5. How long did it take for you to complete the assignment?
#      Including reseraching, the assignment took me 3 1/2 hours.


# Main function to allow for return statements instead of breaks.
def main():

    print('Welcome to the Monopoly Program!')

    # Ask if user owns all properties.
    owns_all = input('Do you own all the green properties? (y/n) ')
    if owns_all != 'y':
        print('You cannot purchase a hotel until you own all the properties ' \
        'of a given color group.')
        return
    
    # Collect information on total houses/hotels.
    pc_houses = int(input('What is on Pacific Avenue? (0:nothing,' \
    ' 1:one house, ... 5:a hotel) '))

    nc_houses = int(input('What is on North Carolina Avenue? (0:nothing,' \
    ' 1:one house, ... 5:a hotel) '))

    pa_houses = int(input('What is on Pennsylvania Avenue? (0:nothing,' \
    ' 1:one house, ... 5:a hotel) '))

    # Create dictionary to keep track of houses/hotels on each property.
    properties = {
        'Pacific': pc_houses,
        'North Carolina': nc_houses,
        'Pennsylvania': pa_houses
    }

    # Calculate how many houses the user has and how many will be needed.      
    total_houses = 0
    total_hotels = 0
    
    for total in [pc_houses, nc_houses, pa_houses]:
        if total == 5:
            total_hotels += 1
        else:
            total_houses += total

    # Hotel-Swapping section (connection 'a' on flowchart).
    if total_hotels != 0:

        # Check if Pennsylvania has a hotel. If it doesn't, end the program.
        if pa_houses == 5:
            print('You cannot purchase a hotel if ' \
            'the property already has one.')
            return
        
        # Check which property has a hotel to swap with Pennsylvania.
        else:
            for name, value in properties.items():
                if value == 5:
                    hotel_property = name
                    break
            print(f"Swap {hotel_property}'s hotel with Pennsylvania's "
                  "4 houses.")
            return
                    
    # Determine how many houses are needed before buying hotel.
    houses_needed = 12 - total_houses
    
    # Determine if there are enough houses/hotels in the bank.
    bank_houses = int(input('How many houses are there to purchase? '))

    if bank_houses < houses_needed:
        print('There are not enough houses available '
        'for purchase at this time.')
        return
    
    # Connection 'b' on flowchart for reference. 
    bank_hotels = int(input('How many hotels are there to purchase? '))
    if bank_hotels <= 0:
        print('There are not enough hotels available '
        'for purchase at this time.')
        return
    
    # Check to see if they have enough cash.
    cash = int(input('How much cash do you have to spend? '))
    house_cost = houses_needed * 200
    hotel_cost = 200
    total_cost = house_cost + hotel_cost

    if cash < total_cost:
        print('You do not have sufficient funds ' \
        'to purchase a hotel at this time.')
        return

    # Search dictionary to see which houses are missing on each property.
    missing_houses = {name: max(0, 4 - value) for name, value in 
    properties.items()}

    print(f'This will cost ${total_cost}.\n'
          f'\tPurchase 1 hotel and {houses_needed} house(s).\n'
          f'\tPut 1 hotel on Pennsylvania and return any houses to the bank.')
    
    for name, missing in missing_houses.items():
        if name != 'Pennsylvania':
            print(f'\tPut {missing} house(s) on {name}.')

if __name__ == "__main__":
    main()
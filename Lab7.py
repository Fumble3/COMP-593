def main():
    # Initialize the complex data structure
    data_table = {
        'name': 'Mark Henderson',
        'student_id': 10204958,
        'pizza_toppings': [
            'Pepperoni',
            'Pineapple',
            'Bacon',
        ],
        'movies': [
            {'title': 'Get Hard',
            'genre': 'Comedy',
            },
            {'title': 'Deadpool',
            'genre': 'Comedy',
            }
        ]
}

# Add one more movie to the list    
    new_movie = {'title': '6 Underground', 'genre': 'Action',}
    data_table['movies'].append(new_movie)
    

def add_toppings(data_table, new_toppings):
    new_toppings = ('Olives', 'Chicken', 'Onion')
    data_table['pizza_toppings'].append(new_toppings)

    sort_toppings = sorted(data_table.keys['pizza_toppings']())
    print(sort_toppings)

def sentence(data_table):
    
    print("Hi Joe, my name is", data_table['name'],"My student ID is", data_table['student_id'])
    print('My ideal pizza has ')
    
    for d in data_table['pizza_toppings']:
        print(d)

    print('I like to watch', data_table['movies'])
   
    print('Some of my favourites are ', data_table['movies'])

main()
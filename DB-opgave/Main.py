import Article
from Location import Location
from Stockitem import StockItem


class Main:
    print("""
    Welcome to website and Stock handler program 9000
    
    Choose what you want to do!
    1 : Create a new Article
    2 : Delete an Article
    3 : Create a new Item in stock
    4 : Remove an Item from stock
    5 : Increase the quantity of an Item in stock
    6 : Decrease the quantity of an Item in stock
    """)
    initial_choice = input('Your choice : ')

    if initial_choice == '1':  # Create a new Article
        print('You have chosen to create a new article, fill in the next 3 inputs (article id have to be unique)')
        article_id = input('What is the article ID : ')
        name = input('Name of the product : ')
        description = input('Description : ')
        print('This will take about 10 seconds')

        Article.Article(article_id, name, description).new_item()
    elif initial_choice == '2':  # Delete an Article
        print('Would you like to delete an Article from the database?')
        article_id = input('What is the Article id you would like to remove : ')
        print('This will take about 10 seconds')

        Article.Article(article_id, None, None).rem_item()
    elif initial_choice == '3':  # Create a new Item in stock
        print('You chose to create a new item in stock, fill in the following values')
        article_id = input('What is the article ID (this have to match a previously created article) : ')
        name = input('Name of the product : ')
        description = input('Description : ')
        stock_item_id = input('Stock-item ID : ')
        quantity = 1
        Location.location_id = input('Location ID : ')
        Location.position = input('Position : ')
        print('This will take about 10 seconds')

        Location(Location.location_id, Location.position).new_item()
        StockItem(article_id, name, description, stock_item_id, quantity,
                  Location(Location.location_id, Location.position)).new_item()
    elif initial_choice == '4':  # Remove an Item from stock
        print('Would you like to remove an item from the Stock item database?')
        stock_item_id = input('What is the Stock-item ID you want to remove? : ')

        StockItem(None, None, None, stock_item_id, None, None).rem_item()
    elif initial_choice == '5':  # Increase the quantity of an Item in stock
        print('still under development')
    elif initial_choice == '6':  # Decrease the quantity of an Item in stock
        print('still under development')
    else:
        print('Wrong input')


Main()

# The extract_store returns the output to the object, so it has to be printed to see the result
# print(Article.Article(1, 'Razer phone', '120hz monitor, 16 GB ram').extract_store())


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create an engine that connects to the SQLite database
engine = create_engine('sqlite:///db/restaurants.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# Create a sessionmaker that will be used to handle the database session
DBSession = sessionmaker(bind=engine)

# Create sample data within a session using the with statement
with DBSession() as session:
    # Create sample restaurants with modified names
    restaurant1 = Restaurant(name="New Pizza Place", price=2)
    restaurant2 = Restaurant(name="New Fine Dining", price=4)

    # Create sample customers with modified names
    customer1 = Customer(first_name="Alice", last_name="Smith")
    customer2 = Customer(first_name="Bob", last_name="Johnson")

    # Create sample reviews
    review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)
    review3 = Review(star_rating=4, restaurant=restaurant2, customer=customer1)

    # Add the objects to the session
    session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])

# Once the block of code is executed, the session is automatically committed and closed
print("Database seeded!")



import datetime
from faker import Faker

# pip install faker
from books.models import Author, Publisher, Book

faker = Faker('pl_PL')

def generate_authors(n):
    for i in range(n):
        first_name = faker.first_name()
        last_name = faker.last_name()
        birth_date = faker.date_of_birth()
        death_date = faker.date_this_century()
        description = faker.text(1000)
        Author.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date, death_date=death_date, description=description)

    print(f'Created {n} authors')

def generate_publishers(n):
    for i in range(n):
        name = faker.company()
        Publisher.objects.create(name=name)

    print(f'Created {n} publishers')

def generate_books(n):
    all_publishers = Publisher.objects.all()
    all_authors = Author.objects.all()

    for i in range(n):
        title = faker.sentence()
        pages = faker.random_int(10, 500)
        price = faker.pydecimal(2,2,positive=True)
        rating = faker.pydecimal(1,2,positive=True)
        authors = faker.random_choices(all_authors, length=faker.random_int(1,3))
        publisher = faker.random_choices(all_publishers, length=1)[0]
        pub_date = faker.date_this_decade()

        book = Book(title=title, pages=pages, price=price, rating=rating, publisher=publisher, pub_date=pub_date)
        book.save()

        # in purpose of many-to-many relation
        for a in authors:
            book.authors.add(a)

    print(f'Created {n} books')

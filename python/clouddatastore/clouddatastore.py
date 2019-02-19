import os
import uuid
from dotenv import load_dotenv
from google.cloud import datastore
import datetime

PROJECT_ID = os.environ.get('GCP_PROJECT_ID')

def add_record():
    cl = client()

    books = []
    for i in range(10):
        key = cl.key('Book', f'book_{uuid.uuid4()}')
        book = datastore.Entity(key=key)
        book.update({
            'title': f'book-{i}',
            'author': f'author-{i}',
            'date': datetime.datetime.utcnow()
        })

        books.append(book)


    cl.put_multi(books)

def get_record_by_id(id):
    cl = client()
    key = cl.key('Book', id)

    query = cl.query(kind='Book')
    query.key_filter(key, operator='=')

    result = list(query.fetch(1))[0]

    return to_book(result)

def get_latest(num):
    cl = client()

    query = cl.query(kind='Book', order=['date'])
    result = query.fetch(limit=num)

    return [to_book(b) for b in list(result)]

def client():
    return datastore.Client(PROJECT_ID)

def to_book(obj):
    return {
        "key": obj.key,
        "title": obj.get('title', ''),
        "author": obj.get('author', ''),
        "date": obj.get('date', None)
    }

if __name__ == '__main__':
    dotenv_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path)

    b = get_latest(10)
    print(b)

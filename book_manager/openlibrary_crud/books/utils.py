import requests

def fetch_book_data(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Alguns livros têm autores separados em outra requisição
        authors = []
        for author in data.get('authors', []):
            # Cada author tem um 'key', precisamos buscar o nome
            author_response = requests.get(f"https://openlibrary.org{author['key']}.json")
            if author_response.status_code == 200:
                authors.append(author_response.json().get('name', ''))
        return {
            'title': data.get('title', ''),
            'author': ', '.join(authors),
            'publish_date': data.get('publish_date', None),
            'isbn': isbn,
            'cover_image': f"http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"  # URL padrão de capa
        }
    return None

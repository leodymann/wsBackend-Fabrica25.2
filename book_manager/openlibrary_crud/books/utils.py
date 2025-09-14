import requests

def fetch_books_by_title(title):
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = []
        for doc in data.get('docs', [])[:10]:
            results.append({
                'title': doc.get('title', ''),
                'author': ', '.join(doc.get('author_name', [])),
                'published_date': str(doc.get('first_publish_year', '')),
                'isbn': doc.get('isbn', [None])[0] if doc.get('isbn') else None,
                'cover_image': f"http://covers.openlibrary.org/b/isbn/{doc.get('isbn', [None])[0]}-L.jpg" if doc.get('isbn') else None
            })
        return results
    return []

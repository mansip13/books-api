from flask import Flask, request

app = Flask(__name__)

books = []

# Get all books
@app.get('/books')
def get_books():
    return {"books": books}, 200

# Get one book by ID
@app.get('/books/<int:id>')
def get_one_book(id):
    if id < 0 or id >= len(books):
        return {"error": "Book not found"}, 404
    return books[id], 200

# Add a new book
@app.post('/books')
def create_book():
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return {"error": "Missing 'title' or 'author'"}, 400
    new_book = {
        "id": len(books),
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return new_book, 201

# Update a book by ID
@app.put('/books/<int:id>')
def update_book(id):
    if id < 0 or id >= len(books):
        return {"error": "Book not found"}, 404
    data = request.get_json()
    if not data:
        return {"error": "Missing data"}, 400
    books[id].update({k: v for k, v in data.items() if k in ["title", "author"]})
    return books[id], 200

# Delete a book by ID
@app.delete('/books/<int:id>')
def delete_book(id):
    if id < 0 or id >= len(books):
        return {"error": "Book not found"}, 404
    deleted = books.pop(id)
    return {"deleted": deleted}, 200

if __name__ == "__main__":
    app.run(debug=True)

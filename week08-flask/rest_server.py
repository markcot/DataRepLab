from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
   return "hello"

books = [
   {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
   {"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
   {"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 3000}
]
nextId = 4

# Get All
#curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
   return jsonify(books)

# find By id
@app.route('/books/<int:id>')
def findById(id):
   return "served by find by id with id " + str(id)

# create
@app.route('/books', methods=['POST'])
def create():
   return "served by Create"

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
   return "served by update with id " + str(id)

# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
   return "served by delete with id " + str(id)

if __name__ == "__main__":
   app.run(debug=True)
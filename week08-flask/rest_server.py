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
#curl http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>')
def findById(id):
   foundBooks = list(filter (lambda t : t["id"]==id, books))
   if len(foundBooks) == 0:
      return jsonify({}), 204
   return jsonify(foundBooks[0])

# create
# This results in a 400 bad request due to abort not json object type
#curl -X POST -d "{\"id\":4, \"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
# This results in a 200 OK request as object type is json
#curl -H "Content-Type:application/json" -X POST -d "{\"id\":4, \"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
   global nextId
   if not request.json:
      abort(400)

   book = {
      "id": nextId,
      "Title": request.json["Title"],
      "Author": request.json["Author"],
      "Price": request.json["Price"]
   }
   books.append(book)
   nextId += 1
   return jsonify(book)

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
   return "served by update with id " + str(id)

# delete
# curl -X DELETE http://127.0.0.1:5000/books/4
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
   return "served by delete with id " + str(id)

if __name__ == "__main__":
   app.run(debug=True)

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
   return "hello"

# Get All
@app.route('/books')
def getAll():
   return "served by Get All()"

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
   return "served by update with id" + str(id)

# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
   return "served by delete with id" + str(id)

if __name__ == "__main__":
   app.run(debug=True)
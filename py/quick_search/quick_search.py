from flask import Flask, jsonify
from re import search
import wikipediaapi

app = Flask(__name__)

# Get the main page that allows to make search using the API itself
@app.route('/')
def home():
    return "<p>Will be implemented in the next iterations</p>"

# Get the documentation page of the API
@app.route('/docs')
def getDocs():
    return "<p>Will be implemented in the next iterations</p>"

# Search for a word
@app.route('/search/<expression>/<lang>')
def searchExpression(expression : str, lang : str):
    # The expression is expected to be without blank with underscores
    # at the place of these.
    if search(" ", expression):
        expression.replace(" ", "_")
    
    # Search at Wikipedia
    w = wikipediaapi.Wikipedia(lang)
    page = w.page(expression)
    if page.exists():
        response = {
            "wikipedia": {
                "title": page.title,
                "summary": page.summary, 
                "url": page.fullurl
            }
        }
        return jsonify(response), 201
    return {"error": "The searched page does not exist"}, 404

if __name__ == "__main__":
    app.run(debug=True)

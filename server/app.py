from flask import Flask, jsonify, make_response
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))   

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')

@app.route('/hello')
def hello():
    response = jsonify(message='Hello, has been called')
    return response

@app.route("/generateCat")
def generateCat():
    print("running generate cat")
    response = client.images.generate(
    model="dall-e-3",
    prompt="Make a comic book style image of a super hero cat in a super hero costume fighting a villan.",
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    print(image_url)
    
    return jsonify(message=image_url)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == '__main__':
    app.run(debug=True)

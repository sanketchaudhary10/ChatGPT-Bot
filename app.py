from flask import Flask, render_template, request
import openai
import os


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ],
        max_tokens=200,
        temperature=0.9,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0.7,
    )
    if responses.choices[0].message!=None:
        return responses.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

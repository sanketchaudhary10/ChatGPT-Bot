from flask import Flask, render_template, request
import openai
import os


app = Flask(__name__)

openai.api_key = "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"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    # Getting message from the POST request
    message = request.json.get("message")
    # Sending message to OpenAI's API and receiving response
    
    
    responses = openai.Completion.create(
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

from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def index():
    code = None
    title = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python code generator assistant. You generate Python classes based on user's request, inheriting from 'Task' and having 'run' and 'calculate_score' methods."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        code = answer.strip()
        title = "Generated Python Class"
    return render_template("index.html", code=code, title=title)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

def add(a, b):
    return a + b

# Run the development server (only if executed directly)
if __name__ == "__main__":
    app.run(debug=True)


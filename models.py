from flask import Flask

app = Flask(__name__)

#Base route

@app.route('/')
def index():
    
    return {"message": "Welcome to the API"}

if __name__ == '__main__':
    app.run(debug=True)
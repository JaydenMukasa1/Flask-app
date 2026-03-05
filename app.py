from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
    return "Welcome to my Flask app!"

@app.route('/count')
def count():
    visits = r.incr('count')
    return f'Visit count: {visits}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
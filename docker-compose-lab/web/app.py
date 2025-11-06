from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    try:
        count = r.incr('counter')
    except Exception as e:
        print("Redis baglanti hatasi:", e)
        count = 'Redis baglanti hhatasi'
    return f"Hello! This page has been visited {count} times./n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

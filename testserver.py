import time

from flask import Flask  # 간단히 플라스크 서버를 만든다
import random
import urllib.request

app = Flask(__name__)




def rand():
    rands= random.randint(1,100)
    print(rands)
    return rands


@app.route("/tospring")
def spring():

    a=str(rand())
    return a


if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=5000)
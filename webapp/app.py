import os
import bugsnag

from flask import Flask

app = Flask(__name__)

bugsnag.configure(
    api_key="8fb4eae6257a8ef2260c41ee758c3033",
    project_root="/webapp/",
)

@app.route('/')
def hello():
    bugsnag.notify(Exception('Test error'))
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

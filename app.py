from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch system details
    full_name = "Durgesh Patel"
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format as HTML response
    return f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

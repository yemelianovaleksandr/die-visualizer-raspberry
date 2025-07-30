from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
import uuid
import threading
import time
from random import random

app = Flask(__name__)

# Delete file after 60 seconds
def delete_file_later(path, delay=60):
    def _delete():
        time.sleep(delay)
        if os.path.exists(path):
            os.remove(path)
    threading.Thread(target=_delete, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll')
def roll():
    user_input = request.args.get('rolls', default=1000, type=int)

    if user_input < 100 or user_input > 5_000_000:
        return render_template('error.html', message="Please enter a number between 100 and 5,000,000")

    frames = min(100, max(1, user_input // 1000))
    rolls_per_frame = max(1, user_input // frames)
    actual_total = frames * rolls_per_frame

    # Generate unique filename
    file_id = str(uuid.uuid4())
    video_name = f"die_{file_id}.mp4"
    video_path = os.path.join("app/static", video_name)

    # Run video generation script
    subprocess.run([
        'python3',
        'app/die_anim.py',
        str(frames),
        str(rolls_per_frame),
        str(actual_total),
        str(user_input),
        video_path
    ])

    # Schedule deletion of the file
    delete_file_later(video_path)

    # Redirect to result page with filename
    return redirect(url_for('result', file=video_name))

@app.route('/result')
def result():
    filename = request.args.get('file')
    return render_template('result.html', filename=filename, rand=random())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

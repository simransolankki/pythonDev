from flask import Flask, render_template

app = Flask(__name__)

# Mock data for video listings
contents = [
    {"id": 1, "video": "videos/1.mp4", "thumbnail": "thumbnails/1.jpg"},
    {"id": 2, "video": "videos/2.mp4", "thumbnail": "thumbnails/2.jpg"},
    {"id": 3, "video": "videos/3.mp4", "thumbnail": "thumbnails/3.jpg"},
    {"id": 4, "video": "videos/4.mp4", "thumbnail": "thumbnails/4.jpg"},
    {"id": 5, "video": "videos/5.mp4", "thumbnail": "thumbnails/5.jpg"},
    {"id": 6, "video": "videos/6.mp4", "thumbnail": "thumbnails/6.jpg"}
]

@app.route('/')
def home():
    return render_template('home.html', contents=contents)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

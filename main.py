from flask import Flask, render_template
import random

app = Flask(__name__)

# Mock data for drama movie listings
contents = [
    {
        "id": 1,
        "title": "Example Drama 1",
        "description": "Description of Example Drama 1.",
        "thumbnail": "thumbnails/thumbnail1.jpg",
        "preview": "videos/video1.mp4",
        "full_video": "videos/full_video1.mp4"
    },
    {
        "id": 2,
        "title": "Example Drama 2",
        "description": "Description of Example Drama 2.",
        "thumbnail": "thumbnails/thumbnail2.jpg",
        "preview": "videos/video2.mp4",
        "full_video": "videos/full_video2.mp4"
    },
    {
        "id": 1,
        "title": "Example Drama 1",
        "description": "Description of Example Drama 1.",
        "thumbnail": "thumbnails/thumbnail1.jpg",
        "preview": "videos/video1.mp4",
        "full_video": "videos/full_video1.mp4"
    },
    {
        "id": 2,
        "title": "Example Drama 2",
        "description": "Description of Example Drama 2.",
        "thumbnail": "thumbnails/thumbnail2.jpg",
        "preview": "videos/video2.mp4",
        "full_video": "videos/full_video2.mp4"
    },{
        "id": 1,
        "title": "Example Drama 1",
        "description": "Description of Example Drama 1.",
        "thumbnail": "thumbnails/thumbnail1.jpg",
        "preview": "videos/video1.mp4",
        "full_video": "videos/full_video1.mp4"
    },
    {
        "id": 2,
        "title": "Example Drama 2",
        "description": "Description of Example Drama 2.",
        "thumbnail": "thumbnails/thumbnail2.jpg",
        "preview": "videos/video2.mp4",
        "full_video": "videos/full_video2.mp4"
    },{
        "id": 1,
        "title": "Example Drama 1",
        "description": "Description of Example Drama 1.",
        "thumbnail": "thumbnails/thumbnail1.jpg",
        "preview": "videos/video1.mp4",
        "full_video": "videos/full_video1.mp4"
    },
    {
        "id": 2,
        "title": "Example Drama 2",
        "description": "Description of Example Drama 2.",
        "thumbnail": "thumbnails/thumbnail2.jpg",
        "preview": "videos/video2.mp4",
        "full_video": "videos/full_video2.mp4"
    }
    # Add more contents as needed
]

@app.route('/')
def home():
    random.shuffle(contents)
    return render_template('index.html', contents=contents)

@app.route('/content/<int:content_id>')
def content_detail(content_id):
    content = next((item for item in contents if item["id"] == content_id), None)
    return render_template('content.html', content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

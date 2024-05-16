from flask import Flask, request, jsonify
import single
import cv2 as cv
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # If the user submits an empty part without a file, ignore it
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file to the uploads folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    
    img = cv.imread('uploads/img.jpg')
    img = single.process(img)
    print("=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-===-=-")
    return img

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        # Receive the image from the client.
        image_blob = request.files['image'].read()
        
        # Process the image using OpenCV.
        measurements = process_image(image_blob)
        
        return jsonify({'measurements': measurements})
    except Exception as e:
        return jsonify({'error': str(e)})

# Function to process the image using OpenCV.
def process_image(image_blob):
    # Convert the image data to a NumPy array.
    image_np = np.frombuffer(image_blob, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    
    # Perform image processing and measurements (you need to implement this part).
    # Example: Convert the image to grayscale and calculate dimensions.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape[0], gray_image.shape[1]
    
    # Return the measurements as a dictionary.
    measurements = {'height': height, 'width': width}
    return measurements

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

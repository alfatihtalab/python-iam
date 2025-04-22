from flask import Flask, jsonify
import boto3

app = Flask(__name__)

# Initialize S3 client (credentials pulled from EC2 instance IAM role)
s3 = boto3.client('s3')

@app.route('/')
def index():
    return "Hello from Flask app in Docker!"

@app.route('/upload')
def upload_file():
    try:
        bucket_name = 'meetswap-rr1'
        key = 'media/reporting/hello-from-docker-python.txt'
        body = 'This file was uploaded using Python Flask app running in Docker on EC2.'

        s3.put_object(Bucket=bucket_name, Key=key, Body=body, ContentType='text/plain')

        return jsonify({
            "message": "File uploaded successfully!",
            "bucket": bucket_name,
            "key": key
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

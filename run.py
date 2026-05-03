from app import create_app
import boto3

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port="9544", host="0.0.0.0")
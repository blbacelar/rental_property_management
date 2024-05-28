# Rental Property Management

This project is a Flask application for managing rental properties. It includes functionality for property and tenant management, JWT-based authentication, and image uploads to AWS S3.

## Features

- Property management
- Tenant management
- JWT authentication
- Image uploads to AWS S3

## Setup

### Prerequisites

- Python 3.8 or higher
- AWS account with S3 bucket
- Virtual environment tool (e.g., `venv`, `virtualenv`)

### Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```plaintext
S3_BUCKET=your_bucket_name
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=your_aws_region
SECRET_KEY=your_flask_secret_key
JWT_SECRET_KEY=your_jwt_secret_key

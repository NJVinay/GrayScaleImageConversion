# Grayscale Image Conversion


A serverless image processing service that converts color images to grayscale using AWS infrastructure.

## Overview

This project implements an image conversion service deployed on AWS, leveraging serverless architecture for scalability and cost-efficiency.

## Architecture

- **AWS Lambda**: Hosts the grayscale conversion function
- **Amazon S3**: Stores input and output images
- **API Gateway**: Provides HTTP endpoint for image upload
- **Additional AWS Services**: IAM for permissions, CloudWatch for monitoring

## Features

- Convert color images to grayscale (PNG format)
- Serverless architecture for automatic scaling
- Load testing with Locust for performance validation

## Files

- `grayscale_converter.py` - Core image conversion logic using PIL
- `locust_grayscale_benchtest.py` - Load testing script

## Usage

Upload an image to the API endpoint:

```bash
POST /convert-to-grayscale
Content-Type: multipart/form-data
```

The service returns a grayscale version of the uploaded image.

## Requirements

- Python 3.x
- PIL/Pillow
- Locust (for testing)

## Deployment

Deployed as an AWS Lambda function with S3 integration for image storage and API Gateway for HTTP access.

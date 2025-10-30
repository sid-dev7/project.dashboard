#!/bin/bash
aws s3 cp ../frontend/ s3://your-bucket-name/ --recursive --acl public-read
import boto3
import argparse
import json

parser = argparse.ArgumentParser(description='Basic deep neural network that works with SVM input')
parser.add_argument('--bucket', required=True, help='Bucket name', metavar='#')
args = parser.parse_args()

s3 = boto3.resource('s3')

videos = []
for file in s3.Bucket(args.bucket).objects.all():
    key = file.key

    # Skip non .mp4 and non first-level files
    if key.lower().endswith('.mp4') and "/" in key:
        videos.append({"name": key, "size": file.size})

json.dump(videos, open('manifest.json', 'w'))
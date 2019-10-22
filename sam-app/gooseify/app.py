import boto3
import os
import tempfile
from pydub import AudioSegment

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        process_record(record['s3'])

def process_record(record):
    key = record['object']['key']
    bucket = record['bucket']['name']

    if key.startswith("improved/"):
        return

    watermark = AudioSegment.from_file('honk-extended.mp3')

    with tempfile.TemporaryFile() as f:
        print(f"Getting: {key} from {bucket}")
        s3.download_fileobj(bucket, key, f)
        f.seek(0)

        AudioSegment.from_file(f).overlay(watermark, loop=True, position=1000).export(f"/tmp/{key}")

    with open(f"/tmp/{key}", "rb") as file:
        s3.put_object(Bucket=record['bucket']['name'], Key=f"improved/{key}", Body=file.read())

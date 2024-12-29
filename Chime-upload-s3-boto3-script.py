import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
###from amazon_chime_sdk.media_recordings import *

class ChimeAudioUploader:
    def __init__(self, region_name='us-east-1'):
        # Configure AWS SDK
        self.s3_client = boto3.client('s3', 
            config=Config(region_name=region_name)
        )
        self.chime_recordings_client = boto3.client('chime-sdk-media-pipelines',
            config=Config(region_name=region_name)
        )

        ###self.chime_recordings_client = ChimeMediaRecordingsClient()

    def upload_audio_to_s3(self, audio_file_path, bucket_name, s3_key):
        """
        Upload a recorded audio file to S3 using Chime SDK
        
        :param audio_file_path: Local path to the audio file
        :param bucket_name: Name of the S3 bucket
        :param s3_key: Destination path in S3
        :return: S3 object URL or None if upload fails
        """
        try:
            # Upload file to S3
            self.s3_client.upload_file(
                Filename=audio_file_path,
                Bucket=bucket_name, 
                Key=s3_key
            )
            
            # Get the object URL
            object_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
            return object_url
        
        except ClientError as e:
            print(f"Error uploading audio file: {e}")
            return None

    def record_and_upload(self, bucket_name, s3_key, recording_duration=60):
        """
        Record audio using Chime SDK and upload to S3
        
        :param bucket_name: S3 bucket name
        :param s3_key: S3 destination path
        :param recording_duration: Recording length in seconds
        :return: S3 object URL or None
        """
        try:
            # Start audio recording
            recording = self.chime_recordings_client.start_media_recording(
                MediaRecordingConfiguration={
                    'AudioConfiguration': {
                        'AudioRecordingDurationInSeconds': recording_duration
                    }
                }
            )
            
            # Wait for recording to complete
            recording_file_path = recording.get_media_recording_file()
            
            # Upload recorded file to S3
            return self.upload_audio_to_s3(
                recording_file_path, 
                bucket_name, 
                s3_key
            )
        
        except Exception as e:
            print(f"Recording or upload failed: {e}")
            return None

# Example usage
if __name__ == "__main__":
    uploader = ChimeAudioUploader()
    
    # Option 1: Upload existing audio file
    s3_url = uploader.upload_audio_to_s3(
        'W:\My Documents\SA\Green\Transcribe\Audio-File.m4a', 
        'vs8624-transcribe-incoming-bucket2', 
        ###'recordings/meeting.wav',
        s3_key='11af09e5-e30b-4ad2-bf8e-446c7ab71a05'
    )
    
    # Option 2: Record and upload directly
    #recorded_s3_url = uploader.record_and_upload(
     #   'my-audio-bucket', 
      #  'recordings/new_meeting.wav',
       # recording_duration=60  # 1-minute recording
    #)
    print ("Test")
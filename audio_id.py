import hashlib

# Read the MP3 file contents
with open('idmp3.mp3', 'rb') as f:
    audio_data = f.read()

# Generate the SHA-256 hash
hash_object = hashlib.sha256(audio_data)
blockchain_id = hash_object.hexdigest()

print(f'Blockchain ID for the audio file: {blockchain_id}')
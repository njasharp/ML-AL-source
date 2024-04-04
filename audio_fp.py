import numpy as np
from pydub import AudioSegment
import hashlib
from Levenshtein import distance

# Audio fingerprinting function
def generate_fingerprint(audio_data):
    # Convert audio data to numpy array
    audio_array = np.array(audio_data.get_array_of_samples())

    # Calculate the spectral centroid
    spectral_centroid = np.mean(np.abs(np.fft.fft(audio_array)))

    # Calculate the root mean square (RMS) energy
    rms_energy = np.sqrt(np.mean(audio_array ** 2))

    # Combine spectral centroid and RMS energy into a fingerprint
    fingerprint = f"{spectral_centroid:.6f}_{rms_energy:.6f}"

    return fingerprint

# Load the audio file
audio_file = AudioSegment.from_file("audio_file.wav", format="wav")

# Generate the audio fingerprint
audio_fingerprint = generate_fingerprint(audio_file)

# Generate the blockchain ID
audio_data = audio_file.raw_data
blockchain_id = hashlib.sha256(audio_data).hexdigest()

# Fingerprint database (simulated)
fingerprint_database = {
    "audio1": ("fingerprint1", "blockchain_id1"),
    "audio2": ("fingerprint2", "blockchain_id2"),
    # Add more entries as needed
}

# Check if the blockchain ID is being copied
for audio_name, (fingerprint, blockchain_id_db) in fingerprint_database.items():
    # Calculate the Levenshtein distance between fingerprints
    fingerprint_distance = distance(audio_fingerprint, fingerprint)

    # Define a similarity threshold
    similarity_threshold = 0.2

    # Check if the fingerprints are similar
    if fingerprint_distance <= similarity_threshold:
        # Check if the blockchain IDs match
        if blockchain_id_db != blockchain_id:
            print(f"Potential copy detected for audio {audio_name}!")
            print(f"Blockchain ID mismatch: {blockchain_id_db} != {blockchain_id}")
        else:
            print(f"Audio {audio_name} is a legitimate copy.")
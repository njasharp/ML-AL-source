import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding

# Load the audio file
audio_file = 'song.mp3'
y, sr = librosa.load(audio_file)

# Extract features from the audio signal
mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)

# Reshape the features for the model input
inputs = mel_spectrogram.reshape(-1, mel_spectrogram.shape[1], 1)

# Define the model architecture
model = Sequential([
    Embedding(input_dim=inputs.max() + 1, output_dim=128),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(inputs.max() + 1, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(inputs, inputs, epochs=10, batch_size=32)

# Get the embedding layer
embedding_layer = model.layers[0]

# Get the embeddings for the input audio
embeddings = embedding_layer.get_weights()[0]
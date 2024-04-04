from pydub import AudioSegment
import os

# Set the path to ffmpeg executable directly
ffmpeg_path = r'D:\pythxn_class\pgm\ffmpeg\ffmpeg-2024-03-20-git-e04c638f5f-essentials_build\bin\ffmpeg.exe'
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
AudioSegment.converter = ffmpeg_path

# Now you can use pydub functionalities, for example, loading an MP3 file
# song = AudioSegment.from_mp3("your_audio_file.mp3")
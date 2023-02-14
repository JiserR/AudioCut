import moviepy.editor
from pathlib import Path

Movie_name = input("Введите имя файла с расширением .mp4: ")
video_file = Path(Movie_name)

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')

print("Аудиофайл находится рядом с исходником видео")
import os
from moviepy.editor import VideoFileClip
import eyed3

def convert_mp4_to_mp3(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name[0] == '1':
            mp4_path = os.path.join(input_folder, file_name)
            mp3_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".mp3")

            # Convert mp4 to mp3 using moviepy
            video_clip = VideoFileClip(mp4_path)
            video_clip.audio.write_audiofile(mp3_path)
            video_clip.close()

            # Set metadata using eyed3
            audiofile = eyed3.load(mp3_path)
            audiofile.tag.artist = "田馥甄"
            audiofile.tag.album = "《一一》第一天"
            audiofile.tag.save()

input_folder = "/Volumes/Passport/Hebe_Tien_Day1/MP4"
output_folder = "/Users/chenwei/Desktop/music"

convert_mp4_to_mp3(input_folder, output_folder)

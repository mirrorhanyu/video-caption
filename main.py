# from moviepy.editor import *
# from moviepy.video.tools.subtitles import SubtitlesClip
#
# generator = lambda txt: TextClip(txt, font='./fonts/GothamMedium.ttf', fontsize=35, color='white', bg_color='#00000066')
# subtitles = SubtitlesClip("Remembering When Coronavirus Was Contained - The Daily Show.en.srt", generator).margin(bottom=15, opacity=0).set_position(('center', 'bottom'))
#
# video = VideoFileClip("Remembering When Coronavirus Was Contained - The Daily Show.webm", audio=True)
# result = CompositeVideoClip([video, subtitles])
#
# result.write_videofile("out.mp4",
#                        threads=4,
#                        fps=video.fps,
#                        temp_audiofile="temp-audio.m4a",
#                        remove_temp=True,
#                        audio_codec="aac")
import os

from bilibiliupload import *

b = Bilibili()
print(b.login(os.getenv('BILIBILI_USERNAME', ''), os.getenv('BILIBILI_PASSWORD', '')))

from typing import Callable, Any

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.margin import margin


def add_subtitle(video_path, subtitle_path):
    generator: Callable[[Any], TextClip] = lambda txt: TextClip(txt,
                                                                font='./fonts/GothamMedium.ttf',
                                                                fontsize=45, color='white',
                                                                bg_color='#00000066')
    subtitle = margin(clip=SubtitlesClip(subtitle_path, generator).set_position(('center', 'bottom')), bottom=35,
                      opacity=0)
    video = VideoFileClip(video_path, audio=True)
    composed_video = CompositeVideoClip([video, subtitle])
    composed_video.write_videofile("out.mp4",
                                   threads=4,
                                   fps=video.fps)


add_subtitle(video_path="Cleaning for Coronavirus - The Daily Show.mp4",
             subtitle_path="Cleaning for Coronavirus - The Daily Show.en-US.srt")

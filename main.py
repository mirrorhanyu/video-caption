from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.margin import margin

generator = lambda txt: TextClip(txt, font='./fonts/GothamMedium.ttf', fontsize=45, color='white', bg_color='#00000066')
subtitles = margin(SubtitlesClip("Remembering When Coronavirus Was Contained - The Daily Show.en.srt", generator).set_position('center', 'bottom'), bottom=45, opacity=0)

video = VideoFileClip("Remembering When Coronavirus Was Contained - The Daily Show.webm", audio=True)
result = CompositeVideoClip([video, subtitles])

result.write_videofile("out.mp4",
                       threads=2,
                       fps=video.fps)

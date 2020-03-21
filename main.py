from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

from notify import send_email

generator = lambda txt: TextClip(txt, font='Arial', fontsize=16, color='white')
subtitles = SubtitlesClip("Wow! Trump Makes Coronavirus Racist - The Daily Show.en.srt", generator)

video = VideoFileClip("Wow! Trump Makes Coronavirus Racist - The Daily Show.mp4")
result = CompositeVideoClip([video, subtitles.set_position(('center','bottom'))])

result.write_videofile("out.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

send_email(from_address=os.getenv('GOOGLE_EMAIL_USERNAME', ''),
           to_address=os.getenv('GOOGLE_NOTIFIED_EMAIL', ''),
           subject='Caption',
           text='Done!',
           attachments=['out.mp4'])

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

from notify import send_email

generator = lambda txt: TextClip(txt, font='Arial', fontsize=70, color='white')
subtitles = SubtitlesClip("Cleaning for Coronavirus - The Daily Show.en-US.srt", generator)

video = VideoFileClip("Cleaning for Coronavirus - The Daily Show.mp4")
result = CompositeVideoClip([video, subtitles.set_position(('center','bottom'))])

result.write_videofile("out.mp4")

send_email(from_address=os.getenv('GOOGLE_EMAIL_USERNAME', ''),
           to_address=os.getenv('GOOGLE_NOTIFIED_EMAIL', ''),
           subject='Caption',
           text='Done!',
           attachments=['out.mp4'])


from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

def  collect_transcript(input_video):
    
    youtube_video = input_video
    video_id = youtube_video.split("=")[1]
    #YouTubeVideo(video_id)

    transcript=""

    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)


    result = ""
    for i in transcript:
        result += ' ' + i['text']

    return result    



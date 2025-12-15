# app/services/youtube_service.py

from googleapiclient.discovery import build
from app.core.config import settings

# genai.configure(api_key=settings.YOUTUBE_API_KEY)

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def find_youtube_video(query: str):
    """
    Finds a single relevant YouTube video for a given query.
    """
    if not settings.YOUTUBE_API_KEY:
        print("Warning: YOUTUBE_settings.YOUTUBE_API_KEY is not set. Skipping YouTube.")
        return None

    try:
        # Initialize the YouTube API client
        youtube = build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=settings.YOUTUBE_API_KEY
        )

        # Use the 'youtube' object to make the search request
        print(query)
        search_response = youtube.search().list(
            q=f"{query}",
            part="snippet",
            maxResults=1,
            type="video",
            # regionCode='ID',
            relevanceLanguage="id"
        ).execute()

        search_results = search_response.get("items", [])
        if not search_results:
            print(f"No YouTube video found for query: {query}")
            return None

        first_result = search_results[0]
        video_id = first_result["id"]["videoId"]
        video_title = first_result["snippet"]["title"]
        channel_title = first_result["snippet"]["channelTitle"]
        
        return {
            "videoId": video_id,
            "title": video_title,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "channel": channel_title
        }


    except Exception as e:
        print(f"An error occurred with YouTube API: {e}")
        return None

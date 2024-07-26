import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import os
from dotenv import load_dotenv

class YouTubePlaylist:
    def __init__(self, url):
        # Extract the playlist ID from the provided URL
        query = parse_qs(urlparse(url).query, keep_blank_values=True)
        self.playlist_id = query["list"][0]
        
        # Load the API key from the .env file
        load_dotenv()
        self.api_key = os.getenv("YOUTUBE_API_KEY")
        
        # Build the YouTube API client using the API key
        self.youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.api_key)
        
    def get_playlist_items(self):
        # Create an API request to get playlist items
        request = self.youtube.playlistItems().list(
            part="snippet",
            playlistId=self.playlist_id,
            maxResults=50  # Maximum number of results to return per request
        )
        
        playlist_items = []
        while request is not None:
            # Execute the request and get the response
            response = request.execute()
            # Add the items from the response to the playlist_items list
            playlist_items += response["items"]
            # Get the next page of results, if available
            request = self.youtube.playlistItems().list_next(request, response)
        
        # Extract the video links from the playlist items
        links = [
            f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={self.playlist_id}'
            for t in playlist_items
        ]
        return links

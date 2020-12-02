import logging
import os
import sys

from dotenv import load_dotenv
import pyyoutube
import subprocess

load_dotenv()

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class GoGoGo:
    
    def __init__(self):
        self.yt_client = pyyoutube.Api(api_key=os.getenv('YOUTUBE_GOOGLE_API'))

    def get_playlist(self, video_count=None):
        playlist_items = self.yt_client.get_playlist_items(
            playlist_id=os.getenv('PLAYLIST_ID'),
            count=video_count,
            return_json=True
        )['items']
        logger.debug(f'len(playlist_items): {len(playlist_items)}')

        return playlist_items

    def create_clip(self, video_id, duration=5, start=None):
        url_base = 'https://www.youtube.com/watch?v='

        video_url = f'{url_base}{video_id}'
        logger.debug(video_url)


if __name__ == '__main__':
    from pprint import pprint

    ggg = GoGoGo()
    pl = ggg.get_playlist(video_count=10)
    pprint(pl)
    for vid in pl:
        print('VID:')
        pprint(vid)
        ggg.create_clip(vid)
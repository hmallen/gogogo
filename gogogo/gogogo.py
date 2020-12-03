import json
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
        self.yt_client = pyyoutube.Api(api_key=os.getenv("YOUTUBE_GOOGLE_API"))

        if not os.path.exists("bin_paths.json"):
            logger.info("Could not find binary path json file. Creating new.")
            with open("bin_paths.json", "a+") as json_file:
                json_file.write(
                    json.dumps(
                        {
                            "ffmpeg": subprocess.run(
                                "which ffmpeg", shell=True, capture_output=True
                            )
                            .stdout.decode("utf-8")
                            .rstrip("\n"),
                            "youtube-dl": subprocess.run(
                                "which youtube-dl", shell=True, capture_output=True
                            )
                            .stdout.decode("utf-8")
                            .rstrip("\n"),
                        }
                    )
                )

        with open("bin_paths.json", "r") as bin_json:
            json_data = json.load(bin_json)

        self.ffmpeg_path = json_data["ffmpeg"]
        logger.debug(f"self.ffmpeg_path: {self.ffmpeg_path}")
        self.youtubedl_path = json_data["youtube-dl"]
        logger.debug(f"self.youtubedl_path: {self.youtubedl_path}")

        if self.ffmpeg_path == "":
            print(
                "Could not find ffmpeg binary executable. Please install before continuing."
            )
            sys.exit(1)

        if self.youtubedl_path == "":
            print(
                "Could not find youtube-dl binary executable. Please install before continuing."
            )
            sys.exit(1)

        if not os.path.exists("clips/"):
            os.makedirs("clips/")

    def get_playlist(self, video_count=None):
        playlist_items = self.yt_client.get_playlist_items(
            playlist_id=os.getenv("PLAYLIST_ID"), count=video_count, return_json=True
        )["items"]
        logger.debug(f"len(playlist_items): {len(playlist_items)}")

        return playlist_items

    def create_clip(self, video_details, clip_duration=3, clip_start=0):
        video_id = video_details["videoId"]
        logger.debug(f'video_id: {video_id}')

        video_datetime = video_details['videoPublishedAt']
        logger.debug(f'video_datetime: {video_datetime}')

        video_url = f"https://www.youtube.com/watch?v={video_id}"
        logger.debug(video_url)

        clip_start_padded = f"{clip_start:02}"
        logger.debug(f"clip_start_padded: {clip_start_padded}")

        clip_end = clip_start + clip_duration
        logger.debug(f"clip_end: {clip_end}")

        clip_end_padded = f"{clip_end:02}"
        logger.debug(f"clip_end_padded: {clip_end_padded}")

        clip_name = f"{video_id}.mp4"
        logger.debug(f"clip_name: {clip_name}")

        ffmpeg_process = subprocess.run(
            f'{self.ffmpeg_path} -ss 00:00:{clip_start_padded} -to 00:00:{clip_end_padded} -i "$({self.youtubedl_path} -f best --get-url https://www.youtube.com/watch?v={video_id})" -c:v copy -c:a copy -n clips/{video_datetime}_{video_id}.mp4',
            shell=True,
        )
        logger.debug(f"ffmpeg_process: {ffmpeg_process}")

        return bool(ffmpeg_process.returncode)


if __name__ == "__main__":
    from pprint import pprint

    ggg = GoGoGo()

    pl = ggg.get_playlist(video_count=2)

    for idx, vid in enumerate(pl):
        print(f'Playlist Item #{idx+1}')
        ggg.create_clip(vid["contentDetails"])

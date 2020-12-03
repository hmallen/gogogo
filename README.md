# gogogo

_...and we're live, guys!_

Automatically download first few seconds of list of Good Morning Crypto episodes to create continuous montage of Ivan saying "go, go, go..."

### Installation:
1) Install ffmpeg
   
   ```bash
   sudo apt install ffmpeg
   ```

2) Create a virtual environment and install dependencies.
   
   ```bash
   virtualenv --python=python3 env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3) Create API key for YouTube Data v3 API on Google Cloud Platform.

4) Rename .env.example to .env and add API key generated in step #3.

### Example command:
```bash
ffmpeg -ss 00:00:37 -to 00:00:44 -i "$(youtube-dl -f best --get-url 'https://youtu.be/PVGeM40dABA')" -c:v copy -c:a copy coffee_sliding.mp4
```
(https://askubuntu.com/questions/970629/how-to-download-a-portion-of-a-video-with-youtube-dl-or-something-else)

```bash
# Command implemented
SYSTEM_FFMPEG_BINARY -ss START_TIMECODE -to END_TIMECODE -i "$(YOUTUBEDL_VENV_BINARY -f best --get-url 'VIDEO_URL')" -c:v copy -c:a copy OUTPUT_FILE

# Working subprocess call
subprocess.run('ffmpeg -ss 00:00:00 -to 00:00:05 -i "$(/home/ubuntu/src/gogogo/env/bin/youtube-dl -f best --get-url https://www.youtube.com/watch?v=NEEMHyzxN-4)" -c:v copy -c:a copy -n test.mp4', shell=True)
```

### Notes:
- Must use shell=True with subprocess to expand variables
- Must not use capture_output=True with subprocess or it will get stuck

### TO DO
- Import/use youtube-dl as python module in main program instead of calling from subprocess.
- Switch to asynchronous subprocess pool for significant speed/performance boost
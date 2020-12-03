# gogogo

_...and we're live, guys!_

Automatically download first few seconds of list of Good Morning Crypto episodes to create continuous montage of Ivan saying "go, go, go..."

### Installation:
1) Initialize submodule dependency (youtube-dl)

```bash
git submodule init
git submodule update
```

2) Create API key for YouTube Data v3 API on Google Cloud Platform.

3) Add API key, and optionally an alternate playlist ID, to a filed named ".env" in the root directory of the project.

### Example command:
```bash
ffmpeg -ss 00:00:37 -to 00:00:44 -i "$(youtube-dl -f best --get-url 'https://youtu.be/PVGeM40dABA')" -c:v copy -c:a copy coffee_sliding.mp4
```
(https://askubuntu.com/questions/970629/how-to-download-a-portion-of-a-video-with-youtube-dl-or-something-else)

### TO DO
- Import/use youtube-dl as python module in main program instead of calling from subprocess.
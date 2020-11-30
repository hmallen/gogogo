# gogogo

_...and we're live, guys!_

Automatically download first few seconds of list of Good Morning Crypto episodes to create continuous montage of Ivan saying "go, go, go..."

### Example command:
```bash
ffmpeg -ss 00:00:37 -to 00:00:44 -i "$(youtube-dl -f best --get-url 'https://youtu.be/PVGeM40dABA')" -c:v copy -c:a copy coffee_sliding.mp4
```
(https://askubuntu.com/questions/970629/how-to-download-a-portion-of-a-video-with-youtube-dl-or-something-else)
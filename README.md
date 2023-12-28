# WebcamViewer

Para verificar qual **index** de sua webcam. 

No Linux: 

```bash
sudo apt install v4l-utils && v4l2-ctl --list-devices
```

Algumas outras alternativas para exibir sua webcam: 

```
sudo apt install ffmpeg
ffplay /dev/video3
```

```
mpv /dev/video3
```

```
sudo apt install mplayer
mplayer -tv device=/dev/video3 tv://
```

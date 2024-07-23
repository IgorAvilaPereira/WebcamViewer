# WebcamViewer

## Formas de como exibir sua webcam no Linux: 

0) Abrir o index.html deste repositório:

Para as demais alternativas, você precisa antes verificar qual dispositivo (webcam) deseja através de **index**: 

Para listar todos os dispositivos de vídeo no Linux: 

```bash
sudo apt install v4l-utils && v4l2-ctl --list-devices
```
1)
```
sudo apt install ffmpeg
ffplay /dev/video3
```
2)
```
mpv /dev/video3
```
3) 
```
sudo apt install mplayer
mplayer -tv device=/dev/video3 tv://
```

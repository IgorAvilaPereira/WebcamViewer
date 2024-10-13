# WebcamViewer

Não sabe testar ou usar sua webcam no Linux rapidamente? Seus problemas acabaram: abaixo listo algumas formas de como usar sua webcam sem softwares burocráticos ou baixar muita coisa. Espero que curta!

## Formas de como exibir sua webcam no Linux: 

0) Abrir o [index.html](https://htmlpreview.github.io/?https://github.com/IgorAvilaPereira/WebcamViewer/blob/main/webcam.html) deste repositório:

obs: Para as demais alternativas, você precisa antes verificar qual dispositivo (webcam) deseja através de **index**: 

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

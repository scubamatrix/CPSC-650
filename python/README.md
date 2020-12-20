# 3. Experimental Tutorial

This folder contains sample code from the [Raspberry-Pi-G1-Tank](https://github.com/YahboomTechnology/Raspberry-pi-G1-Tank) repository.

## Basic Course

1. Color_LED
2. advance
3. CarRun
4. ServoControlColor
5. KeyScanStart
6. tracking
7. avoid_ultrasonic
8. servo_avoid_ultrasonic
9. bluetooth_control
10. TCP_Control

## [Viewing Camera Remotely](https://www.antonsmindstorms.com/2018/10/27/how-to-create-a-realtime-video-stream-with-a-raspberry-pi-and-picam/

)

Easiest method seems to be gstreamer.

```bash
    # On raspi
    sudo apt-get install gstreamer1.0-tools

    # On Mac
    brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-plugins-ugly gst-libav

    # 1. On Mac
    gst-launch-1.0 udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! \
    rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false

    # 2. On Raspberry Pi
    raspivid -t 999999 -b 2000000 -o - | gst-launch-1.0 -e -vvv fdsrc ! h264parse ! \
    rtph264pay pt=96 config-interval=5 ! udpsink host=192.168.7.69 port=5000

    raspivid -t 999999 -w 640 -h 480 -fps 25 -b 2000000 -p 0,0,640,480 -o - | \
    gst-launch-1.0 -e -vvv fdsrc ! h264parse ! \
    rtph264pay pt=96 config-interval=5 ! udpsink host=192.168.7.69 port=5000
```

---

## MP4 Video Format

The Pi captures video as a raw H264 video stream. Many media players will refuse to play it, or play it at an incorrect speed, unless it is "wrapped" in a suitable container format like MP4. The easiest way to obtain an MP4 file from the `raspivid` command is using MP4Box.

```bash
    # Install MP4Box
    sudo apt install -y gpac

    # Capture 5 seconds of raw video at 640x480 and 150kB/s bit rate into a pivideo.h264 file:
    raspivid -t 5000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -o pivideo.h264
    # Wrap the raw video with an MP4 container:
    MP4Box -add pivideo.h264 pivideo.mp4
    # Remove the source raw file, leaving the remaining pivideo.mp4 file to play
    rm pivideo.h264

    # Capture your raw video
    raspivid -o video.h264

    # Wrap MP4 around your existing raspivid output
    MP4Box -add video.h264 video.mp4
```

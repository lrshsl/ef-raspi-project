# Raspberry Pi Project 'Time Lapse Camera'


## Incentive

The goal of this project is to make it possible to create time lapse videos with a raspberry pi. I mainly want to use that for creating time lapses to observe what my 3d printer did, but it should be easily adaptable for other use-cases as well.

## Get started

### Install and run the server

First one has to log into the raspberry pi in order to clone the repo and start the server there.
```sh
# Log into the raspberry pi via ssh (replace xx here with the actual parts of the ip address)
ssh pi@192.168.xx.xx

# Clone the project
git clone https://github.com/lrshsl/ef-raspi-project
cd ef-raspi-project/
```

Afterwards, the python virtual environment has to be activated and a .env has to be created.
```sh
# Copy the example .env to ef-raspi-project/.env
cp .env.example .env

# Activate the Python virtual environment
source .venv/bin/activate    # For bash
```

> Note: The `.env` file should be inspected manually and adapted, especially the variable SECRET_KEY needs to be set to something secret.

Finally, one can run the program:

```sh
# Start the server on 0.0.0.0 (to expose it to the local network) on the port 5000
python3 -m flask run -h 0.0.0.0 -p 5000
```

Now one should be able to navigate to the webpage from any browser on a device connected to the same network as the raspberry pi. For that, enter the local IP address of the raspberry pi followed by the port into the address bar: `192.168.xx.xx:5000`.

### Changing settings of the program

Various settings, such as the interval between the frame captures and the duration of the timelapse, can be passed to the program through environment variables.
For that, either the `.env` file can be adapted, or the can be set via the command line.

For instance, to set the timelapse to record a frame every 6 seconds (0.1 minutes) for 2 hours (120 minutes), the following command can be used:
```sh
INTERVAL_MINUTES=0.1 RECORDING_DURATION_MINUTES=120 python3 -m flask run -h 0.0.0.0 -p 5000
```

### Retrieval of the images

Once the timelapse and pictures have been captured, they are stored on the raspberry pi. To extract them, on unix-like systems, the `scp` or `rsync` commands can be used:
```sh
# Run this commands from the device it should get transfered to
mkdir rsp_cam_output
rsync -r pi@192.168.xx.xx:/home/pi/[path_to_the_code/]ef-raspi-project/output/ ./rsp_cam_output/
```
This creates the folder `rsp_cam_output` in the current working directory and copies the captured images and timelapses in the respective subdirectories. Note that `[path_to_the_code]` has to be replaced by the actual path from the `pi` home directory to where the `ef-raspi-project` had been cloned into.

The timelapse is stored as single frames, which have to be converted to a video format. There are various online and offline tools that can be used for that task, I used the `ffmpeg` program, which would look something like this:
```sh
ffmpeg -framerate 20 -i capture_[capture_name]_frame%03.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p timelapse_[capture_name].mp4
```
With the respective `[capture_name]` that has been set before recording the timelapse on the webpage. This command has been inspired by this [askubuntu answer](https://askubuntu.com/a/610945), where the flags are explained in more detail.

## Progress

- [X] Write program on the Pi that can regularly record photos with a given period
- [ ] Provide an easy way for general settings and commands
    - [X] Start/stop recording
    - [ ] Change frequency
    - [X] Turn off automatically (after some time)
- [ ] Make the resulting video available
    - [ ] Via SSH
    - [ ] Send via telegram
    - [ ] If using with GUI, display it there

I have decided to write a website that is hosted on the pi for providing a gui, to address most of those problems. 




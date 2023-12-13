# Raspberry Pi Project 'Time Lapse Camera'


## Incentive

The goal of this project is to make it possible to create time lapse videos with a raspberry pi. I mainly want to use that for creating time lapses to observe what my 3d printer did, but it should be easily adaptable for other use-cases as well.

## Run the program

First one has to log into the raspberry pi to start the server there:
```sh
# Clone the project
git clone https://github.com/lrshsl/ef-raspi-project
cd ef-raspi-project/
```

```sh
# Activate the Python virtual environment
source .venv/bin/activate    # For bash, alternatively: 
```

```sh
# Start the server on 0.0.0.0 (to expose it to the local network) on the port 5000
python3 -m flask run -h 0.0.0.0 -p 5000
```

Now one should be able to navigate to the webpage from any browser on a device connected to the same network as the raspberry pi by entering the local IP address of the raspberry pi followed by the port: `192.168.xx.xx:5000`.

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




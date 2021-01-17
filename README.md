# Sorting Simulator
This project includes code for the sorting simulator of Prime Vision.

## Dependecies
```
pip install sanic
pip install jinja2
```

## Getting started
```
git clone https://github.com/TimoThans33/sorting-sim.git
```
```
python setup.py install
```
```
python testservice
```
Now you should find the testservice on 0.0.0.0:6543 in the webbrowser.

To simulate the server side you can use the following:
```
python3 echo-server.py
```
## Install as systemd service
Change the .env and .service files accordingly. Then copy the .service file to systemd folder.
```
cp cx-test-service.service /etc/systemd/system/
```
```
sudo systemctl daemon-reload
sudo systemctl start cx-test-service.service
```
To enable from boot.
```
sudo systemctl enable cx-test-service.service
```

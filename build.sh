#!/bin/bash

# Build docker image to be run as container which will show the time and date in browser 

docker build -t pydatetime . 

docker run -it -d -p 8081:80 pydatetime 

echo "View the date and time on the browser by accesing the ip address and on port 8081"
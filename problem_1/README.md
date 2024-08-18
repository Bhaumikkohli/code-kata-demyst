## Problem 1:

To run the Docker image and get the outpu, follow the steps:

1. Open Terminal and redirect to this directory

2. Run the following command:

`docker build --build-arg=export_file=spec.json -t coding-challenge-problem1 .`

3. Check if the docker image is built:

`docker image list`

4. Run the docker image:

`docker run coding-challenge-problem1`

5. Check container ID:

`docker ps -a`

6. Now we need to export our files from the docker environment, run these two commands

`docker cp <containerID>:/parsed_output.csv parsed_output.csv`

`docker cp <containerID>:/fixed_width_text.txt fixed_width_text.txt`

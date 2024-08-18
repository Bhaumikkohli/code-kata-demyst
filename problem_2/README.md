## Problem 2:

To run the Docker image and get the outpu, follow the steps:

1. Open Terminal and redirect to this directory

2. Run the following command to give access to bash script:

`chmod +x run_and_merge.sh`

3. Run the bash script:

`./run_and_merge.sh`

The bash script performs multiple tasks including:

- Spinning a docker build spread across 4 distributed systems. Didn't use replica, as I wanted to control the naming.
- 2 GB size of CSV data is parsed and anonymous values are generated.
- Cleanup of temp tables
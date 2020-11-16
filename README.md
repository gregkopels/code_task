# code_task
This repository holds two parts of the requested assignment.
1. Python script which searchs a file with a regex pattern. 
2. Arguments were added to the commandline to change the output.
  - -c/--color highlights the pattern in the line
  - -m/--machine prints the output in a machine readable format
3. Makefile and Dockerfile are used to install an Alpine container
4. This container uses Pytest to run a series of test cases.
  a. Ping to google.com
  b. Ping to AWS linux server
  c. Verification of SSH connectivity to the AWS server
5. Ability to run test case with Make
6. Ability to run test cases from command line
7. Ability to run test cases with Bash script
# Procedure
1. Clone repository
git clone https://github.com/gregkopels/code_task.git
2. Run make from cloned folder
 - make prune clears the setup
 - make test runs test case
# Make commands
1. To create the container
make
2. To remove the container
make prune
3. To run test case
make test 
# Runs test case from command line
docker run -it --rm -v `pwd`:`pwd` -w `pwd` tester pytest <test1.py> 
docker run -it --rm -v `pwd`:`pwd` -w `pwd` tester python3 <test1.py> 
# Runs test case from BASH
run_test_suite.sh  


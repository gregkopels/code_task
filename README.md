# code_task
This repository holds two parts of the requested assignment.
# Part I
1. Python script which searchs a file with a regex pattern. 
2. Arguments were added to the commandline to change the output.
  - -c/--color highlights the pattern in the line
  - -m/--machine prints the output in a machine readable format
# Run Command 
1. python3 ind_matched_lines.py <file> <regex> <optional argumentt -c, -m and -h>
  - I included a /var/log/message file called file. You can run the script on that or any file of your choice.
# Part 2
 This part creates a container and runs tests using pytest
1. Makefile and Dockerfile are used to install an Alpine container
2. This container uses Pytest to run a series of test cases.
 - Ping to google.com
 - Ping to AWS linux server
 - Verification of SSH connectivity to the AWS server
3. Ability to run test case with Make
4. Ability to run test cases from command line
5. Ability to run test cases with Bash script
# Procedure
1. Clone repository
git clone https://github.com/gregkopels/code_task.git
2. Run make from cloned folder
# Make commands
1. To create the container
make
2. To remove the container
make prune
3. To run test case
make test 
# Runs test case from command line
docker run -it --rm -v `pwd`:`pwd` -w `pwd` tester pytest test1.py
docker run -it --rm -v `pwd`:`pwd` -w `pwd` tester pytest testsuite.py
docker run -it --rm -v `pwd`:`pwd` -w `pwd` tester python3 ssh_aws_servre.py
# Runs test case from BASH
run_test_suite.sh
# Main Regex script
find_matched_lines.py
python3 


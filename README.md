# code_task
 
 # download our files
git clone https://github.com/gregkopels/code_task.git
# build, test and run a command
make build test shell cmd="whoami"
# my favorite for container exploration
make shell
# shell-target is the default (first item), so this also works: 
make cmd="whoami"
make cmd="ls /"
# force a rebuild, test and cleanup
make rebuild test clean
# Run command
docker run -it --rm -v `pwd`:`pwd` -w `pwd` 5d6ebb754770 pytest test1.py

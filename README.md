# code_task
 
 # download our files
git clone https://github.com/gregkopels/code_task.git
# enter directory
cd dockerbuild
# build, test and run a command
make build test shell cmd="whoami"
# my favorite for container exploration
make shell
# shell-target is the default (first item), so this also works: 
make cmd="whoami"
make cmd="ls /"
# force a rebuild, test and cleanup
make rebuild test clean

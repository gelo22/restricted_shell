### Purpose

allow only listed commands for particular ssh connection identified by public key

### Example usage

my_server_host - client(s) will connect to this host
my_client_host - client host, which will connect to my_server_host
my_ssh_key - public ssh key which my_client_host will use for connection to my_server_host
my_user - user, which my_client_host will use for connection to my_server_host

- Clone git to the my_server_host
<pre>
cd /opt/
git clone https://github.com/gelo22/restricted_shell.git
</pre>
- Create new ssh key on the my_client_host
<pre>
ssh-keygen
# copy you public key to the clipboard
cat ~/.ssh/id_rsa.pub
</pre>
- Authorize this ssh key on the my_server_host for my_user
<pre>
cd /home/my_user
editor .ssh/authorized_keys
# add ssh key like this:
command="/opt/restricted_shell/restricted_shell.py" my_ssh_key
</pre>
- Make your own config from example ".py.conf" on the my_server_host
<pre>
cd /opt/restricted_shell
cp -a restricted_shell.py.conf restricted_shell.py_my_user.conf
# add log file
touch restricted_shell.py_my_user.log
chown my_user:my_user restricted_shell.py_my_user.log
</pre>
- Run desired command via ssh from the my_client_host
<pre>
ssh my_user@my_server_host ls -la
# you must see debug output
===+===
splited_command: ['ls', '-la']
original_command: 'ls -la'
</pre>
- Add new commands to json list "allowed_commands" from a log file to the config "restricted_shell.py_my_user.conf" on the my_server_host
<pre>
# example:
ssh my_user@my_server_host ls -la /
cat /opt/restricted_shell/restricted_shell.py_my_user.log
# log output is:
===+===
splited_command: ['ls', '-la', '/']
original_command: 'ls -la /'
# add "original_command" value to the restricted_shell.py_my_user.conf
editor restricted_shell.py_my_user.conf
# example:
"allowed_commands": [
  "ls -la",
  "ls -la /",
  "rsync --server -logDtpre.iLsfx . /opt/dir_2/"
  ]
# turn off debug mode
# change key from
"debug": "yes"
# to
"debug": ""
# and check your command again, it must works now
</pre>

### Ruquirements

Python2 or Python3

GNU/Linux

Openssh

### Options

Config file and script have the same options:
<pre>
usage: restricted_shell.py [-h] [--config_file CONFIG_FILE]
                           [--log_file LOG_FILE] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  --config_file CONFIG_FILE
                        config file location
  --log_file LOG_FILE   log file location
  --debug               enable debug mode - output to terminal
</pre>

Options from command line will owerride values from config

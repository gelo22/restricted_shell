### Purpose

allow only listed commands for particular ssh connection identified by public key

### Example usage

- Clone git
<pre>
cd /opt/
git clone https://github.com/gelo22/restricted_shell.git
</pre>
- Create new ssh key on my_client_host
<pre>
ssh-keygen
</pre>
- authorize this ssh key on the destination host
<pre>
</pre>
- Make your own config from example ".py.conf"
<pre>
</pre>
- Run desired command via ssh
<pre>
</pre>
- Add command from log to config
<pre>
</pre>

where
my_server_host - client(s) will connect to this host
my_client_host - client host, which will connect to my_server_host
my_ssh_key - public ssh key which my_client_host will use for connection to my_server_host
my_user - user, which my_client_host will use for connection to my_server_host

# on the my_client_host todo:
# login as desired user, generate ssh_keys (by default id_rsa and id_rsa.pub)
ssh-keygen

# on the my_server_host todo:

### Ruquirements

Python2 or Python3

GNU/Linux

Openssh

### Options

Config file and script have the same options, run script in help mode to get list of options:
./.py -h

Options from command line will owerride values from config


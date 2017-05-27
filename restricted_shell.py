#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from subprocess import PIPE, Popen
import shlex
import sys
import os
import json
import argparse
import sys
import traceback

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('--config_file', default=sys.argv[0] + '.conf', help='config file location')
parser.add_argument('--log_file', default=sys.argv[0] + '.log', help='log file location')
args = parser.parse_args()

# init config dictionary
conf = dict()

# get config from json file
conf_file = json.load(open(args.config_file))

# add parsed from config_file to config dictionary
for key in conf_file:
    conf[key] = conf_file[key]

# add parsed args to config dictionary
for key in vars(args):
    if vars(args)[key]:
        conf[key] = vars(args)[key]

# main loop for interactive menu
if __name__ == '__main__':
    try:
        # get and prepare command
        command_tmp = os.environ['SSH_ORIGINAL_COMMAND']
        command = shlex.split(command_tmp)
        # write log
        with open(conf['log_file'], 'w') as log:
            log.write("splited_command: {0}\noriginal_command: '{1}'\n".format(command, command_tmp))
        # accept only allowed commannds
        if command_tmp in conf['allowed_commands']:
            proc0 = Popen(command, stdout=sys.stdout, stderr=sys.stderr)
            proc = proc0.communicate()
            proc0.wait()
    except:
        if conf.get('debug'):
            trace = traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
            with open(conf['log_file'], 'a') as log:
                log.write(''.join(trace))



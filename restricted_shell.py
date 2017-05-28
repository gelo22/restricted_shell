#!/usr/bin/env python3

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

# init config dictionary
conf = dict()

def parse_args():
    '''Collect data and parse args'''
    # get user name
    user_name = os.environ['LOGNAME']
    # set default filename
    base_name = '{0}_{1}'.format(sys.argv[0], user_name)

    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', default=base_name + '.conf', help='config file location')
    parser.add_argument('--log_file', default=base_name + '.log', help='log file location')
    parser.add_argument('--debug', action='store_const', const=True, help='enable debug mode - output to terminal')
    args = parser.parse_args()

    # set debug before any actions
    conf['debug'] = vars(args)['debug']

    # get config from json file
    conf_file = json.load(open(args.config_file))

    # add parsed from config_file to config dictionary
    for key in conf_file:
        conf[key] = conf_file[key]

    # add parsed args to config dictionary
    for key in vars(args):
        if vars(args)[key]:
            conf[key] = vars(args)[key]

def _write_log(message):
    '''Write log to log file'''
    if conf.get('debug'):
        print(message)
    else:
        with open(conf['log_file'], 'w') as log:
            log.write(message)

def get_trace():
    '''Get trace and write it to log'''
    trace = traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    message = ''.join(trace)
    _write_log(message)
    sys.exit(1)

def run_command():
    '''Run command from ssh'''
    # get and prepare command
    command_tmp = os.environ['SSH_ORIGINAL_COMMAND']
    command = shlex.split(command_tmp)

    # write log
    message = "===+===\nsplited_command: {0}\noriginal_command: '{1}'\n".format(command, command_tmp)
    _write_log(message)
    # accept only allowed commands
    if command_tmp in conf['allowed_commands']:
        proc0 = Popen(command, stdout=sys.stdout, stderr=sys.stderr)
        proc = proc0.communicate()
        proc0.wait()

def run():
    '''Run whole script'''
    parse_args()
    run_command()

if __name__ == '__main__':
   #run()
    try:
        run()
    except:
        get_trace()


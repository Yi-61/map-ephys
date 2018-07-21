
import os


def run_system_cmd(cmdstr):
    if os.system(cmdstr):
        raise Exception('command "{}" failed'.format(cmdstr))


def test_run_system_cmd():
    run_system_cmd('echo')


def test_mock():
    # TODO: should be run with safeguards, or perhaps mock should have safeguards
    run_system_cmd('./mock.py')


def test_behavior_ingest():
    # TODO: should be run with safeguards, or perhaps mock should have safeguards
    run_system_cmd('./mapshell.py populateB')


def test_ephys_ingest():
    # TODO: should be run with safeguards, or perhaps mock should have safeguards
    run_system_cmd('./mapshell.py populateE')

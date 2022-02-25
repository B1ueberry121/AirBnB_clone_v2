#!/usr/bin/python3
"""deletes out of date files"""
from fabric.api import run, local


def do_clean(number=0):
    """cleans up local machine and server from old files"""
    number = int(number)
    delnum = number + 1
    if number == 0 or number == 1:
        local("cd versions; ls -t | tail -n +2 | xargs rm -rf")
        run("cd /data/web_static/releases; ls -t | tail -n +2 | xargs rm -rf")
    else:
        local("cd versions; ls -t | tail -n +{} | xargs rm -rf".format(delnum))
        run("cd /data/web_static/releases; ls -t | tail +{} | xargs rm -rf"
            .format(delnum))

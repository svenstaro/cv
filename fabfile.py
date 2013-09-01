from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ["apoc"]
env.use_ssh_config = True
env.colorize_errors = True

def deploy():
    code_dir = "/home/svenstaro/prj/cv"
    deploy_dir = "/srv/http/pub/customalized.org/"

    # clone/pull using keybearer first
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:svenstaro/cv.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        sudo("cp index.html cv.css %s" % deploy_dir)
from fabric.api import *
from fabric.contrib import files
from fabric.operations import put
def setup_mo_repo():
    run("mkdir -p git_key")
    with cd("/home/ubuntu/git_key"):
        if not files.exists("./rtb_key"):
            with lcd("%s/conf/git_keys" % os.getcwd()):
                put("rtb_key", "", use_sudo = True)
    run("chmod 0600 rtb_key")
    try:
        run("")  ##too sick
    except:
        pass
    sudo("pip install virtualenv")
    if not files.exists("momo"):
        run("virtualenv -p /usr/bin/python2.7 momo")
    with cd("momo"):
        run("source bin/activate")
        run("eval `ssh-agent` && ssh-add /home/ubuntu/rtb_key && git clone git@github.com:tony7126/momonitor.git")
        with cd("momonitor"):
            run("pip install -r requirements.txt")

@hosts(['mongo-backup.lyfemobile.net'])
def deploy_mo():
    env.user = "ubuntu"
    with cd("momo/momonitor"):
        run("git pull origin master")

@hosts(['mongo-backup.lyfemobile.net'])
def reload_uwsgi():
    with cd("momo/momonitor"):
        run("source ../bin/activate && uwsgi --reload /tmp/momo.pid")
@hosts(["localhost"])
def git_push():
    local("git push origin master")
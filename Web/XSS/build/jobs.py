import subprocess

from flask_rq2 import RQ

rq = RQ()

@rq.job(timeout=15)
def admin(link):
    subprocess.run(
        ["node", "xss_bot_pupet.js", link], timeout=15)
import subprocess

from config import config


class AzureMessageService:
    subproc = []

    def __init__(self):
        self.p = subprocess.Popen(['java', '-cp', config.AZURE_MSG_SERVICE_JAR, config.AZURE_MSG_SERVICE_NS], stdin=subprocess.PIPE)

    def write(self, dict):
        self.p.stdin.write(str(dict) + '\n')

    def exit(self):
        self.p.stdin.write('exit')

import subprocess

from config import api


class AzureMessageService:
    subproc = []

    def __init__(self):
        self.p = subprocess.Popen(['java', '-cp', api.AZURE_MSG_SERVICE_JAR, api.AZURE_MSG_SERVICE_NS], stdin=subprocess.PIPE)

    def write(self, dict):
        self.p.stdin.write(str(dict) + '\n')

    def exit(self):
        self.p.stdin.write('exit')

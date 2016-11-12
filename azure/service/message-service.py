#!/usr/bin/python

import subprocess

p = subprocess.Popen(['java', '-cp', './azure-message-service/target/azure-message-service-1.0-SNAPSHOT-jar-with-dependencies.jar', 'com.avatify.azuremsgsvc.App'], stdin=subprocess.PIPE)
p.stdin.write("{'text':'You\\\'re doing great. Keep it up!', 'mood':'happy'}\n")
p.stdin.write("{'text':'Just a little more.', 'mood':'meh'}\n")
p.stdin.write("exit")

#!/usr/bin/python
import os, math, smtplib, socket
###### configure below ##########
#################################
## set the disk volume
disk = os.statvfs("/")
## threshold
spaceThreshold = 50
## email details
smtpLogin = ''
smtpPass = ''
smtpHost = 'smtp.gmail.com'
smtpPort = 587
mailRecipients = [''] ## add more  ['email1@example.com', 'email2@example.com']
mailSender = ''
###### end configure ##########
###############################
hostName = socket.gethostname()
## get the disk usage for the root volume
totalBytes = float(disk.f_bsize*disk.f_blocks)
totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
## round up the percentage to build in contingency
percentUsed = math.ceil(totalUsedSpace/totalBytes*100)
## fire off an email if the space is above the required number
if percentUsed >= spaceThreshold:
    print "disk space over %d on %s - sending email" % (spaceThreshold,hostName)
    ## send email via the SMTP server
    server = smtplib.SMTP(smtpHost,smtpPort)
    server.starttls()
    server.login(smtpLogin, smtpPass)
    msg = "Subject: Urgent: Space on server %s is over %d percent" % (hostName,spaceThreshold)
    server.sendmail(mailSender, mailRecipients, msg)
    server.quit()

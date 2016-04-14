#!/usr/bin/python
print "Content-type: text/html\n"

import os
import re
import sys
import cgi
import cgitb
import subprocess
import tempfile


def findWholeWord(w):
    return re.compile(r'\b({0})\b\s*\('.format(w), flags=re.IGNORECASE).search


cgitb.enable(display=1, logdir="./")
form = cgi.FieldStorage()
code = form.getvalue("code", "")

okcode = """
phpinfo
"""

badcode = """
eval
call_user_func
call_user_func_array
invoke
dl
passthru
exec
system
chroot
scandir
chgrp
chown
shell_exec
proc_open
proc_get_status
error_log
pfsockopen
syslog
readlink
symlink
popen
stream_socket_server
putenv
apache_child_terminate
apache_setenv
define_syslog_variables
escapeshellarg
escapeshellcmd
exec
fp
fput
ftp_connect
ftp_exec
ftp_get
ftp_login
ftp_nb_fput
ftp_put
ftp_raw
ftp_rawlist
highlight_file
ini_alter
ini_get_all
ini_restore
inject_code
mysql_pconnect
openlog
passthru
php_uname
phpAds_remoteInfo
phpAds_XmlRpc
phpAds_xmlrpcDecode
phpAds_xmlrpcEncode
popen
posix_getpwuid
posix_kill
posix_mkfifo
posix_setpgid
posix_setsid
posix_setuid
posix_uname
proc_close
proc_get_status
proc_nice
proc_open
proc_terminate
shell_exec
syslog
system
xmlrpc_entity_decode
"""

isBad = False
badlist = re.split('[\W\s\n\r]+', badcode)
for x in badlist:
    if len(x) == 0:
        continue
    if findWholeWord(x)(code) != None:
        print "bad code"
        exit()

temp = tempfile.NamedTemporaryFile(suffix='.php',
                                   prefix='prefix_' + str(os.getpid()),
                                   dir='/tmp/'
)

print """<!DOCTYPE html>
<html>
<head lang="zh">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
"""

print "<pre>"

temp.write(code)

temp.flush()

proc = subprocess.Popen("php " + temp.name, shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
(output, outerr) = proc.communicate()
# script_response = proc.stdout.read()
if outerr:
    print outerr
print cgi.escape(output)

print "</pre>"
print "</body>"
print "</html>"
# print os.path.exists(temp.name)

temp.close()

exit()




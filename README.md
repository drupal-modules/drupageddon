Drupageddon
===========

SA-CORE-2014-005 - Drupal core - SQL injection

Drupal 7 includes a database abstraction API to ensure that queries executed against the database are sanitized to prevent SQL injection attacks.

A vulnerability in this API allows an attacker to send specially crafted requests resulting in arbitrary SQL execution. Depending on the content of the requests this can lead to privilege escalation, arbitrary PHP execution, or other attacks.


Patch: [SA-CORE-2014-005-D7.patch](https://www.drupal.org/files/issues/SA-CORE-2014-005-D7.patch)

See also:

 - [Security risk SA-CORE-2014-005 - Drupal core - SQL injection](https://www.drupal.org/SA-CORE-2014-005) at Drupal.org
 - [FAQ on SA-CORE-2014-005](https://www.drupal.org/node/2357241) at Drupal.org
 - [Database ExpandArguments placeholder naming issues when using array](https://www.drupal.org/node/2146839) at Drupal.org (independently reported in public Drupal issue tracker a year ago, without recognizing the impact)
 - [Advisory 01/2014: Drupal - pre Auth SQL Injection Vulnerability](https://www.sektioneins.de/en/advisories/advisory-012014-drupal-pre-auth-sql-injection-vulnerability.html) at sektioneins.de
 - [SA-CORE-2014-005 - Drupal core - SQL injection](http://www.reddit.com/r/netsec/comments/2jbu8g/sacore2014005_drupal_core_sql_injection/) at reddit
 - [drupal_drupageddon module](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/drupal_drupageddon.rb) for [Metasploit framework](http://www.metasploit.com/) at GitHub
 - Blog: [Of Drupageddon and other fancy names](https://0x776b7364.wordpress.com/2014/10/16/of-drupageddon-and-other-fancy-names/) at 0x776b7364
 - Blog: [Drupal SQL Injection Attempts in the Wild](http://blog.sucuri.net/2014/10/drupal-sql-injection-attempts-in-the-wild.html) at sucuri.net
 - Blog: [Your Drupal website has a backdoor](http://drupal.geek.nz/blog/your-drupal-websites-backdoor) at drupal.geek.nz

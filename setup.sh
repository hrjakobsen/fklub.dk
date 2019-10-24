#!/bin/bash
mkdir -p /data/galleries
mkdir -p /data/media
ln -sfn /data/media /var/www/html/media
ln -sfn /data/galleries /var/www/html/galleries
touch /data/f-ordbog.scm
touch /data/faq.scm
chown -R daemon:daemon /data

httpd-foreground
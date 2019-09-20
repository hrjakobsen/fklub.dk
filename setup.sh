#!/bin/bash
mkdir -p /data/galleries
touch /data/f-ordbog.scm
touch /data/faq.scm
chown -R daemon:daemon /data

httpd-foreground
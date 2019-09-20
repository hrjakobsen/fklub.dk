FROM hrjakobsen/laml:latest
ADD "setup.sh" "/scripts/setup.sh"
ADD "new-user-internal.scm" "/scripts/new-user-internal.scm"
ADD "new-user" "/scripts/new-user"
CMD ["/scripts/setup.sh"]

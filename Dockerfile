FROM hrjakobsen/laml:latest
ADD "setup.sh" "/scripts/setup.sh"
CMD ["/scripts/setup.sh"]

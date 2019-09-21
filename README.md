# fklub.dk
Implementation of [fklub.dk](http://fklub.dk) written in the [LAML](http://people.cs.aau.dk/~normark/laml/) Scheme web-framework
> Just because it's legacy code, it doesn't mean thats it's old code
> 
> -- <cite>Albert Einstein 1367</cite>

LAML is a framekwork written by [Kurt Nørmark](http://people.cs.aau.dk/~normark) that enables the use of the Scheme 
programming language for writing dynamic web pages using CGI-programming and [HTML mirror functions](http://people.cs.aau.dk/~normark/laml-distributions/laml/lib/xml-in-laml/mirrors/man/xhtml10-transitional-mirror.html#MANUAL-TOP). 

This is a work-in-progress for the new front-page for [fklub.dk](http://fklub.dk) written in this framework.

## Requirements
- Docker

## Running the webserver
1. Clone the repository
```bash
git clone https://github.com/hrjakobsen/fklub.dk
```
2. Run `docker-compose up -d`
3. Access the page at http://localhost:4000/cgi-bin/index.cgi

## Creating an admin user
After the server has been started in step to, add a new user 
```bash
docker exec -it fklub_web_1 /scripts/new-user
```
You can now use the specified username and password to log in to site

## Debugging
When the server is running, you can follow the access/error log with the following command
```bash
docker logs fklub_web_1 -f --tail 10
```

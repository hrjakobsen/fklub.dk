#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  
(lib-load "file-read.scm") ;  
(lib-load "crypt.scm") ;  

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "lib/cookies.scm")
(cgi-lib-load "lib/cgi.scm")
(cgi-lib-load "lib/file.scm")
(cgi-lib-load "lib/common.scm")


(set-cookie! 'session-id "")
(set-cookie! 'username "")

(redirect "/cgi-bin/index.cgi")
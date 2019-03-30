(cgi-lib-load "lib/cgi.scm")
(cgi-lib-load "lib/cookies.scm")
(cgi-lib-load "lib/auth.scm")

(define ensure-admin (lambda ()
    (if ((negate-n admin?) (get-cookie 'username ) (get-cookie 'session-id )) 
        (begin 
            (redirect "/cgi-bin/login.cgi") 
            (end))
        #t)))



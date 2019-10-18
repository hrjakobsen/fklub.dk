(define cgi-testing #f)
(define (redirect x) 
    (cgi-write (string-append "<meta http-equiv='refresh' content='0; URL=" x "'>"))
    (end))

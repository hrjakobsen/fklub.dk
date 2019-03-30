(define (redirect x) 
    (display (string-append "Location: http://" (getenv "HTTP_HOST") x "\n\n"))
    (end))

(cgi-lib-load "lib/common.scm")
(cgi-lib-load "lib/url.scm")

(define (set-cookie! name content) 
    (display (string-append "Set-Cookie: " (symbol->string name) "=" (url-encode content) "; SameSite=Strict\n")))

(define (get-cookie name) 
    (eq-lookup name (get-all-cookies #f)))

(define (get-all-cookies x)
    (let ((cookies (getenv "HTTP_COOKIE")))
    (if cookies (cookie-to-assoc cookies) '())))

(define (cookie-to-assoc cookie-string)
    (let* (
        (parts (str-split cookie-string #\;))
        (constituents (map (lambda (x) (str-split x #\=)) parts))
        )
        (map (lambda (x) (cons (string->symbol (remove-prefix-spaces (car x))) (url-decode (cadr x)))) constituents)
        ))

(define (remove-prefix-spaces str)
    (if (null? str) ""
        (if (equal? (substring str 0 1) " ") 
            (remove-prefix-spaces (substring str 1))
            str)))


(define (str-split str ch)
    (if (= (string-length str) 0) '()
        (reverse (str-split-help str ch '() '()))))

(define (str-split-help rest ch lst cur)
    (cond 
        ((= (string-length rest) 0)  (cons (list->string (reverse cur)) lst))
        ((char=? (string-ref rest 0) ch) (str-split-help (substring rest 1) ch (cons (list->string (reverse cur)) lst) '()))
        (else (str-split-help (substring rest 1) ch lst (cons (string-ref rest 0) cur)))))

#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  
(lib-load "file-read.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "lib/cookies.scm")
(load "lib/cgi.scm")
(load "lib/file.scm")
(load "lib/common.scm")

(define cgi-testing #f)
(define url-pars (extract-url-parameters))


(define mode 
    (as-symbol (defaulted-get 'mode url-pars 'none )))

(define error 
    (as-symbol (defaulted-get 'error url-pars 'none )))

(define (print-error err)
    (redirect (string-append "login.cgi?error=" (url-encode err))))

(define random-session (lambda () (random-string 64)))

(define (correct-password? username password)
    (let* 
        ((data (read-data-file (string-append "/data/users/" username "/password.dat"))))
        (equal? data password)
    ))

(define perform-login (lambda () 
    (let* (
        (form-a-list (map symbolize-key (extract-form-input))) ;  
        (username (as-string (get 'username form-a-list)))
        (password (as-string (get 'password form-a-list)))
       )
       (cond 
        (((negate directory-exists?) (string-append "/data/users/" username)) (print-error "Invalid user"))
        (((negate-n correct-password?) username password) (print-error "Invalid password"))
        (else 
            (let ((session-id (random-session)))
            (begin
                (write-data-file (string-append "/data/users/" username "/session.dat") session-id)
                (set-cookie! 'session-id session-id)
                (redirect "index.cgi")
                )))))))

(if (eq? mode 'do-login)
    (perform-login)
    (write-page
        "Login"
        (form-1
          "login.cgi?mode=do-login"
          (con
              (if (eq? error 'none ) (div) (p (symbol->string error)))
              (text-line 'username 8 "")
              (br)
              (password-line 'password 8 "")
              (br)
              (submit "Login"))
        )
      ))
(end)

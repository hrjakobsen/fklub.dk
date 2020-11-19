#!/usr/bin/plt/bin/mzscheme -r
(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))
(load "/usr/bin/laml/lib/general.scm")
(load "/usr/local/cgi-bin/lib/file.scm")
(load "/usr/local/cgi-bin/lib/security.scm")

(define (get-string input)
    (begin (display input)
           (read-line (current-input-port))))

(let ((username (get-string "Enter username> "))
      (password (get-string "Enter password> "))) 
      (begin 
        (ensure-exists (string-append "/data/users/" username))
        (write-data-file (string-append "/data/users/" username "/password.dat") (hash-password-default password))
        (write-data-file (string-append "/data/users/" username "/session.dat") "")
        (display (string-append "Created user for " username "\n"))))
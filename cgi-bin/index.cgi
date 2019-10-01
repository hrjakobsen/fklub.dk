#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "common.scm")
(load "lib/namespace.scm")
(load "lib/file.scm")
(define cgi-testing #f)

(fklub-page
  "Forside"
  (con
    (let ((ns (create-famespace))
          (data (safe-read "/data/frontpage.scm" ""))) 
        (parameterize ((current-namespace ns)) (eval (read (open-input-string (string-append "(list " data ")"))))))
  ))
(end)

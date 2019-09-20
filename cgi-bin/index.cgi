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
(define cgi-testing #f)

(fklub-page
  "Forside"
  (con
    (p "page")
        (div 'class "slider"
        (p 'class "rolling" "Siden er udviklet i LAML af FIT &mdash; F-klubbens IT udvalg"))
  ))
(end)

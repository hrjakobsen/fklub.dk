#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(define cgi-testing #f)

(define url-pars (extract-url-parameters))

(load "common.scm")
(load "lib/cgi.scm")
(load "lib/file.scm")
(load "lib/cookies.scm")
(load "lib/url.scm")

(set-cookie! 'testcookie "test af en hest")
(write-page "test" 
    (div 
        menu-list
        (ul
            (map (lambda (x) (li (if (string? (cdr x)) "true" "false"))) (get-all-cookies #f)))
        (p (get-cookie 'session-id))
        (p (url-decode (url-encode "test af en hest...")))
    ))
(end)

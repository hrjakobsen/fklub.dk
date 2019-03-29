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

(write-page "test" 
    (form-1 
        "upload-image.cgi"
        (con 
            (input 'type "file" 'name "images" 'multiple "")
            (submit "Tilføj billede")
        )
    ))

(end)

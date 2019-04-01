#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  
(lib-load "collect-skip.scm") ;  
(lib-load "file-read.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")

(ensure-admin)

(define cgi-testing #f)

(define url-pars (extract-url-parameters))

(define cur-gallery 
	(as-symbol (defaulted-get 'cur-gallery url-pars 'none )))


(let* ((form-a-list (map symbolize-key (extract-form-input))) ;  
        (image (as-string (get 'image form-a-list)))
       )
    (delete-file (string-append "/data/galleries/" (symbol->string cur-gallery) "/" image))
    )

(redirect (string-append "/cgi-bin/admin/edit-gallery.cgi?cur-gallery=" (symbol->string cur-gallery)))

(end)

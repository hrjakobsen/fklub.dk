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

(define cur-gallery 
    (as-symbol (defaulted-get 'cur-gallery url-pars 'none )))
	
(define galleries (dir-list "/data/galleries/"))

(define (get-images gallery-id) 
	(dir-list (string-append "/data/galleries/" gallery-id)))

(define gallery-overview
	  	(div 
		  	menu-list
		    (map (lambda (g) (a 'href (string-append "galleri.cgi?cur-gallery=" g) g)) galleries)))

(define (gallery gallery-id)
	(div 
		menu-list
		(map (lambda (image) (img 'src (string-append "/galleries/" gallery-id "/" image))) (get-images gallery-id))))
		  
	  

(define page-body
	(if (eq? 'none cur-gallery)
		gallery-overview
		(gallery (symbol->string cur-gallery))))

(write-page "test" page-body)

(end)

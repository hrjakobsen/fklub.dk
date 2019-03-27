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

(define images 
	(let ((data (read-data-file "/data/galleri.scm"))) 
		(if (list? data) (reverse data) (list))))



(define (gallery imgs) 
	  	(div 
		  	menu-list
		    (if (null? imgs) #f
			  	(div (map (lambda (x) (img 'src x)) imgs))
			    )

		 	(form-1 
		 		"upload-image.cgi"
		 		(con 
		 			(text-line 'new-url 3 "")
		 			(submit "Tilføj billede")
		 		)
		 	)))
	

(write-page "test" (gallery images))

(end)

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

(define questions 
	(let ((data (read-data-file "/data/faq.scm"))) 
		(if (list? data) (reverse data) (list))))



(define (faq questions) 
	  	(div 
		  	menu-list
		    (if (null? questions) #f
			  	(ul
			  		(map (lambda (x) (li (string-append (car x) " - " (cdr x)))) questions)
			  	))

		 	(form-1 
		 		"upload-faq.cgi"
		 		(con 
		 			(text-line 'question 3 "")
		 			(text-line 'answer 3 "")
		 			(submit "Tilføj FAQ")
		 		)
		 	)))
	

(write-page "test" (faq questions))

(end)

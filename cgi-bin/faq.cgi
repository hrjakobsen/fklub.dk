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

(define questions 
	(let ((data (safe-read "/data/faq.scm" '()))) 
		(if (list? data) (reverse data) (list))))


(define (faq questions) 
	  	(container 
		    (if (null? questions) (p "Ingen spørgsmål")
				(ul
			  		(map (lambda (x) (li (string-append (car x) " - " (cdr x)))) questions)
				))))
	

(fklub-page "test" (faq questions))

(end)

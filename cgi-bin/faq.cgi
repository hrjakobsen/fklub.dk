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

(define (faq-element x)
	(div 'class "faq" 
		(div 'class "faq-word" (span 'class "faq-title" (car x)))
		(div 'class "faq-answer" (cdr x))))

(define (faq questions) 
	  	(container 
		  (con 
			(heading "Hyppigt stillede spørgsmål")
		    (if (null? questions) (p "Ingen spørgsmål")
				(div
			  		(map faq-element questions)
				)))))
	

(fklub-page "Hyppigt stillede spørgsmål" (faq questions))

(end)

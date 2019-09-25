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

(define entries 
	(let ((data (read-data-file "/data/f-ordbog.scm"))) 
		(if (list? data) (reverse data) (list))))

(define (create-entry x)
	(div 'class "word-definition"
		(div 'class "word-title"
			(span 'class "title-text" (car x)))
		(div 'class "word-description"
			(span 'class="description-text" (cdr x)))))


(define (dictionary entries) 
	  	(container 
		    (if (null? entries) (p "Ingen opslag")
				(con
			  		(map create-entry entries)
				))))
	
(fklub-page "test" (dictionary entries))
(end)

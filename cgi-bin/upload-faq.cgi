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

(load "common.scm")
(load "lib/file.scm")
(load "lib/cgi.scm")

(define cgi-testing #f)

(define url-pars (extract-url-parameters))

(define questions 
	(let ((data (read-data-file "/data/faq.scm"))) 
		(if (list? data) (reverse data) (list))))

(let* ((form-a-list (map symbolize-key (extract-form-input))) ;  
    (question (as-string (get 'question form-a-list)))
    (answer (as-string (get 'answer form-a-list)))
   )
(begin 
	(write-data-file "/data/faq.scm" (cons (cons question answer) questions))
	(redirect "faq.cgi")
)
)



(end)

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


(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")
(cgi-lib-load "lib/utf-8-form-fix.scm")

(ensure-admin)

(define cgi-testing #f)

(define url-pars (extract-url-parameters))

(define questions 
	(let ((data (read-data-file "/data/faq.scm"))) 
		(if (list? data) (reverse data) (list))))

(let* ((form-a-list (map symbolize-key (extract-form-input))) ;  
    (question (as-string (get 'question form-a-list)))
   )
(begin 
	(write-data-file "/data/faq.scm" (filter (negate (lambda (x) (equal? (car x) question))) questions))
	(redirect "/cgi-bin/admin/edit-faq.cgi")
)
)



(end)

#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(define cgi-testing #f)

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")

(ensure-admin)

(define data (safe-read "/data/frontpage.scm" ""))

(define (edit-form current-data) 
	  	(container 
		 	(form-1 
		 		"upload-frontpage.cgi"
		 		(con 
		 			(textarea 'name 'data 'rows "25" 'class "frontpage-field" current-data)
					(br)
		 			(submit "Gem")
		 		)
		 	)))

(fklub-page "Rediger forside" (con admin-menu-list (edit-form data)))

(end)

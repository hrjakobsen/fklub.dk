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

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")

(ensure-admin)

(define cur-gallery 
	(as-symbol (defaulted-get 'cur-gallery url-pars 'none )))
	
(define galleries (dir-list "/data/galleries/"))

(define (get-images gallery-id) 
	(dir-list (string-append "/data/galleries/" gallery-id)))

(define gallery-overview
	(map (lambda (g) (a 'href (string-append "edit-gallery.cgi?cur-gallery=" g) g)) galleries))

(define (gallery gallery-id)
	(con
		;(map (lambda (image) (img 'src (string-append "/galleries/" gallery-id "/" image))) (get-images gallery-id))
			
		(multipart-form 
			(string-append "upload-images.cgi?cur-gallery=" gallery-id) 
			(string-append "/data/galleries/" gallery-id "/") 
			(string-append "/galleries/" gallery-id) 
			(con 
				(input 'type "hidden" 'name "cur-gallery" 'value gallery-id)
				(input 'type "file" 'name "images" 'multiple "")
				(submit "Tilføj billede")))
))


(define page-body
	(con
		menu-list
		admin-menu-list
		(if (eq? 'none cur-gallery)
			gallery-overview
			(gallery (symbol->string cur-gallery)))))

(write-page "test" page-body)

(end)

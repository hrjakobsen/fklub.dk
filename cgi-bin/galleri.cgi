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
(load "lib/date.scm")


(define cur-gallery 
    (as-symbol (defaulted-get 'cur-gallery url-pars 'none )))
	
(define galleries (reverse (dir-list "/data/galleries/")))

(define (get-images gallery-id) 
	(if (in-gallery? gallery-id)
		(dir-list (string-append "/data/galleries/" gallery-id))
		'()))

(define (to-thumbnail image gallery-id) 
	(let ((url (string-append "/galleries/" gallery-id "/" image)))
		(div 'class "col col-sm-12 col-md-4" 
			(a 'href url  'data-lightbox "test"
				(img 'class "gallery-thumbnail" 'src url)))))

(define gallery-overview
		(con 
			(heading "Galleri")
			(div 'class "gallery"
				(div 'class "list-group"
					(map (lambda (g) (a  'class "list-group-item list-group-item-action" 'href (string-append "galleri.cgi?cur-gallery=" g) g (span 'class "badge badge-secondary float-right" (fa "calendar")(get-date-string (get-last-edit (string-append "/data/galleries/" g)))))) galleries)))))


(define (gallery gallery-id)
	(con
		(heading gallery-id)
		(div 'class "gallery-col"
			(row 
				(map (lambda (x) (to-thumbnail x gallery-id)) (get-images gallery-id))))))
		  
	  

(define page-body
	(container (if (eq? 'none cur-gallery)
		gallery-overview
		(gallery (symbol->string cur-gallery)))))

(fklub-page "Galleri" page-body)

(end)

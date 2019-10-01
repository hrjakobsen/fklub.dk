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
	
(define error
    (as-symbol (defaulted-get 'error url-pars 'none)))
	
(define galleries (dir-list "/data/galleries/"))

(define (get-images gallery-id) 
	(dir-list (string-append "/data/galleries/" gallery-id)))

(define gallery-overview
	(con 
		(h3 "Gallerier")
		(div 'class "list-group"
		(map (lambda (g) (a 'class "list-group-item list-group-item-action" 'href  (string-append "edit-gallery.cgi?cur-gallery=" g) g)) galleries))
		(h3 "Tilføj nyt galleri")
		(if (eq? error 'empty-gallery-name ) (p "Giv" (b "venligst") "galleriet et navn.") (div))
		(form-1 
			"create-gallery.cgi"
			(con 
				(input-text 'name "Galleri-navn")
				(br)
				(submit-btn "Opret")))))

(define (gallery gallery-id)
	(con
		(h3 (string-append "Rediger " gallery-id))
		(if (> (length (get-images gallery-id)) 0)
			(con
			(row
				(map (lambda (image) 
					(col "col-sm-3 gallery-img" 
						(con
						(form-1 
								(string-append "remove-image.cgi?cur-gallery=" gallery-id)
								(con 
									(hidden-line 'image image)
									(button 'type "submit" 'class "btn btn-danger remove-button" (fa "trash"))
								)
							)
						(img 'width 200 'src (string-append "/galleries/" gallery-id "/" image))))
				) (get-images gallery-id))
			))
				(p "No images"))
		(multipart-form 
			(string-append "upload-images.cgi?cur-gallery=" gallery-id) 
			(string-append "/data/galleries/" gallery-id "/") 
			(string-append "/galleries/" gallery-id) 
			(con 
				(input 'type "hidden" 'name "cur-gallery" 'value gallery-id)
				(input 'type "file" 'name "images" 'multiple "")
				(br)
				(br)
				(submit-btn "Upload billeder")))
		(br)
		(form-1 
			(string-append "remove-gallery.cgi?cur-gallery=" gallery-id)
			(con 
				(button 'type "submit" 'class "btn btn-danger remove-button" (con "Slet galleri" (fa "trash")))))))


(define page-body
	(con
		admin-menu-list
		(container (if (eq? 'none cur-gallery)
			gallery-overview
			(gallery (symbol->string cur-gallery))))))

(fklub-page "Rediger galleri" page-body)

(end)

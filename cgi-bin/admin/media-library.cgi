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

(define media 
	(dir-list "/data/media/"))

(cgi-write 
		(html
			(head
				(title "Media library - Fklub.dk")
				(meta 'charset "utf-8")
				(meta 'http-equiv "X-UA-Compatible" 'content "IE=edge")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
				(link 'rel "stylesheet" 'href "/style.css")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Josefin+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Open+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"))
			(body 
                (h1 "Media library")
                (a 'class "btn btn-primary" 'href "/cgi-bin/admin/add-media.cgi" "Upload media")
                (br)
                (row
                    (map (lambda (image) 
                        (col "col-sm-3 gallery-img" 
                                (con
                                    (img 'class "media-thumbnail" 'src (string-append "/media/" image))
                                    (br)
                                    (input 'class "media-link" 'type "text" 'value (string-append "/media/" image) 'onclick "this.select();")
                                    (br)
                                    (br)))
                    ) media)))))
                

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

(cgi-write 
		(html
			(head
				(title "Add media - Fklub.dk")
				(meta 'charset "utf-8")
				(meta 'http-equiv "X-UA-Compatible" 'content "IE=edge")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
				(link 'rel "stylesheet" 'href "/style.css")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Josefin+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://fonts.googleapis.com/css?family=Open+Sans&display=swap")
				(link 'rel "stylesheet" 'href "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"))
			(body 
				(con 
					(h1 "Upload media")
                    (multipart-form 
                        (string-append "upload-media.cgi") 
                        (string-append "/data/media/") 
                        (string-append "/media/") 
                        (con 
                            (input 'type "file" 'name "media")
                            (br)
                            (br)
                            (submit-btn "Upload media")))))))
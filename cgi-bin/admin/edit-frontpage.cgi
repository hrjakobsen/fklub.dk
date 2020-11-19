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
		  (h3 "Rediger forside")
		  (button 'class "btn btn-primary" 'onclick "window.open('/cgi-bin/admin/media-library.cgi','Media Library','height= 480 px,width =760 px ,')" "Åbn mediebibliotek")
		  (p "Følgende funktioner er tilgængelige:")
		  (ul
		  	(li "(section [baggrundsfarve] [data])")
		  	(li "(text [data])")
		  	(li "(title [titel])")
		  	(li "(link [url] [data])")
		  	(li "(image [url])")
		  	(li "(images [data])")
		  	(li "(center [data])")
		  	(li "(youtube [video-id])")
		  	(li "(imagelink [href] [image-src])")
		  	(li "(button-(primary|secondary|info) [text])")
		  	(li "(bold [text])")
		  )
		  (p "Eksempel på side")
		  (pre 'class "example-frontpage" "(section \"#efefef\"\n\t(title \"F-Klubben\")\n\t(text \"Beskrivelse af F-Klubbens arbejde\")\n\t(image \"https://via.placeholder.com/300x150\")\n)")
		 	(form-1 
		 		"upload-frontpage.cgi"
		 		(con 
		 			(textarea 'name 'data 'rows "25" 'class "frontpage-field" current-data)
					(br)
					(br)
		 			(submit-btn "Gem")
		 		)
		 	)
			 (br)))

(fklub-page "Rediger forside" (con admin-menu-list (edit-form data)))

(end)

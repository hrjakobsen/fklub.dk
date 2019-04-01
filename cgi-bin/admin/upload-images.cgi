#!/usr/bin/plt/bin/mzscheme -r

(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "color.scm") ;  
(lib-load "collect-skip.scm") ;  
(lib-load "file-read.scm") ;  

; HTML mirror loading
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

(load "/usr/local/cgi-bin/lib/common.scm")
(cgi-lib-load "admin/admin.scm")
(cgi-lib-load "common.scm")
(cgi-lib-load "lib/file.scm")

(ensure-admin)

(define cgi-testing #f)

(define url-pars (extract-url-parameters))

(define cur-gallery 
	(as-symbol (defaulted-get 'cur-gallery url-pars 'none )))

(set! ip (current-input-port))

;; Redefinition of internal LAML function. 
; Read the file byte-by-byte instead of character-by-character
; As it will only work for text-files otherwise.
(define (generic-read-char ip)
  (cond ((input-port? ip) (integer->char (read-byte ip)))
        ((string? ip) 
           (if (>= pstring-ip-pointer (string-length ip))
               #f
               (let ((res (string-ref ip pstring-ip-pointer)))
		 (set! pstring-ip-pointer (+ 1 pstring-ip-pointer))
		 res)))
        (else (laml-error "generic-read-char: ip must be a string or an input stream"))))


;; Redefinition of internal LAML function. 
; Write the file byte-by-byte instead of char-by-char
(define (pass-uploaded-file-1! op boundary match-pos boundary-lgt)
    (if (= boundary-lgt match-pos) ; @a
        'done
        (let* ((ch (read-a-char))
            (match-ch (string-ref boundary match-pos))
            )
            (cond ((eqv? ch match-ch)
                (display-mes-if-debugging (string-append "Matches " (as-string ch) " match-pos: " (as-string (+ match-pos 1))))
                (pass-uploaded-file-1! op boundary (+ match-pos 1) boundary-lgt))
            ((and (not (eqv? ch match-ch)) (> match-pos 0))
                (display-mes-if-debugging (string-append "Writing " (substring boundary 0 match-pos) "to op"))
                (write-string-bytes-to-port (substring boundary 0 match-pos) op) ; (@b) write matched part of boundary
                (write-byte (char->integer ch) op)
                (pass-uploaded-file-1! op boundary 0 boundary-lgt))
            ((not (eqv? ch match-ch)) 
                (display-mes-if-debugging (string-append "Passing " (as-string ch) " through"))
                (write-byte (char->integer ch) op)
                (pass-uploaded-file-1! op boundary 0 boundary-lgt))
            ))))

(define (write-string-bytes-to-port str op)
    (empty-port-into-port (open-input-string str) op))

(define (empty-port-into-port in op)
    (if (eof-object? (peek-byte in)) #t 
        (begin 
            (write-byte (read-byte in) op)
            (empty-port-into-port in op))))
(multipart-decode (current-seconds))

(redirect (string-append "/cgi-bin/admin/edit-gallery.cgi?cur-gallery=" (symbol->string cur-gallery)))

(end)

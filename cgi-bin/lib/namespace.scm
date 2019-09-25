(define laml-dir "/usr/bin/laml/") ;  
(load (string-append laml-dir "laml.scm"))

(lib-load "cgi.scm") ;  @a
(lib-load "encode-decode.scm") ;  
(lib-load "html4.01-transitional-validating/basis.scm")
(lib-load "html4.01-transitional-validating/surface.scm")
(lib-load "html4.01-transitional-validating/convenience.scm")

; Utility functions allowed in markup language

(define (f-section color . data)
    
        (div 'class "section" 
            'style (string-append "background-color:" color ";") 
            (container (con data))))

(define (f-title text)
    (h2 text))

(define (f-par text)
    (p text))

(define (f-img url)
    (div 'class "imagecontainer" (img 'src url)))

(define (f-imgs . data)
    (div 'class "imagescontainer" (con data)))

(define (f-link url text)
    (a 'href url text))

(define (f-center . data) 
    (div 'class "center" data))

(define create-famespace
  (lambda ()
    (let ((ns (make-namespace))) 
        (parameterize ((current-namespace ns)) 
          (begin 
            (namespace-set-variable-value! 'section f-section)
            (namespace-set-variable-value! 'text f-par)
            (namespace-set-variable-value! 'image f-img)
            (namespace-set-variable-value! 'images f-imgs)
            (namespace-set-variable-value! 'title f-title)
            (namespace-set-variable-value! 'link f-link)
            (namespace-set-variable-value! 'center f-center)
            ns)))))




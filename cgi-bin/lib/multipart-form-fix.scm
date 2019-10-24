(define cgi-testing #f)

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
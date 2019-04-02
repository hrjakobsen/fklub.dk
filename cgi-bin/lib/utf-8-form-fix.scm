; Today has been a day of challenges. 
; LAML does not support decoding UTF-8 strings in 
; forms with application/x-www-form-urlencoded enctype.
; This file seeks to remedy that by overriding key functions in the encode-decode.scm
; file in the LAML library. It does so by expanding the state machine using for 
; parsing the form input, and by allowing encoded characters to span multiple
; data segments such as %C3%A6 = æ. It (should) support(s) the full range of 
; UTF-8 characters of 1-4 bytes length. 
(define (decode-string-alist-1 instr inptr inlength outstr outptr prop-list collected current-state)
	(if (= inptr inlength)
	
		(cond 
				((eq? current-state 'in-key-or-value) (cons (substring outstr 0 outptr) prop-list))  ; include the last string
				((eq? current-state 'hex3) (cons (substring outstr 0 outptr) prop-list))             ; also here
				((eq? current-state 'equal-accepted) (cons "" prop-list))                            ; include a trailing empty string
				((eq? current-state 'ampersand-accepted) prop-list)                                  ; just return prop-list
				(else (error "decode-string-a-list-1: Strange end of string input")))
					
		(let* ((inch (string-ref instr inptr))
				(trans-res (decode-string-transition current-state inch collected))
				(next-state (car trans-res))
				(next-collected (cdr trans-res))
				)
	
			(cond 
			((and (eq? next-state 'in-key-or-value) (eq? inch #\+)) (string-set! outstr outptr #\space))  ; handle '+'
			((eq? next-state 'in-key-or-value) (string-set! outstr outptr inch))                          ; normal case
			((eq? next-state 'hex3) (string-set! outstr outptr next-collected))                           ; insert hex conversion
			)
	
			(decode-string-alist-1 instr (+ 1 inptr) inlength
								outstr 
								(cond ((eq? next-state 'equal-accepted) 0)
										((eq? next-state 'ampersand-accepted) 0)
										((eq? next-state 'hex1) outptr)
										((eq? next-state 'hex2) outptr)
										((eq? next-state 'hex-gobble-2) outptr)
										((eq? next-state 'hex-gobble-3) outptr)
										((eq? next-state 'hex-gobble-4) outptr)
										(else  (+ outptr 1)))
								(if (or (eq? next-state 'equal-accepted) (eq? next-state 'ampersand-accepted))
									(cons (substring outstr 0 outptr) prop-list)
									prop-list)
								next-collected
								next-state)
		)))


; The state machine is expanded with 'hex-gobble-[2-4] states 
; thats reads 1-4 bytes of UTF-8 encoded characters.
(define (decode-string-transition in-state ch hex-collect)
	(let ((char (as-string ch)))
		(cond 
			((eq? in-state 'in-key-or-value)
				(cond 
						((eqv? ch #\%)                                           hex1-state)
						((eqv? ch #\=)                                           equal-accepted-state)
						((eqv? ch #\&)                                           ampersand-accepted-state)
						(else                                                   in-key-or-value-state)
				))
	
			((eq? in-state 'hex1)
                                    (cons 'hex2 (as-string ch)))
	
			((eq? in-state 'hex2)
                                    (let* (
                                        (cur (string-append hex-collect (as-string ch))))
                                        (cond 
                                            ((has-pattern 224 cur 192) (cons 'hex-gobble-2 cur))
                                            ((has-pattern 240 cur 224) (cons 'hex-gobble-3 cur))
                                            ((has-pattern 248 cur 240) (cons 'hex-gobble-4 cur))
                                            (else (cons 'hex3 (two-digit-hex-to-char cur))))))
			((eq? in-state 'hex-gobble-2)
                                    (cond 
                                        ((eqv? ch #\%) (cons 'hex-gobble-2 hex-collect))
                                        ((= (string-length hex-collect) 3) (cons 'hex3 (parse-hex-to-char (string-append hex-collect (as-string ch)))))
                                        (else (cons 'hex-gobble-2 (string-append hex-collect (as-string ch))))))
			((eq? in-state 'hex-gobble-3)
                                    (cond 
                                        ((eqv? ch #\%) (cons 'hex-gobble-3 hex-collect))
                                        ((= (string-length hex-collect) 5) (cons 'hex3 (parse-hex-to-char (string-append hex-collect (as-string ch)))))
                                        (else (cons 'hex-gobble-3 (string-append hex-collect (as-string ch))))))
			((eq? in-state 'hex-gobble-4)
                                    (cond 
                                        ((eqv? ch #\%) (cons 'hex-gobble-4 hex-collect))
                                        ((= (string-length hex-collect) 7) (cons 'hex3 (parse-hex-to-char (string-append hex-collect (as-string ch)))))
                                        (else (cons 'hex-gobble-4 (string-append hex-collect (as-string ch))))))
																					
			((eq? in-state 'hex3)
				(cond 
                    ((eqv? ch #\&)                            ampersand-accepted-state)
                    ((eqv? ch #\=)                            equal-accepted-state)
                    ((eqv? ch #\%)                            hex1-state)
                    (else                                     in-key-or-value-state)
				))
	
			((eq? in-state 'ampersand-accepted)
				(cond 
						((eqv? ch #\%)                        hex1-state)
						((eqv? ch #\=)                        equal-accepted-state)
						((eqv? ch #\&)                        ampersand-accepted-state)
						(else                                 in-key-or-value-state)
				))
	
			((eq? in-state 'equal-accepted)
				(cond 
						((eqv? ch #\%)                        hex1-state)
						((eqv? ch #\=)                        equal-accepted-state)
						((eqv? ch #\&)                        ampersand-accepted-state)
						(else                                 in-key-or-value-state)
				))
	
	
	
			(else                                             (error (string-append 
															        "decode-string-transition: Unknown state: "
																	(as-string in-state))))
	
		)))

; The following section are helper functions used to compute in the above fix. 
(define (^ n1 n2)
	(if (= n2 0)
		1
		(* n1 (^ n1 (- n2 1)))))

(define (has-pattern pattern value result)
	(let* (
		(number (parse-hex-to-int value))
		(after-and (bitwise-and number pattern)))
		(= after-and result)))

(define (parse-hex-to-char str)
	(string-ref (bytes->string/utf-8 (hex->bytes str)) 0))

(define (parse-hex-to-int str)
	(if (= (string-length str) 0) 0
		(+ (* (hex-ciffer->decimal-ciffer (string-ref str 0)) (^ 16 (- (string-length str) 1))) (parse-hex-to-int (substring str 1)))))

(define (get-last-two-chars str)
	(substring str (- (string-length str) 2)))

(define (hex->bytes str)
	(if (= (string-length str) 0)
		(bytes)
		(if (and (= (modulo (string-length str) 2) 0) (> (string-length str) 1))
			(bytes-append 
				(bytes (parse-hex-to-int (substring str 0 2))) 
				(hex->bytes (substring str 2))
				)
			(error "Invalid hex string"))))
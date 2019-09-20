(define (admin? username session-id)
    (and 
        (string? username)
        (> (string-length username) 0) 
        (string? session-id)
        (> (string-length session-id) 0) 
        (correct-session? username session-id)))


(define (correct-session? username session)
    (let* 
        ((data (read-data-file (string-append "/data/users/" username "/session.dat"))))
        (equal? data session)))
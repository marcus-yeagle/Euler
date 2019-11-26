;; Sum all even Fibonacci Numbers less than 4 Million 

(defn fibo[n]
    (cond 
        (= n 0) 0
        (= n 1) 1
        :else (+ n (fibo (- n 1))))) 

(print (fibo 3))
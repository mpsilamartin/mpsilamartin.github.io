let mult_naive p q =
  let n = Array.length p in
  let pq = Array.make (2*n-1) 0 in
  for k = 0 to 2*n-2 do
    let ck = ref 0 in
    for j = 0 to k do
      if j < n && k-j < n
      then ck := !ck + p.(j)*q.(k-j)
    done;
    pq.(k) <- !ck
  done;
  pq
;;

let rec mult_karatsuba p q =
  let n = Array.length p in
  if n = 1 
  then [|p.(0)*q.(0)|]
  else
    let m = (n+1)/2 in
    let p0 = Array.make m 0 in
    let p1 = Array.make m 0 in
    let q0 = Array.make m 0 in
    let q1 = Array.make m 0 in
    let c1 = Array.make m 0 in
    let c2 = Array.make m 0 in
    for i = 0 to m-1 do
      p0.(i) <- p.(i);
      q0.(i) <- q.(i);
      if i+m < n
      then
        begin
          p1.(i) <- p.(m+i);
          q1.(i) <- q.(m+i)
        end;
      c1.(i) <- p0.(i) - p1.(i);
      c2.(i) <- q1.(i) - q0.(i)
    done;
    let p0q0 = mult_karatsuba p0 q0 in
    let p1q1 = mult_karatsuba p1 q1 in
    let c1c2 = mult_karatsuba c1 c2 in
    let pq = Array.make (2*n-1) 0 in
    for i = 0 to 2*m-2 do
      pq.(i) <- p0q0.(i)
    done;
    for i = 0 to 2*m-2 do
      pq.(m+i) <- pq.(m+i)
                  + c1c2.(i)
                  + p0q0.(i)
                  + p1q1.(i)
    done;
    for i = 0 to 2*n-2-2*m do
      pq.(2*m+i) <- pq.(2*m+i)+p1q1.(i)
    done;
    pq
;;

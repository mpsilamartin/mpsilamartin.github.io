let mult_naive p q =
  let n = Array.length p in
  let pq = Array.make (2*n-1) (p.(0)*q.(0)) in
  for k = 1 to 2*n-2 do
    let c = ref 0 in
    for i = 0 to k do
      c := !c + (if i >= n
                 then 0
                 else p.(i))
                *(if k-i >= n
                  then 0
                  else q.(k-i)
                 )
    done;
    pq.(k) <- !c
  done;
  pq
;;
let mult_naive p q =
  let n = Array.length p in
  let pq = Array.make (2*n-1) (p.(0)*q.(0)) in
  for k = 1 to 2*n-2 do
    let c = ref 0 in
    for i = 0 to k do
      if i < n && k-i < n
      then c := !c + p.(i)*q.(k-i)
    done;
    pq.(k) <- !c
  done;
  pq
;;

let combi_poly p q a b =
  (* Calcule aP+bQ avec p et q de même longueur *)
  let n = Array.length p in
  let cl = Array.make n 0 in
  for i = 0 to n-1 do
    cl.(i) <- a*p.(i) + b*q.(i)
  done;
  cl
;;

let somme p q =
  combi_poly p q 1 1
;;
  
let rec mult_karatsuba p q =
  let n = Array.length p in
  match n with
  | 0 -> [||]
  | 1 -> [|p.(0)*q.(0)|]
  | _ -> let m = (n+1)/2 in
         let p0 = Array.make m 0 in
         let p1 = Array.make m 0 in
         let q0 = Array.make m 0 in
         let q1 = Array.make m 0 in
         for i = 0 to m-1 do
           p0.(i) <- p.(i);
           q0.(i) <- q.(i)
         done;
         for i = m to n-1 do
           p1.(i-m) <- p.(i);
           q1.(i-m) <- q.(i)
         done;
         let p0q0 = mult_karatsuba p0 q0 in
         let p1q1 = mult_karatsuba p1 q1 in
         let p0q1_plus_p1q0 =
           somme
             (mult_karatsuba
                (combi_poly p0 p1 1 (-1))
                (combi_poly q1 q0 1 (-1))
             )

             (somme p0q0 p1q1)
         in
         let pq = Array.make (2*n-1) 0 in
         for e = 0 to 2*m-2 do
           pq.(e) <- pq.(e) + p0q0.(e);
           pq.(m+e) <- pq.(m+e)+p0q1_plus_p1q0.(e);
           if 2*m+e < 2*n-1
           then
             pq.(2*m+e) <- pq.(2*m+e) + p1q1.(e)
         done;
         pq
;;
         
         
         
         
         
         

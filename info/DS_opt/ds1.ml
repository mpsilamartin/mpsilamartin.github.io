let rec debut n lst =
  match n, lst with
  | 0, _ -> []
  | _, [] -> []
  | _, t::q -> t::(debut (n-1) q)
;;

let rec iterer n f x =
  match n with
  | 0 ->  [x]
  | _ -> x::iterer (n-1) f (f x)
;;

let init n f =
  let rec construit k =
    (* Construit la liste [f(k);...;f(n-1)]*)
    if k = n
    then []
    else f k::construit (k+1)
  in construit 0
;;
  
type sexe = M | F;;

type division =
  | MPSI of int
  | MP of int
  | PSI
;;

type etudiant = {
    nom : string;
    prenom : string;
    classe : division;
    sexe : sexe
  };;

let bonemine = {
    nom = "ABRARACOURCIX";
    prenom = "Bonemine";
    classe = MPSI 3; (* de type division *)
    sexe = F (* de type sexe *)
  };; 
let rec repartition_mp lst =
  match lst with
  | [] -> [], []
  | t::q -> let mp1, mp2 = repartition_mp q in
            match t.classe with
            | MP 1 -> t::mp1, mp2
            | MP 2 ->mp1, t::mp2
            | _ -> mp1, mp2
;;
let rec repartition_sexe lst =
  match lst with
  | [] -> 0, 0
  | t::q -> let nq, pq = repartition_sexe q in
            match t.sexe with
            | F -> nq + 1, pq
            | M -> nq, pq +1
;;

let proportion_filles lst =
  let n, p = repartition_sexe lst in
  float_of_int n /. (float_of_int (n+p))
;;

let nouvelle_repartition lst1 lst2 =
  let n1, p1 = repartition_sexe lst1 in
  let n2, p2 = repartition_sexe lst2 in
  let new_n1, new_p1 = (n1+n2)/2, (p1+p2+1)/2 in
  let rec construit_mp1 l1 l2 n p =
    match l1, l2 with
    | [], [] -> [], []
    | t1::q1,_ ->
       begin
         match t1.sexe, n, p with
         | F, 0, _ ->  let mp1, mp2 = construit_mp1 q1 l2 0 p in mp1, t1::mp2
         | F, _, _ -> let mp1, mp2 = construit_mp1 q1 l2 (n-1) p in t1::mp1, mp2
         | M, _, 0 -> let mp1, mp2 = construit_mp1 q1 l2 n 0 in  mp1, t1::mp2
         | M, _, _ ->  let mp1, mp2 = construit_mp1 q1 l2 n (p-1) in t1::mp1, mp2
       end
    | _, t2::q2 ->
       begin
         match t2.sexe,n, p with
         | F, 0, _ ->  let mp1, mp2 = construit_mp1 l1 q2 0 p in mp1, t2::mp2
         | F, _, _ -> let mp1, mp2 = construit_mp1 l1 q2 (n-1) p in t2::mp1, mp2
         | M, _, 0 -> let mp1, mp2 = construit_mp1 l1 q2 n 0 in  mp1, t2::mp2
         | M, _, _ ->  let mp1, mp2 = construit_mp1 l1 q2 n (p-1) in t2::mp1, mp2
       end
  in construit_mp1 lst1 lst2 new_n1 new_p1
;;

let cantor x y =
  x + (x+y)*(x+y+1)/2
;;

let rec cantor_rec x y =
  match x with
  | 0 -> y*(y+1)/2
  | _ -> 1 + cantor_rec (x-1) (y+1)
;;

let rec carre x y =
  if x = 0
  then y*y
  else
    if y < x
    then 1 + carre x (y+1)
    else 1 + carre (x-1) y
;;
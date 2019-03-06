(* Q1 *)

Random.self_init ()

let rec  liste_alea n =
  match n with
  | 0 -> []
  | _ -> (Random.int 1000) :: (liste_alea (n-1))
;;

  (** Tri sélection **)
let rec extrait_min l =
  match l with
  | [] -> failwith "Liste vide"
  | [x] -> x, []
  | t::q -> let m, reste = extrait_min q in
	    if t < m
	    then t, q
	    else m, t::reste
;;

let rec tri_selection l =
  match l with
  | [] -> []
  | _ -> let m, reste = extrait_min l in
	 m::(tri_selection reste)
;;

  (** Tri insertion **)
let rec insere x l =
  match l with
  | [] -> [x]
  | t::q -> if x < t
	    then x::l
	    else t::(insere x q)
;;

let rec tri_insertion l =
  match l with
  | [] -> []
  | t::q -> insere t (tri_insertion q)
;;

  (* Tri fusion *)
let rec decoupe l =
  match l with
  | [] -> [], []
  | [x] -> [x], []
  | x::y::q -> let a, b = decoupe q in
	       x::a, y::b
;;

let rec fusionne l1 l2 =
  match l1 with
  | [] -> l2
  | t1::q1 ->
     match l2 with
     | [] -> l1
     | t2::q2 -> if t1 < t2
		 then t1::(fusionne q1 l2)
		 else t2::(fusionne l1 q2)
;;

let rec fusionne l1 l2 =
  match l1, l2 with
  |_, [] -> l1
  |[], _ -> l2
  |t1::q1, t2::q2 -> if t1 < t2
		     then t1::(fusionne q1 l2)
		     else t2::(fusionne l1 q2)
;;
let rec tri_fusion l =
  match l with
  | [] -> []
  | [x] -> [x]
  | _ -> let l1, l2 = decoupe l in
	 fusionne (tri_fusion l1) (tri_fusion l2)
;;

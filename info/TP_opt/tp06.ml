(* Q1 *)
let rec est_sous_sequence l1 l2 =
  match l1, l2 with
  |[], _ -> true
  | _, [] -> false
  | t1::q1, t2::q2 ->
     if t1 = t2
     then est_sous_sequence q1 q2
     else est_sous_sequence l1 q2	        
;;

  (* Q2 : 2^n sous-séquences *)

  (* Q3 *)

let rec sous_sequences lst =
  (* ajoute_ou_pas renvoie la liste de listes 
obtenue en ajoutant ou pas x 
à chaque liste de la liste de listes ll *)
  let rec ajoute_ou_pas x ll =
    match ll with
    | [] -> []
    | lt::llq -> lt::(x::lt)::(ajoute_ou_pas x llq)
  in
  match lst with
  | [] -> [[]]
  | t::q ->
     let ss_sq_q = sous_sequences q in
     ajoute_ou_pas t ss_sq_q
;;
  

let rec sous_sequences lst =
  match lst with
  | [] -> [[]]
  | t::q ->
     let ss_sq_q = sous_sequences q in
     ss_sq_q@(List.map (fun l -> t::l) ss_sq_q)
;;


  (* Q4 *)
let plssc1 l1 l2 =
  let ssl1 = sous_sequences l1 in
  let lm = ref [] in
  let rec aux lst =
    match lst with
    | [] -> !lm
    | t::q -> if est_sous_sequence t l2
		 && List.length t > List.length !lm
	      then lm := t;
	      aux q
  in aux ssl1
;;

  (* Q11 *)
let lplssc2 l1 l2 =
  let t1 = Array.of_list l1 in
  let t2 = Array.of_list l2 in
  let len1 = Array.length t1 in
  let len2 = Array.length t2 in  
  let mat_L = Array.make_matrix
		(len1 + 1)
		(len2 + 1)
		0 in
  for i = 1 to len1 do
    for j = 1 to len2 do
      if t1.(i-1) = t2.(j-1)
      then
	mat_L.(i).(j) <- 1 + mat_L.(i-1).(j-1)
      else
	mat_L.(i).(j) <- max mat_L.(i-1).(j) mat_L.(i).(j-1)	   	
    done
  done;
  mat_L.(len1).(len2)
;;
	  

  (* Q13 *)
let plssc2 l1 l2 =
  let t1 = Array.of_list l1 in
  let t2 = Array.of_list l2 in
  let len1 = Array.length t1 in
  let len2 = Array.length t2 in  
  let mat_L = Array.make_matrix
		(len1 + 1)
		(len2 + 1)
		0 in
  for i = 1 to len1 do
    for j = 1 to len2 do
      if t1.(i-1) = t2.(j-1)
      then
	mat_L.(i).(j) <- 1 + mat_L.(i-1).(j-1)
      else
	mat_L.(i).(j) <- max mat_L.(i-1).(j) mat_L.(i).(j-1)	   	
    done
  done;
  let rec reconstruit i j fin =
    match (i, j) with
    | (0, _) -> fin
    | (_, 0) -> fin
    | (i, j) ->
       if mat_L.(i).(j) =  mat_L.(i-1).(j-1) + 1 
       then reconstruit (i-1) (j-1) (t1.(i-1)::fin)
       else
	 if mat_L.(i).(j) =  mat_L.(i-1).(j)
	 then reconstruit (i-1) j fin
	 else reconstruit i (j-1) fin
  in
  reconstruit len1 len2 []		 
;;

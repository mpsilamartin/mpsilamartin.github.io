let question3 l = 
match l with
| x::[] -> true
| x::y::[] -> true
| [] -> true
| _ -> false
;;

let question3 l =
match l with
| x::y::z::q -> false
| _ -> true
;;

let question4 l =
match l with
| x::_ -> x
| _ -> false
;;

let question4 l =
match l with
| true::_ -> true
| _ -> false
;;

let question5 l =
match l with
|false::true::_ -> true
| _ -> false
;;

let rec question6 l =
match l with 
| [] | [_]-> failwith "Pas assez d'éléments
"
| [a; b] -> a
| t::q -> question6 q
;;

let rec carre l = 
match l with
| [] -> []
| a::q -> a*a :: carre q
;;

carre [1;2;3;4];;

let rec somme l =
match l with
| [] -> 0
| a::q -> a + somme q
;;

let rec length l =
match l with
| [] -> 0
| a::q -> 1 + length q
;;

let rec mem x l =
match l with
| t::q ->   if t = x
            then true
            else mem x q
| _ -> false
;;

let rec map f l =
match l with
| [] -> []
| a::q -> (f a)::map f q
;;

map (function x -> x*x) [1;2;3;4];;

let rec filter f l =
match l with
| [] -> []
| t::q ->   if f t
            then t::filter f q
            else filter f q
;;

let entiers n =
    let rec aux a =
        match a with
        | 0 -> []
        | a -> (n+1-a) :: aux (a-1)
    in
    aux n
;;

entiers 4;;

let entiers n =
    let rec aux n k =
    if k > n
    then []
    else k::aux n (k+1)
    in
    aux n 1
;;

entiers 4;;

let entiers n =
    let rec aux k lst =
    match k with 
    | 0 -> lst
    | k -> aux (k-1) (k::lst)
    in
    aux n []
;;

entiers 4;;

let rec append lst1 lst2 =
match lst1 with
| [] -> lst2
| t::q -> t::append q lst2
;;

let pluspetits l =
    match l with
    | [] | [_] -> failwith "Trop court"
    | e1::e2::q ->
        let rec aux (x,y) lst =
        (* On maintient x plus petit que y *)
            match lst with
            | [] -> (x,y)
            | t::q -> if t < x
                      then aux (t,x) q
                      else 
                          if t < y 
                          then aux (x,t) q
                          else aux (x,y) q
        in
        if e1 < e2
        then aux (e1,e2) q
        else aux (e2,e1) q
;;

pluspetits [3;2;9;4;1;5];;

let rec deux_plus_petits l =
  (*Renvoie un couple constitué du min et du suivant *)
  match l with
  | [] -> failwith "Trop court"
  | [_] -> failwith "Trop court"
  | [a; b] -> if a < b then (a, b) else (b, a)
  | t::q -> let a, b = deux_plus_petits q in
            if t <= a
            then (t, a)
            else
              if t <= b
              then (a, t)
              else (a, b)
;;

let rec evalue lst x =
    match lst with
    | [] -> 0
    | [a0] -> a0
    | a::b::q -> evalue (a*x+b::q) x
;;

let rec chgt_signe lst =
    match lst with
    | [] -> 0
    | [_] -> 0
    | t::0::q -> chgt_signe (t::q)
    | a::b::q -> if a*b < 0
                 then 1 + chgt_signe (b::q)
                 else chgt_signe (b::q)
;;        

chgt_signe[0;0;0;1;0;0;-1;0;1];;

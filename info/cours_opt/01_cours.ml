(* Quelques types *)
2 + 2.3;;

float_of_int(2) +. 2.3;;


5 + 7 mod 2;;

3 + 2*4;;

5/2*2;;

2147483648*2147483648;;

2147483648*2147483648 - 1;;

3.**2. +. sqrt(4.);;

sin(asin(0.5));;

tan(1) +. tan(-1);;

(2. < 3.) || (1/0 = 1);;

not (2. < 3.) || (1/0 = 1);;

(3 < 0) && (5/0 = 1);;

(3 > 0) && (5/0 = 1);;


'a';;

"a";;

"MPSI";;

"MP"^"SI";;

String.length;;

String.length "anticonstitutionnellement";;

String.get "anticonstitutionnellement" 5;;

String.sub "anticonstitutionnellement" 4 12;;


("MPSI", 2019)


(* Définitions globales et locales *)
let a = 5;;

let a = 3 in a + 1;;

a;;

let a = 3 and b = 5;;

let c = 2 and d = c + 1;;

(* Expression conditionnelle *)

let x = 2 and y = 3;;

let maxi = if x < y then y else x;;

if x > y then 3 else 1.2;;

let z = 3 + (if x < y then y else x);;

(* Les fonctions *)
fun x -> x + x;;

let f = fun x -> x*x;;

f 4;;

f 4 + 2;;

(fun x -> x^x) "to";;

let g x = x + 1;;


fun x y -> x + y;;

let p = fun x y -> x*y;;

let concat x y = x^y;;

let somme1 = fun x y -> x + y;;

let somme2 = fun (x, y) -> x + y;;


(* Fonctions récursives *)
let rec fact n =
  if n = 0
  then 1
  else n * fact (n-1)

let rec truc n p =
  if n < 0
  then 0
  else 1 + truc (n-1) (p-2)
;;

let rec u n =
  if n = 0
  then 1
  else 3*u(n-1) + 2*v(n-1)
and v n =
  if n = 0
  then 2
  else 2*u(n-1) + 3*v(n-1)
;;

let premier = fun (x, y) -> x
;;

let compose f g = fun x -> f (g x)

let rec est_pair n =
  match n with
  | 0 -> true
  | 1 -> false
  | _ -> if n < 0
         then est_pair (-n)
         else est_pair (n-2)
       
let est_pair n =
  let a = n mod 2 in
  a = 0
;;       
let est_pair n =
  n mod 2 = 0
;;



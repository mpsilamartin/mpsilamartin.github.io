(** Exercice 6 **)
let a = 1;;
let f x = a * x;;
let a = 2 in f 1;;
let a = 3 and f x = a * x;;
(* On se souvient....*)
let c = 3 and d = 2 + c;;
f 1;;

(** Exercice 7 **)
let f1 c d = c + d;;

let f2 (c, d) = c + d;;

let f3 x = (x, x*x);;

let f4 g = 2*(g 1);;

let f5 n =
  fun x -> 2*x + n
;;

let f6 n g = (g (n+1) ) + 1;;

(** Exercice 8 **)
fun x y z -> x y z;;
fun f x y -> f x y;;

let truc = fun f x y -> f x y;;

fun x y z -> x+y+z;;

fun x y z -> x (y z);;

fun x y z -> (x y) + (x z);;

(** Exercice 9 **)

(* curry prend une fonction de type
'a*'b -> 'c et renvoie la "même" fonction
'a -> 'b -> 'c *)

let f_par (x, y) = x + y;;

let curry f =
  let fc x y = f (x, y) in
  fc
;;
let f_sans_par = curry f_par;;

let curry f =
  fun x y -> f (x, y);;

let uncurry f =
  let fu (x, y) = f x y in
  fu
;;

let uncurry f =
  fun (x, y) -> f x y;;

(** Exercice 12 **)

let rec facto n =
  match n with
  | 0 -> 1
  | _ -> n * facto (n-1)
;;

let coeff_bin n p =
  facto n / (facto p * facto (n-p))
;;

let rec coeff_bin2 n p =
  if n > 0
  then
    if p = 0
    then 1
    else
      coeff_bin2 (n-1) (p-1) +
        coeff_bin2 (n-1) p
  else
    if n = 0
    then
      if p = 0
      then 1
      else 0
    else
      failwith "n négatif"
;;

let rec coeff_bin2 n p =
  match (n, p) with
  | (_, 0) -> 1
  | (0, _) -> 0
  | (_, _) -> coeff_bin2 (n-1) (p-1) +
                coeff_bin2 (n-1) p
;;

let rec coeff_bin3 n p =
  match (n, p) with
  | (_, 0) -> 1
  | (0, _) -> 0
  | (_, _) ->
     int_of_float (
         (float_of_int n) /.
           (float_of_int p)
           *.
             (float_of_int
                (coeff_bin3 (n-1) (p-1))
             )
       )
             
;;


let rec coeff_bin3 n p =
  match (n, p) with
  | (_, 0) -> 1
  | (0, _) -> 0
  | (_, _) -> n*(coeff_bin3 (n-1) (p-1))
              /p           
;;

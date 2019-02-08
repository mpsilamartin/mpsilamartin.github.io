let a = 1
          
let f x = a * x;;
let a = 2 in f 1;;
let rec a = 3 and f x = a * x;;
f 1;;


(* Exercice 7 *)

fun x y -> x+y;;
let f x y = x + y;;

fun (x, y) -> x + y;;

fun x -> (x+x,x);;
let f = fun 1 -> 2;;


let g f = 3*(f 3);;

let g = fun f -> 3*(f 3);;

fun x -> (fun y -> x+y);;
(* int -> (int -> int) est le même type 
que int -> int -> int *)


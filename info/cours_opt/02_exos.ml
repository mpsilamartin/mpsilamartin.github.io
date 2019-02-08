(* Exercice 1 *)
type complexe = { re : float ; im : float ;};;


let module_complexe = fun z ->
  let a = z.re in
  let b = z.im in
  sqrt (a**2. +. b**2.)
;;

let produit z1 z2 =
  let a = z1.re *. z2.re -. z1.im *. z2.im
  and b = z1.re *. z2.im +. z1.im *. z2.re
  in { re = a ; im = b;}
;;
  

let produit z1 z2 =
  { re = z1.re *. z2.re -. z1.im *. z2.im;
    im = z1.re *. z2.im +. z1.im *. z2.re;
  }
;;

(* Exercice 2 *)
type reel_etendu =
  | PlusInfini
  | MoinsInfini
  | Reel of float
;;

let etendu_of_float = fun x ->
  Reel x
;;

let somme a b =
  match a, b with
  | PlusInfini, MoinsInfini->
     failwith "Non !!!!"
  | MoinsInfini, PlusInfini ->
     failwith "Horreur !!!!"
  | PlusInfini, _ -> PlusInfini
  | _, PlusInfini -> PlusInfini
  | MoinsInfini, _ -> MoinsInfini
  | _, MoinsInfini -> MoinsInfini
  | Reel z1, Reel z2 -> Reel (z1 +. z2)
;;
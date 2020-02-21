(** Exercice 1 **)
type complexe = {
    r : float ;
    i : float
  };;

let i = {r = 0. ; i = 1.};;

let modul z =
  sqrt(z.i**2. +. z.r**2.)
;;

let produit a b =
  {
    r = a.r *. b.r -. a.i *. b.i ;
    i = a.r *. b.i +. a.i *. b.r
  }
;;

(** Exercice 2 **)

type reel_etendu =
  | PlusInf
  | MoinsInf
  | Reel of float
;;

let etendu_of_float x =
  Reel x
;;

let somme x y =
  match x, y with
  | PlusInf, MoinsInf ->
     failwith "Pas content"
  | MoinsInf, PlusInf ->
     failwith "Pas content"
  | PlusInf, _ -> PlusInf
  | MoinsInf, _ -> MoinsInf
  | _, PlusInf -> PlusInf
  | _, MoinsInf -> MoinsInf
  | Reel a, Reel b -> Reel (a +. b)
;;

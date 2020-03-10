(** Exercice 1 **)
type complexe = {
    reel : float ;
    img : float
  };;

let modul {reel = x; img = y} =
  sqrt(x**2. +. y**2.)
;;

let modul z =
  sqrt(z.reel ** 2. +. z.img ** 2.)
;;

let modul z =
  let a = z.reel and b = z.img in
  sqrt(a**2. +. b**2.)
;;

let produit z1 z2 =
  {
    reel =
      z1.reel *. z2.reel -. z1.img *. z2.img;
    img =
      z1.reel *. z2.img +. z1.img *. z2.reel
  };;

(** Exercice 2 **)
type reel_etendu =
  | PlusInfini
  | MoinsInfini
  | Reel of float
;;

(* Convertit un float en reel_etendu *)
let etendu_of_float x =
  Reel x 
;;

(* Ajoute deux réels étendus *)
let somme x y =
  match x with
  | PlusInfini ->
     if y = MoinsInfini
     then failwith "Non défini"
     else PlusInfini
  | MoinsInfini ->
     if y = PlusInfini
     then failwith "Non défini"
     else MoinsInfini
  | Reel a ->
     if y = MoinsInfini
     then MoinsInfini
     else
       if y = PlusInfini
       then PlusInfini
       else
         let Reel b = y in
         Reel (a +. b)     
;;
let somme x y =
  match x with
  | PlusInfini ->
     if y = MoinsInfini
     then failwith "Non défini"
     else PlusInfini
  | MoinsInfini ->
     begin
       match y with
       |PlusInfini -> failwith "Non défini"
       | _ -> y
     end
  | Reel a ->
     match y with
     | Reel b -> Reel (a +. b)
     | _ -> y
;;

let somme x y =
  match x, y with
  | MoinsInfini, PlusInfini ->
     failwith "FI"
  | PlusInfini, MoinsInfini ->
     failwith "FI"
  | PlusInfini, _ -> PlusInfini
  | MoinsInfini, _ -> MoinsInfini
  | _, PlusInfini  -> PlusInfini
  | _, MoinsInfini -> MoinsInfini
  | Reel a, Reel b -> Reel (a +. b)
;;

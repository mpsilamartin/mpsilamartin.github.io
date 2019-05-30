let rec sac_a_dos les_wv wmax =
  let n = Array.length les_wv in
  let col =
    ref (Array.make (wmax+1) 0) in
  for j = 1 to n do
    let wj, vj = les_wv.(j-1) in
    let new_col =
      Array.make (wmax+1) 0 in
    for w = 0 to wmax do
      if wj > w
      then new_col.(w) <- !col.(w)
      else new_col.(w) <-
             max (vj + !col.(w-wj))
               (!col.(w))
    done;
    col := new_col
  done;
  !col.(wmax)
;;
  
let mes_wv = [|(5, 3);
               (2,7);
               (9,789);
               (1515, 10) ;
               (14, 7);
               (1,1) ;
               (0, 0) ;
               (8, 9) ;
               (9, 8) |];;
let mon_sd = 33;;


sac_a_dos mes_wv mon_sd;;

let rec sac_a_dos les_wv wmax =
  let n = Array.length les_wv in
  let col = Array.make (wmax+1) 0 in
  for j = 1 to n do
    let wj, vj = les_wv.(j-1) in
    for w = wmax downto 0 do
      if wj > w
      then col.(w) <- col.(w)
      else col.(w) <-
             max (vj + col.(w-wj))
               (col.(w))
    done;
  done;
  col.(wmax)
;;

(* Distance d'édition *)
let malo = "MALO";;
let laio = "LÉO";;

let distance m1 m2 =
  let n1 = String.length m1 in
  let n2 = String.length m2 in
  let mb = Array.make_matrix (n1+1) (n2+1) 0 in
  for i = 0 to n1 do
    for j = 0 to n2 do
      match (i,j) with
      | (0, _) ->
         mb.(i).(j) <- j
      | (_, 0) ->
         mb.(i).(j) <- i
      | (_, _) ->
         let c1 = String.get m1 (i-1) in
         let c2 = String.get m2 (j-1) in
         if c1 = c2
         then
           mb.(i).(j) <- mb.(i-1).(j-1)
         else
           mb.(i).(j) <-
             1 +
               min
                 (min mb.(i).(j-1)
                      mb.(i-1).(j))
                 mb.(i-1).(j-1)
    done
  done;
  let liste = ref [] in
  let i = ref n1 in
  let j = ref n2 in
  while !i > 0 || !j > 0 do
    let c1 = String.get m1 (!i-1) in
    let c2 = String.get m2 (!j-1) in
    if c1 = c2
    then
      begin
        liste := "G"::!liste;
        i := !i-1;
        j := !j-1
      end
    else
      begin
        if mb.(i).(j-1) < mb.(i-1).(j)
        then
          if mb.(i).(j-1) <mb.(i-1).(j-1)
          then failwith "ATerminer"
        else raise AVousDeJouer
      end
  mb.(n1).(n2)
;;
                                  

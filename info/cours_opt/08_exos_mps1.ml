let sac_a_dos wmax les_wv =
  let n = Array.length les_wv in
  let mat_k =
    Array.make_matrix (wmax+1) (n+1) 0 in
  for j = 1 to n do
    let wj, vj = les_wv.(j-1) in 
    for w = 0 to wmax do
      if wj > w
      then mat_k.(w).(j) <- mat_k.(w).(j-1)
      else mat_k.(w).(j) <-
             max (vj + mat_k.(w-wj).(j-1))
               (mat_k.(w).(j-1))
    done
  done;
  mat_k.(wmax).(n)
;;
  
  
let sac_a_dos wmax les_wv =
  let n = Array.length les_wv in
  let mat_k =
    Array.make_matrix (wmax+1) (n+1) 0 in
  for j = 1 to n do
    let wj, vj = les_wv.(j-1) in 
    for w = 0 to wmax do
      mat_k.(w).(j) <-
        if wj > w
        then mat_k.(w).(j-1)
        else max (vj + mat_k.(w-wj).(j-1))
               (mat_k.(w).(j-1))
    done
  done;
  let rec contenu w j acc =
    match j with
    | 0 -> acc
    | _ ->
       let wj, vj = les_wv.(j-1) in 
       if wj > w
       then contenu w (j-1) acc
       else
         if vj + mat_k.(w-wj).(j-1) > mat_k.(w).(j-1)
         then contenu (w-wj) (j-1) (j::acc)
         else contenu w (j-1) acc
  in
  mat_k.(wmax).(n), contenu wmax n []
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
let sac_a_dos wmax les_wv =
  let n = Array.length les_wv in
  let colette =
    ref (Array.make (wmax+1) 0) in
  for j = 1 to n do
    let wj, vj = les_wv.(j-1) in
    let jean_claude = Array.make (wmax+1) 0 in
    for w = 0 to wmax do
      jean_claude.(w) <-
        if wj > w
        then !colette.(w)
        else max (vj + !colette.(w-wj)) !colette.(w)
    done;
    colette := jean_claude
  done;
  !colette.(wmax)
;;


(** Distance d'édition **)

(* Reconstruction itérative *)
let distance s1 s2 =
  let n1 = String.length s1 in
  let n2 = String.length s2 in
  let m = Array.make_matrix (n1+1) (n2+1) 0 in
  for i = 1 to n1 do
    m.(i).(0) <- i
  done;
  for j = 1 to n2 do
    m.(0).(j) <- j
  done;
  for i = 1 to n1 do
    for j = 1 to n2 do
       m.(i).(j) <-
         if String.get s1 (i-1) =
              String.get s2 (j-1)
         then m.(i-1).(j-1)
         else 1 + min (min m.(i-1).(j)
                         m.(i).(j-1))
                    m.(i-1).(j-1)
    done;
  done;
  let i, j = ref n1, ref n2 in
  let slt = ref [] in
  while m.(!i).(!j) <> 0 && !i > 0 && !j > 0 do
    if String.get s1 (!i-1) =
         String.get s2 (!j-1)
    then
      begin
        slt := "Pas de modif"::!slt;
        decr i;
        decr j
      end
    else
      begin
        if m.(!i-1).(!j-1) <= m.(!i).(!j-1)
         && m.(!i-1).(!j-1) <= m.(!i-1).(!j)
        then
          begin
            i := !i - 1;
            j := !j - 1;
            slt := "Remplace"::!slt
          end
        else
          if  m.(!i).(!j-1) < m.(!i-1).(!j)
          then 
            begin
              j := !j - 1;
              slt := "Ajoute"::!slt
            end
          else
            begin
              i := !i-1;
              slt := "Supprime"::!slt
            end
      end
  done;
  while !i > 0 do
    i := !i-1;
    slt := "Supprime"::!slt
  done;
  while !j > 0 do
    
    j := !j - 1;
    slt := "Ajoute"::!slt
  done;
  m.(n1).(n2), !slt
;;

(* Reconstruction récursive *)
let distance s1 s2 =
  let n1 = String.length s1 in
  let n2 = String.length s2 in
  let m = Array.make_matrix (n1+1) (n2+1) 0 in
  for i = 1 to n1 do
    m.(i).(0) <- i
  done;
  for j = 1 to n2 do
    m.(0).(j) <- j
  done;
  for i = 1 to n1 do
    for j = 1 to n2 do
       m.(i).(j) <-
         if String.get s1 (i-1) =
              String.get s2 (j-1)
         then m.(i-1).(j-1)
         else 1 + min (min m.(i-1).(j)
                         m.(i).(j-1))
                    m.(i-1).(j-1)
    done;
  done;
  let rec suite m i j acc =
    match i, j with
    | 0, 0 -> acc
    | _, 0 -> suite m (i-1) 0 ("Suppr"::acc)
    | 0, _ -> suite m 0 (j-1) ("Ajout"::acc)
    | _, _ ->
       if String.get s1 (i-1) =
              String.get s2 (j-1)
       then
         suite m (i-1) (j-1) ("PasModif"::acc)
       else
         if m.(i-1).(j-1)
            <= min m.(i-1).(j) m.(i).(j-1)
         then
           suite m (i-1) (j-1) ("Rempl"::acc)
         else
           if  m.(i-1).(j) < m.(i).(j-1)
           then suite m (i-1) j ("Suppr"::acc)
           else suite m i (j-1) ("Ajout"::acc)
  in             
                  
  m.(n1).(n2), suite m n1 n2 []
;;

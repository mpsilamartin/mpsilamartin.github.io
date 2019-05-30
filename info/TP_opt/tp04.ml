let nb_inversion t =
  let n = Array.length t in
  let nb_inv = ref 0 in
  for i = 0 to n-2 do
    for j = i+1 to n-1 do
      if t.(i) > t.(j)
      then incr nb_inv
    done
  done;
  !nb_inv
;;

let fusion t1 t2 =
  let n1 = Array.length t1 in
  let n2 = Array.length t2 in
  let nb_inv = ref 0 in
  if n1+n2 = 0
  then [||], 0
  else
    let t = Array.make (n1+n2) (-1) in
    let i1 = ref 0 and i2 = ref 0 in
    while !i1 < n1 && !i2 < n2 do
      if t1.(!i1) < t2.(!i2)
      then
        begin
          t.(!i1 + !i2) <- t1.(!i1);
          incr i1
        end
      else
        begin
          t.(!i1 + !i2) <- t2.(!i2);
          incr i2;
          nb_inv := !nb_inv + n1 - !i1
        end
    done;
    while !i1 < n1 do
      t.(!i1 + !i2) <- t1.(!i1);
      incr i1
    done;
    while !i2 < n2 do
      t.(!i1 + !i2) <- t2.(!i2);
      incr i2
    done;
    t, !nb_inv
;;

let nb_inversion t =
  let rec trie t =
    let n = Array.length t in
    match n with
    | 0 -> t, 0
    | 1 -> t, 0
    | _ -> 
       let t1, nb_inv1 = trie (Array.sub t 0 (n/2)) in
       let t2, nb_inv2 = trie (Array.sub t (n/2) (n-n/2)) in
       let tab, nb_inv_croise = fusion t1 t2 in
       tab, nb_inv1 + nb_inv2 + nb_inv_croise
  in
  let _, nb_inv = trie t in
  nb_inv
;;

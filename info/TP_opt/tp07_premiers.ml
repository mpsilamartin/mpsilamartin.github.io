(* tables des nombres premiers proches d'une puissance de deux :
   si t.(i) vaut k, alors 2**i - k est premier.
   Les valeurs de t sont toutes strictement positives, sauf la première, négative.
   t est de longueur 40.
*)

let t =
  [| -1; (* 2**0 - (-1) est premier *)
     0; (* 2**1 - 0 est premier *)
     1; (* 2**2 - 1 est premier *)
     1; (* 2**3 - 1 est premier *)
     3; (* 2**4 - 3 est premier *)
     1;
     3;
     1;
     5;
     3;
     3;
     9;
     3;
     1;
     3;
     19;
     15;
     1;
     5;
     1;
     3;
     9;
     3;
     15;
     3;
     39;
     5;
     39;
     57;
     3;
     35;
     1;
     5;
     9;
     41;
     31;
     5;
     25;
     45;
     7; (* 2**39 - 7 est premier *)
    |]

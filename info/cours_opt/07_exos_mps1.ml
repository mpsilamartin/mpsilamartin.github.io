type lexeme =
  | Entier of int
  | Operateur of char
;;

type lexeme =
  | Entier of int
  | Plus
  | Moins
  | Fois
  | Quot
;;

exception ExpressionIncorrecte
let evalue lst =
  let pile = Stack.create () in
  let rec eval reste =
    match reste with
    | [] -> let r = Stack.pop pile in
            if Stack.is_empty pile
            then r
            else raise ExpressionIncorrecte
    | (Entier a)::q -> Stack.push a pile;
                       eval q
    | t::q  ->
       try
         let a = Stack.pop pile in
         let b = Stack.pop pile in
         let res =
           match t with
           | Plus -> a+b
           | Moins -> b-a
           | Fois -> a*b
           | Quot -> b/a
         in
         Stack.push res pile;
         eval q
       with
       | Stack.Empty -> raise ExpressionIncorrecte
  in
  eval lst
;;

let liste = [Entier 3 ;Entier 3 ;Entier 3 ; Plus; Entier 3; Fois];;

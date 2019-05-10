type lexeme =
  | Entier of int
  | Op of char
;;

exception ExpressionNotOk
let evalue lst =
  let p = Stack.create () in
  let rec eval l =
    match l with
    | [] -> if Stack.is_empty p
            then raise ExpressionNotOk
            else
              begin
                let r = Stack.pop p in
                if Stack.is_empty p
                then r
                else raise ExpressionNotOk
              end
    | (Entier x)::q ->
       (* On empile x *)
       Stack.push x p;
       (* On continue *)
       eval q
    | (Op c)::q ->
       let y = Stack.pop p in
       let x = Stack.pop p in
       let res =
         match c with
         | '+' -> x+y
         | '-' -> x-y
         | '*' -> x*y
         | '/' -> x/y
         | _ -> raise ExpressionNotOk
       in
       Stack.push res p;
       eval q
  in
  eval lst
;;                
       

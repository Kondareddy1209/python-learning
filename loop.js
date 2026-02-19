// for (let i=1;i<=5;i++){
//     console.log(i)
// }


// let n=4
// sum=0
// for (let i=1;i<=n;i++){
//     sum+=i
// }
// console.log(sum)

// let n=prompt("Enter the number :")
// s=0
// for(let i=1;i<=n;i++){
//     s+=i
// }
// console.log(s)

// let n=Number(prompt("Enter the number: "))
// let s=0
// let i=1
// while(i<=n){
//     s+=i;
//     i++;
// }
// console.log(s);

// let n=10
// do{
//     console.log("Hello");
// }while(n<=5);


// For -of Loop
// let str="Kondareddy";
// for (let i of str){
//     console.log(i)
// }

// For - in Loop
// let konda={
//     name : "reddy",
//     age : 20,
//     place : "kadapa",
// };
// for (let key in konda){
//     console.log("key=",key,"value=",konda[key])
// }

//print even numbers 0 to 100
// let num=100
// s=0
// for(let i=2;i<=100;i++){
//     if (i % 2==0){
//         console.log(i)
//         s+=i
//     }
// }
// console.log(s)

//print even numbers 0 to 100

// let num=100
// s=0
// i=0
// while(i<=num){
//     if (i %2 ==0){
//         console.log(i)
//         s+=i
//     }
//     i++;
// }
// console.log(s)


//Guess game 

// let gess_game=100;
// let num=Number(prompt("Guess the numeber: "));
// if (gess_game==num){
//     console.log("Correct Guess")
// }else{
//     console.log("Entered Wrong Number")
// }


//Guess game 

let gess_game=100;
let num=prompt("Guess the numeber: ");
while(num !=gess_game){
    num=prompt("You Entered Wrong Number ,Guess Again.....");
}
console.log("You Enterd Correct Number");
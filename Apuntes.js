/* APUNTES */                    //Crtl + F2 para cambiar todos los textos iguales



let numero1= 1, numero2=4;

let nombre = prompt("dime tu nombre");      //Si no se usa let, es como si usaramos var
alert(nombre+" edad "+numero2);

frase = "" + numero1 + numero2; /* Esto no me dara 5, sino 14 xk lo comvierte todo en string*/
frase2 = `soy ${nombre} y tengo ${numero1+numero2} años <br>`  /* Con el accento abierto (backtick) y el ${} podemos poner variables string o numeros dentro de un string*/
/* Se pueden hacer las cadenas de strings tanto con " con ' o con `*/


document.write(frase2);

result = numero1 == numero2; /*Esto dara o true o false, comparacion de igualdad*/
result = numero1 != numero2; /* Con === seria estrictamente igual, que sea lo mismo i ademas el mismo tipo de variable, osea numero, string... */



/* CONDICIONALES*/

if (100 < 50){                           // El if podria ir solo sin else//
    let name = "Dalto"
    document.write(name)
}else if(100<70){
    let name = "dani"               //Si no se cumple lo anterior, un else pero con una condicion igualmente
document.write(name)
}else{                              //Si no se cumple ninguna, pues con el else ya se ejecuta la ultima     
    document.write("No tienes nombre")
} 

dineroConfla="2"
/*De string  a numero */ dineroConfla = parseInt(dineroConfla);  


/* ARRAYS */

let frutas = ["banana", "manzana", "pera"] //Banana posicion 0, manzana posicion 1...
//document.write(frutas[0]) -> banana
let pc = {
    nombre4: "Pc de Dani",      //Array pero con pc[nombre]
    procesador: "Intel",
    ram: "16gb",
    espacio:"1TB"
}; 
let mipc = pc["nombre4"];      //Importante las comillas en pc["__"]
frasePc = `El nombre de mi pc es ${mipc}`;  //Si ponemos ${pc[nombre4]} NO VA, x eso lo sacamos fuera en la linea anterior
document.write(frasePc);




/*
OPERADORES 
let x,y;

x=y
x += y seria x = x+y
x -= y seria x = x-y
x *= y seria x = x*y
x /= y seria x = x/y
x %= y seria x = x%y
x **= y seria x = x**y exponencial
x <<= y seria x = 
x >>= y seria x = 
x >>>=y seria x = 
x &= y seria x =  AND
x ^= y seria x =  XOR
x |= y seria x =  OR

COMPARADORES
== != !== === 

COMPARADORES LOGICOS (solo aceptan true o false)
&& and -> si entre los dos valores hay algun false, sera false. Si todos son true da true.
|| or -> si entre los valores hay algun true, dara true
!VALOR; -> Para cambiar el valor que habia antes. Si antes era true, ahora sera false

document.write(num1 < num2 || num1 == num2); Si solo se cumple 1 pues ya dara true.
Si fuera && (and), tendrian que cumplirse las 2.
*/

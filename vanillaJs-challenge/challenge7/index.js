
const span = document.querySelector("span");
const numberBtn = document.querySelectorAll(".number");
const operatorBtn = document.querySelectorAll(".operator");
const equal = document.querySelector(".equal");
const reset = document.querySelector(".js-reset");
let btnArray = document.querySelectorAll("button");

let inputNumber = 0;
let result = 0;
let newNumber = 0;
let operator = null;

function doReset(event){
    event.preventDefault();
    inputNumber = 0;
    newNumber = 0;
    result = 0;
    operator = null;
    span.innerText = result;
    console.log(result);
}


function calculate(event){
    event.preventDefault();
    if(operator === "+"){
        result = result + inputNumber + newNumber;
        inputNumber = 0;
        newNumber = 0;
        operator = null;        
        console.log(result);
        span.innerText = result;
    }
    else if(operator === "-"){
        if(result === 0){
            result = inputNumber-newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        else{
        result = result -(inputNumber+newNumber);
        inputNumber = 0;
        newNumber = 0;
        operator = null;
        }
        console.log(result);
        span.innerText = result; 
    }
    else if(operator === "*")
    {
        if(result===0){
            result = inputNumber * newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        else{
            result = result *newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        console.log(result);
        span.innerText = result; 
    }
    else if(operator === "/"){
        if(result === 0){
            result = inputNumber/newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        else{
            result = result/newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        console.log(result);
        span.innerText = result; 
    }
}

function calculate2(){
    if(operator === "+"){
        result = result + inputNumber + newNumber;
        inputNumber = 0;
        newNumber = 0;
        operator = null;        
        console.log(result);
        
    }
    else if(operator === "-"){
        if(result === 0){
            result = inputNumber-newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        else{
        result = result -(inputNumber+newNumber);
        inputNumber = 0;
        newNumber = 0;
        operator = null;
        }
        console.log(result);
        
    }
    else if(operator === "*")
    {
        if(result===0){
            result = inputNumber * newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        else{
            result = result *newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        console.log(result);
         
    }
    else if(operator === "/"){
        if(result === 0){
            result = inputNumber/newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        else{
            result = result/newNumber;
            inputNumber = 0;
            newNumber = 0;
            operator = null;
        }
        console.log(result);
         
    }
}

function addInputNumber(event){
    event.preventDefault();
    if(operator === null){
        if(inputNumber===0){
        inputNumber = parseInt(event.target.innerText);
        span.innerText = inputNumber;
        console.log(inputNumber);
        }
        else{
            inputNumber = inputNumber*10 + parseInt(event.target.innerText);
            span.innerText = inputNumber;
            console.log(inputNumber);
        }
    }
    else{
        if(newNumber === 0){
            newNumber = parseInt(event.target.innerText);
            span.innerText = newNumber;
            console.log(newNumber);
        }
        else{
            newNumber = newNumber*10 + parseInt(event.target.innerText);
            span.innerText = newNumber;
            console.log(newNumber);
        }
    
    }
    
}



function addOperator(event){
    event.preventDefault();
    if(operator === null){
        operator = event.target.innerText;
    }
    else{
        calculate2();
        span.innerText = result;
        operator = event.target.innerText;
    }
}


function init(){
    numberBtn.forEach(function(elem){
        elem.addEventListener("click",addInputNumber);
    });

     operatorBtn.forEach(function(elem){
          elem.addEventListener("click",addOperator);
     });
    equal.addEventListener("click",calculate);
    reset.addEventListener("click",doReset);
} 

init();

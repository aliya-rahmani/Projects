
let firstName=document.querySelector(".firstName");
let lastName=document.querySelector(".lastName");
let email=document.querySelector(".email");
let password=document.querySelector(".password");
let phone=document.querySelector(".phone");
let bio=document.querySelector(".bio");
let inp=document.getElementsByTagName("input");
let button=document.querySelector("button");

firstName.style.display="none";
lastName.style.display="none";
email.style.display="none";
password.style.display="none";
phone.style.display="none";
bio.style.display="none";

let res1=false;
let res2=false;
let res3=false;
let res4=false;
let res5=false;
let res6=false;


inp[0].addEventListener("input",function(e){
    if (e.target.value==""){
        res1=false;
        firstName.style.display="none";
        inp[0].style.border="1px solid #D0D3D4";
        inp[0].style.boxShadow="0px 1px 1px #B3B6B7";
    }
    else{
        let values=e.target.value; 
        let pattern=/^[A-Za-z0-9 ]{3,16}$/; 
        let result=pattern.test(values);
        
        if (result){
            res1=true;
            firstName.style.display="none";
            inp[0].style.border="3px solid #51C37C";
            inp[0].style.boxShadow="none";
        }
        else{
            res1=false;
            firstName.style.display="block";
            inp[0].style.border="1px solid #F94739 ";
            inp[0].style.boxShadow="0px 1px 1px #B3B6B7";
        }
    }
});



inp[1].addEventListener("input",function(e){
    if (e.target.value==""){
        res2=false;
        lastName.style.display="none";
        inp[1].style.border="1px solid #D0D3D4";
        inp[1].style.boxShadow="0px 1px 1px #B3B6B7";
    }
    else{
        let values=e.target.value; 
        let pattern=/^[A-Za-z0-9 ]{3,16}$/; 
        let result=pattern.test(values);
        
        if (result){
            res2=true;
            lastName.style.display="none";
            inp[1].style.border="3px solid #51C37C";
            inp[1].style.boxShadow="none";
        }
        else{
            res2=false;
            lastName.style.display="block";
            inp[1].style.border="1px solid #F94739 ";
            inp[1].style.boxShadow="0px 1px 1px #B3B6B7";
        }
    }
});



inp[2].addEventListener("input",function(e){
    if (e.target.value==""){
        res3=false;
        email.style.display="none";
        inp[2].style.border="1px solid #D0D3D4";
        inp[2].style.boxShadow="0px 1px 1px #B3B6B7";
    }
    else{
        let values=e.target.value; 
        let pattern=/^[a-zA-Z0-9\.]+@+[a-z]+\.[a-z]{3}$/; 
        let result=pattern.test(values);
        
        if (result){
            res3=true;
            email.style.display="none";
            inp[2].style.border="3px solid #51C37C";
            inp[2].style.boxShadow="none";
        }
        else{
            res3=false;
            email.style.display="block";
            inp[2].style.border="1px solid #F94739 ";
            inp[2].style.boxShadow="0px 1px 1px #B3B6B7";
        }
    }
});


inp[3].addEventListener("input",function(e){
    if (e.target.value==""){
        res4=false;
        password.style.display="none";
        inp[3].style.border="1px solid #D0D3D4";
        inp[3].style.boxShadow="0px 1px 1px #B3B6B7";
    }
    else{
        let values=e.target.value; 
        let pattern=/^[a-zA-Z0-9 @,_-]{6,20}$/; 
        let result=pattern.test(values);
        
        if (result){
            res4=true;
            password.style.display="none";
            inp[3].style.border="3px solid #51C37C";
            inp[3].style.boxShadow="none";
        }
        else{
            res4=false;
            password.style.display="block";
            inp[3].style.border="1px solid #F94739 ";
            inp[3].style.boxShadow="0px 1px 1px #B3B6B7";
        }
    }
});


inp[4].addEventListener("input",function(e){
    if (e.target.value==""){
        res5=false;
        phone.style.display="none";
        inp[4].style.border="1px solid #D0D3D4";
        inp[4].style.boxShadow="0px 1px 1px #B3B6B7";
    }
    else{
        let values=e.target.value; 
        let pattern=/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/; 
        let result=pattern.test(values);
        
        if (result){
            res5=true;
            phone.style.display="none";
            inp[4].style.border="3px solid #51C37C";
            inp[4].style.boxShadow="none";
        }
        else{
            res5=false;
            phone.style.display="block";
            inp[4].style.border="1px solid #F94739 ";
            inp[4].style.boxShadow="0px 1px 1px #B3B6B7";
        }
    }
});



inp[5].addEventListener("input",function(e){
    if (e.target.value==""){
        res6=false;
        bio.style.display="none";
        inp[5].style.border="1px solid #D0D3D4";
        inp[5].style.boxShadow="0px 1px 1px #B3B6B7";
    }
    else{
        let values=e.target.value; 
        let pattern=/^[a-z-_\s]{8,50}$/; 
        let result=pattern.test(values);
        
        if (result){
            res6=true;
            bio.style.display="none";
            inp[5].style.border="3px solid #51C37C";
            inp[5].style.boxShadow="none";
        }
        else{
            res6=false;
            bio.style.display="block";
            inp[5].style.border="1px solid #F94739 ";
            inp[5].style.boxShadow="0px 1px 1px #B3B6B7";
        }
    }
});

document.querySelector("form").addEventListener("keyup",function(){
    if (res1 && res2 && res3 && res4 && res5 && res6){
        button.style.backgroundColor="#51C37C";
        button.disabled=false;
    }
    else{
        button.style.backgroundColor="#4B4D4D";
        button.disabled=true;
    }
});
button.addEventListener('click',function(){
    
});




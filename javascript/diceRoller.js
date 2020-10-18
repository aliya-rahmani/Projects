const diceRoller = (x,y) =>{
  
  const aux = [];
  for (var i = 0; i < x; i++){
    aux.push(Math.floor((Math.random() * y)+1));
  }
  console.log(aux);
}
 diceRoller(4,20);

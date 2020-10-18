console.log("starting");
var settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india",
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com",
		"x-rapidapi-key": "bcd247492amsh6e64b6f5354d967p1a13fejsncc365ce3c2dc"
	}
}

console.log("after settings");

$.ajax(settings).done(function (response) {
    console.log(response);
    console.log("inside ajax after response");

     $("#total_value").html("<li>Total Cases: "+response.total_values.confirmed+"</li>");
     $("#total_value").append("<li>Active Cases: "+response.total_values.active+"</li>");
     $("#total_value").append("<li>Death Cases: "+response.total_values.deaths+"</li>");
     $("#total_value").append("<li>Recovered: "+response.total_values.recovered+"</li>");
     $("#total_value").append("<li>LastUpdatedAt: "+response.total_values.lastupdatedtime+"</li>");
    var a = [];
    a = Object.getOwnPropertyNames(response.state_wise);
    a.sort();
    
    $("#li").html("<li class='button1'>" + a[0] + "</li>")
    for(var i = 1;i<a.length;i++){
         $("#li").append("<li class='button1'>" + a[i] + "</li>")
    }
var state;


$(".button1").click(function(){
    state = $(this).html();
    console.log(state);         
    $(".details").html("<h4>"+response["state_wise"][state]["state"]+ "</h4>")
    $(".details").append("<li>Total Cases: "+response["state_wise"][state]["confirmed"]+"</li>");
    $(".details").append("<li>Active Cases: "+response["state_wise"][state]["active"]+"</li>");
    $(".details").append("<li>Total Deaths: "+response["state_wise"][state]["deaths"]+"</li>");
    $(".details").append("<li>Recovered: "+response["state_wise"][state]["recovered"]+"</li>");
    $(".details2").html(" ");
     districtslist(state);
})

$("#input1").keypress(function(event){   
if(event.which===13){
    state = $(this).val();
    $(this).val("");
    state = titleCase(state);
    console.log(state);

    console.log(response["state_wise"][state]["active"]);
    $(".details").html("<h4>"+response["state_wise"][state]["state"]+ "</h4>")
    $(".details").append("<li>Total Cases: "+response["state_wise"][state]["confirmed"]+"</li>");
    $(".details").append("<li>Active Cases: "+response["state_wise"][state]["active"]+"</li>");
    $(".details").append("<li>Total Deaths: "+response["state_wise"][state]["deaths"]+"</li>");
    $(".details").append("<li>Recovered: "+response["state_wise"][state]["recovered"]+"</li>");
    $(".details2").html(" ");
        districtslist(state);
    }})

function districtslist(state){
      var b=[];
         b  = Object.getOwnPropertyNames(response["state_wise"][state]["district"]);
           $("#li2").html(" ");
           b.sort();
           for(var i =0;i<b.length;i++){
                 $("#li2").append("<li class='button2'>" + b[i] + "</li>")
           }
           $("#input2").html("<input type='text' id ='here' placeholder='Enter district name'>")

           districtdetails(state);
    }
 
function districtdetails(state){
var districtu;
$(".button2").click(function(){    
    districtu = $(this).html();
    console.log(districtu);
    $(".details2").html("<h4>"+districtu+"</h4>")
    $(".details2").append("<li>Total Cases: "+response["state_wise"][state]["district"][districtu]["confirmed"]+"</li>");
    $(".details2").append("<li>Active Cases: "+response["state_wise"][state]["district"][districtu]["active"]+"</li>");
    $(".details2").append("<li>Total Deaths: "+response["state_wise"][state]["district"][districtu]["deceased"]+"</li>");
    $(".details2").append("<li>Recovered: "+response["state_wise"][state]["district"][districtu]["recovered"]+"</li>");
})

$("#here").keypress(function(event){  
if(event.which===13){
districtu = $(this).val();
    $(this).val("");
    districtu = titleCase(districtu);
    console.log(districtu);
    console.log(state);
    $(".details2").html("<h4>"+districtu+"</h4>")
    $(".details2").append("<li>Total Cases: "+response["state_wise"][state]["district"][districtu]["confirmed"]+"</li>");
    $(".details2").append("<li>Active Cases: "+response["state_wise"][state]["district"][districtu]["active"]+"</li>");
    $(".details2").append("<li>Total Deaths: "+response["state_wise"][state]["district"][districtu]["deceased"]+"</li>");
    $(".details2").append("<li>Recovered: "+response["state_wise"][state]["district"][districtu]["recovered"]+"</li>");
}})
}
});
function titleCase(str) {
   var splitStr = str.toLowerCase().split(' ');
   for (var i = 0; i < splitStr.length; i++) {
       splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);     
   }
   
   return splitStr.join(' '); 
}

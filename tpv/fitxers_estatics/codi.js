window.onload = rellotge();
		
function rellotge(){
    var ara     = new Date(); 
    var any    = ara.getFullYear();
    var mes   = ara.getMonth()+1; 
    var dia     = ara.getDate();
    var hora    = ara.getHours();
    var minut  = ara.getMinutes();
    var segon  = ara.getSeconds(); 
    
    if(mes.toString().length == 1)         	var mes = '0' + mes;
    if(dia.toString().length == 1)         	var dia = '0' + dia;
    if(hora.toString().length == 1)         var hour = '0' + hora;
    if(minut.toString().length == 1)        var minut = '0' + minut;
    if(segon.toString().length == 1)        var segon = '0' + segon;
 
    var dataHora = dia + '/' + mes + '/' + any + ' ' + hora + ':' + minut + ':' + segon;
    setTimeout("rellotge()",1000);
    document.getElementById("dataHora").innerHTML=dataHora;
    
}
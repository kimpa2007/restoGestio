$(document).ready(function() { 
   setInterval(function() {
	   $.ajax({
		   url : "/gestio/dataHora",
		   type : "GET",
		   dataType: "json",
		   success : function(dataHora) {
    		   $("#dataHora").text(dataHora);
		   },
		   error : function(xhr,errmsg,err) {
			   console.log("error")
		   }
       });
   },1000);
   var separat;
   
    $('.categories').click(function() {
	    $('#productes').empty();
        var cat = $(this).attr('value'); 
        
    	var n = $('#nouProducte').attr('href').lastIndexOf("/");
    	var abans = $('#nouProducte').attr('href').substring('0',n+1);
    	var urlNova = abans+cat;
    	$("#nouProducte").attr('href', urlNova);
    	
        $.ajax({
        	url : "/productes/llistarProductes",
        	type : "GET",
        	dataType: "json",
        	data : {
        		categoria : cat,
        	},
        	
        	success : function(productes) {
        		var i = 0;
        		  $.each(productes, function() {
        		      var id = this['pk'];
        		      var producte = this['fields']['producte'];
        		      var img = this['fields']['imatge'];
        		      var imatge = "/media/" + this['fields']['imatge'];

        		      if(img.length > 0){ 
	        		      $('#productes').append("<div  class='col-md-1 element'  id='" + id + 
	        		    		  "'><a href='http://127.0.0.1:8000/productes/editarProducte/" + id +"'><img class='img-responsive' src='" + imatge +
	        		    		  "'><p class='etiqueta'>" +
	        		    		  producte + "</p></a></div>");
	        		      }
        		      else{
	        		      $('#productes').append("<div class='col-md-1 col-md element'  id='" + id + 
	        		    		  "'><a href='http://127.0.0.1:8000/productes/editarProducte/" + id + "'><p class='etiqueta senseImg'>" +  producte + "</p></a></div>");
	        		   
        		      }
        		      i++;
        		  });
        	},
        	error : function(xhr,errmsg,err) {
        		console.log
        	}
        	});
        	return false;
    }); 
    var comanda;
    var pagament;
    var total="000";
    
    $(".cobrar").click(function (){
    	$("#total").empty();
    	$("#total1").empty();
    	$("#normal").prop("checked","true");
    	//$("#total2").empty();
    	comanda = $(this).attr("id");
    	
        $.ajax({
        	url : "/comandes/obtenirTotal/" + comanda,
        	type : "GET",
	        contentType: "application/json",
        	success : function(t){
        		total = t['total'];
            	$("#total").append("<div>Total a cobrar: " + total + "€</div>");
        	},
	        error: function (xhr, errmsg, err) {
	        	alert(xhr.status + " " + xhr.responseText);
	        }
        });
		$("#myModal").modal('show');
    });

    
    $("#efectiu").click(function (){
    	$("#myModal").modal('hide');
    	$("#meffectiu").modal('show');
    	pagament = "efectiu";
    });
    
    $("#targeta").click(function (){
    	$("#myModal").modal('hide');
    	$("#total1").append("<div> Total a cobrar: " + total + "€</div>");
    	pagament = "targeta";
    	guardarPagament();
    });
    
    $("#donaCanvi").click(function (){
    	var qtatDonada = $("#qtatDonada").val();
    	console.log(qtatDonada)
    	
    	$.ajax({
        	url : "/gestio/donaCanvi/" +qtatDonada + "/" + total,
        	type : "GET",
	        contentType: "application/json",
        	success : function(t){
        		//Ensenyar modal am el canvi o insult si cal
        	},
	        error: function (xhr, errmsg, err) {
	        	alert(xhr.status + " " + xhr.responseText);
	        }
        });

    });
    
    function guardarPagament(){
    	comanda = comanda.trim()
    	$.ajax({
        	url : "/gestio/guardarPagament/" +comanda + "/" + pagament,
        	type : "GET",
	        contentType: "application/json",
        	success : function(t){
            	$("#mtargeta").modal('show');
        	},
	        error: function (xhr, errmsg, err) {
	        	alert(xhr.status + " " + xhr.responseText);
	        }
        });
    }
    $(".ok").click(function(){
    	location.reload();
    });
}); 
$(document).ready(function() { 
   setInterval(function() {
	   $.ajax({
		   url : "/gestio/dataHora",
		   type : "GET",
		   dataType: "json",
		   success : function(dataHora) {
			   console.log(dataHora)
    		   $("#dataHora").text(dataHora);
		   },
		   error : function(xhr,errmsg,err) {
			   console.log("error")
		   }
       });
   },60000);
   var separat;
   
    $('.categories').click(function() {
	    $('#productes').empty();
        var cat = $(this).attr('value'); 
        
    	var n = $('#nouProducte').attr('href').lastIndexOf("/");
    	var abans = $('#nouProducte').attr('href').substring('0',n+1);
    	var urlNova = abans+cat;
    	console.log(urlNova);
    	$("#nouProducte").attr('href', urlNova);
    	
        $.ajax({
        	url : "/productes/llistarProductes",
        	type : "GET",
        	dataType: "json",
        	data : {
        		categoria : cat,
        	},
        	success : function(productes) {
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
        		  });
        	},
        	error : function(xhr,errmsg,err) {
        		console.log
        	}
        	});
        	return false;
    }); 
}); 
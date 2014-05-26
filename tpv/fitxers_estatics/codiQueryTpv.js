$(document).ready(function() { 
	var quantitat = "";
	var producte = "";
	
	if ($('#usuari').length > 0) {
		 $.ajax({
	        	url : "/tpv/donaTaules",
	        	type : "GET",
	        	dataType: "json",
	        	success : function(taules) {
	        		  $('#tauletes').append("<select class='form-control' id='selecTaules'></select>");
	        		  $.each(taules, function() {
	        		      var id = this['pk'];
	        		      if (id != null){
	        		    	  var capacitat = this['fields']['capacitat']
	        		    	  $('#selecTaules').append("<option value=" + id + "> TAULA: " + id + " Capacitat: " + capacitat + "</option>")
	        		    	  
	        		      }
	        		      else{
	        		    	  $('#taules').find(':first-child').remove();
	        		    	  $('#taules').append("<span id='taulesIndispo'> No hi ha cap taula lliure </span>");
	        		      }
	        		  });
	        		  $('#tauletes').append("<button class='btn btn-success' id='comprovaT'> OK </button>")
	        		  $('#comprovaT').click(function(){
	        				var tauleta = $("#taules option:selected" ).text()
	        				$("#taules").empty();
	        				$("#taules").append("<span>" + tauleta + "</span>")
	        				$(".amagats").show();
	        				$("#numeros").show();
	        				carregaCategories();
	        		  });
	        	}
	      });
	  }
	
	function carregaCategories(){
		   $.ajax({
			   url : "/productes/llistarCategoriesAjax",
			   type : "GET",
			   dataType: "json",
			   success : function(categories) {
				   $.each(categories, function() {
					   var id = this['pk']
					   var nom = this['fields']['categoria']
					   var imatge =this['fields']['imatge']
					   $("#categories").append("<li class='als-item categories'><img src='/media/" + imatge + "' alt='" + nom + "'/>" + nom + "</li></a>" )
				   });
				   $("#demo1").als({
						visible_items: 5,
						scrolling_items: 3,
						orientation: "horizontal",
						circular: "no",
						autoscroll: "no"
					});

				   $('.categories').click(function() {
					    $('#productes').empty();
				        var cat = $(this).text(); 
				    
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
					        		      $('#productes').append("<div class='col-md-2 col-sm-2 producte'  id='" + id + 
					        		    		  "'><img class='img-responsive' src='" + imatge +
					        		    		  "'><p class='etiqueta'>" +
					        		    		  producte + "</p></a></div>");
					        		      }
				        		      else{
					        		      $('#productes').append("<div class='col-md-2 col-sm-2 producte'  id='" + id + 
					        		    		  "'><p class='etiqueta senseImg'>" +  producte + "</p></a></div>");
					        		   
				        		      }
				        		  });
			        		      esperaProducte();
				        	},
				        	error : function(xhr,errmsg,err) {				        	
				        		console.log("error")
				        	}
				        	});
				        	return false;
				    }); 
			   },
			   error : function(xhr,errmsg,err) {
				   console.log("error")
			   }
	       });
	}
	
	$(".num").click(function(){
		   q = $(this).text();
		   quantitat += q;
	});
	
	function esperaProducte(){
		$(".producte").click(function(){
			var idProducte = $(this).attr("id");
			producte = $(this).text();
			var opcionetes = carregaOpcions(idProducte);
			//Si es surt del modal sense donar als botons, fent això aqui m'asseguro de que no es faci servir el que s'hagi entrat abans
			$("#contenido-interno").empty();
		});
	}
	
	function carregaOpcions(idProducte){
		$.ajax({
        	url : "/productes/dadesProducte/" + idProducte,
        	type : "GET",
        	dataType: "json",

        	success : function(opcions) {
        		  var opcionetes = new Array();
        		  for(var i=0; i<opcions.length; i++){
        			  opcionetes.push(opcions[i]['opcio']);
        		  }
        		  modal(opcionetes);
        	},
        	error : function(xhr,errmsg,err) {				        	
        		console.log("error")
        	}
        	});
	}
	
	
		function modal(opcionetes) {
			$("#myModal").modal('show');
			if(quantitat == "")  quantitat = 1;
			
			$("#contenido-interno").append("<form class='form-horizontal' id='formulari'></form>")
			$("#formulari").append("<label>Quantitat</label><input id='qtat' type='number' class='form-control'></input>");
			$("#qtat").val(quantitat);
			
			if(opcionetes.length > 0){
				$("#formulari").append("<label> Opcio </label><select class='form-control' id='opcionetes'></select>")
				for(var i=0; i<opcionetes.length; i++){
					$("#opcionetes").append("<option value=" + opcionetes[i]+ ">" + opcionetes[i] + "</option>")
				}
			}
			$("#formulari").append("<label> Comentari </label> <textarea class='form-control' id='comentari'>")
		
			$("#cancela").click(function(){
				netejaModal();
			});
			
			$("#guarda").click(function(){
				//Recuperar les dades
				//Es tornà a recuperar la quantitat per si s'ha editat en el formulari del modal.
				quantitat = $("#qtat").val();
				var opcio = $("#opcionetes option:selected" ).text()
				var comentari = $("#comentari").val()
				console.log("producte " + producte + " qtat " + quantitat + " opcio " + opcio + " comentari " + comentari)
				//Enviar les dades al servidor
				//Afegir una linia al div resum
				netejaModal();
			});
		}
		
		function netejaModal(){
			quantitat = "";
			producte = "";
			$("#contenido-interno").empty();
			$("#myModal").hide();
		}
});
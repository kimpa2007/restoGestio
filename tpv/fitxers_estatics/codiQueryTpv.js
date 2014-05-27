$(document).ready(function() { 
	var quantitat = "";
	var producte = "";
	var comandeta;
	var moments = new Array();
	var linia = 0;
	
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
	        				var idTaula = $("#taules option:selected" ).attr('value');
	        				var tauleta = $("#taules option:selected" ).text()
	        				
	        				$("#taules").empty();
	        				$("#taules").append("<span>" + tauleta + "</span>")
	        				
	        				comandeta = new Comanda();
	        				var idTaula = $("#taules option:selected");
	        				comandeta.setTaula(idTaula)
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
					   $("#categories").append("<div class='categories'><img src='/media/" + imatge + "' alt='" + nom + "'/>" + nom + "</div>" )
				   });
				   $("#demo1").als({
						visible_items: 4,
						scrolling_items: 2,
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
					        		      $('#productes').append("<div class='col-md-2 producte'  id='" + id + 
					        		    		  "'><img class='img-responsive' src='" + imatge +
					        		    		  "'><p class='etiqueta'>" +
					        		    		  producte + "</p></a></div>");
					        		      }
				        		      else{
					        		      $('#productes').append("<div class='col-md-2 producte'  id='" + id + 
					        		    		  "'><p class='etiqueta senseImg'>" +  producte + "</p></a></div>");
					        		   
				        		      }
				        		  });
				      			  carregaMoment();
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
	
	function carregaMoment(){
		moments = new Array();
		$.ajax({
        	url : "/comandes/momentApat/",
        	type : "GET",
        	dataType: "json",

        	success : function(e) {
        		$.each(e, function(){
        			var moment = this['moment']['descripcio']
        			moments.push(moment)
        		}); 
        	},
        	error : function(xhr,errmsg,err) {				        	
        		console.log("error")
        	}
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
        			  if (opcions[i]['opcio'] != null)    			  opcionetes.push(opcions[i]['opcio']);
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
			if(moments.length > 0){
				$("#formulari").append("<label> Moment Apat </label><select class='form-control' id='momentet'></select>")
				for(var i=0; i<moments.length; i++){
					$("#momentet").append("<option value=" + moments[i]+ ">" + moments[i] + "</option>")
				}
			}
			$("#formulari").append("<label> Comentari </label> <textarea class='form-control' id='comentari'>")
		
			$("#cancela").click(function(){
				netejaModal();
			});
			
			$("#guarda").click(function(){
				//Recuperar les dades
				//Es tornà a recuperar la quantitat per si s'ha editat en el formulari del modal.
				$("#resum").show()
				quantitat = $("#qtat").val();
				var opcio = $("#opcionetes option:selected" ).text()
				var comentari = $("#comentari").val()
				var momentapat = $("#momentet option:selected").text()
				//Crear un nou objecte
				
				if( quantitat != null && producte !=null && momentapat != null){
					var liniaNova = new LiniaComanda();
					liniaNova.setProducte(producte);
					liniaNova.setQuantitat(quantitat);
					liniaNova.setComentari(comentari);
					liniaNova.setMomentApat(momentapat);
					liniaNova.setOpcio(opcio)
					comandeta.setLinies(liniaNova);
					console.log(comandeta.getLinies())
					
					//Afegir una linia al div resum
					//S'ha de fer la merda aquella de que es pugui editar.....
					console.log(momentapat)
					var taula = "";
					
					switch(momentapat){
						case "Aperitiu":
							taula = "aperitius";
						break;
						case "Entrant":
							taula = "primers";
						break;
						case "Segon":
							taula = "segons";
						break;
						case "Postre":
							taula = "postres";
						break;
						case "Per emportar":
							taula="xemportar";
						break;
					}
					
					$("#" + taula).show();
					$("#" + taula  + "> tbody").append("<tr id='t" + taula + linia + "'>" );
					$("#t" + taula + linia).append("<td><button class='btn btn-info' value='mes'>+</button><button class='btn btn-danger' value='menys'>-</button></td>")
					if(opcio != ""){
						$("#t" + taula + linia).append("<td>" + quantitat + "</td><td>" + producte + " amb " + opcio + " " + "</td><td>" + comentari + "</td>");
					}
					else{
						$("#t" + taula + linia).append("<td>" + quantitat + "</td><td>" + producte + "</td><td>" + comentari + "</td>");
					}
					
					linia++;
				}
				
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
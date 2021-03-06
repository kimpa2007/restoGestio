$(document).ready(function() { 
	var quantitat = "";
	var producte = "";
	var comandeta;
	var moments = new Array();
	var linia = 0;
	var defaultMomentet = "QuanSigui";
	var cat;
	
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
	   },3000);
	
	$("#novaComanda").click(function(){
		$("#tauletes").empty();
		if ($('#usuari').length > 0) {
			carregaMoment();
			 $.ajax({
		        	url : "/comandes/donaTaules",
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
		        					        				comandeta = new Comanda();
		        				var idTaula = $("#taules option:selected");
		        				comandeta.setTaula(idTaula.attr("value"))
		        				
		        				$("#taules").empty();
		        				$("#taules").append("<span>" + tauleta + "</span>")
		        				
		        				carregaCategories();
		        		  });
		        	}
		      });
		  }
		
		
	});
	$("#editaComanda").click(function(){
		$("#tauletes").empty();
		$("#passaComanda").remove();
		$("#anulaComanda").remove();
		$("#resum").append("<button class='btn btn-success' id='editaC'>Edita comanda </button>");
		carregaMoment();
		$.ajax({
        	url : "/comandes/taulesOccupades",
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
        		    	  $('#taules').append("<span id='taulesIndispo'> No hi ha cap taula ocupada </span>");
        		      }
        		  });
        		  $('#tauletes').append("<button class='btn btn-success' id='comprovaT'> OK </button>");
        		  $('#comprovaT').click(function(){
	      				var idTaula = $("#taules option:selected" ).attr('value');
	    				var tauleta = $("#taules option:selected" ).text()
	    				carregaIdComanda(idTaula);
	    				comandeta = new Comanda();
	    				var idTaula = $("#taules option:selected");
	    				comandeta.setTaula(idTaula.attr("value"))
	    				
	    				$("#taules").empty();
	    				$("#taules").append("<span>" + tauleta + "</span>")
	    				
	    				carregaCategories();
	    
        		  });
        	}
		});
		$("#editaC").click(function(){
			var c = JSON.stringify(comandeta)
			$.ajax({
				url: "/comandes/editaComanda",
		        contentType: "application/json",
				type: "GET",
				data: {
					'comandeta': c 
				},

		        success: function (response) {
		           alert("Comanda editada");
		           location.reload(true);
		        },
		        error: function (xhr, errmsg, err) {
		        	alert(xhr.status + " " + xhr.responseText);
		        }
			});
		});
	});
	
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
					   $("#categories").append("<span class='categories'><img src='/media/" + imatge + "' alt='" + nom + "'/><p id='etiqueta'>" + nom + "</p></span>" )
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
				        cat = $(this).text(); 
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
				        		    	  $('#productes').append("<div class='producte'  id='" + id + 
					        		    		  "'><img class='img-responsive' src='" + imatge +
					        		    		  "'><p>" +
					        		    		  producte + "</p></a></div>");
					        		      }
				        		      else{
					        		      $('#productes').append("<div class='producte'  id='" + id + 
					        		    		  "'><p>" +  producte + "</p></a></div>");

				        		      }
				        		  });
				 
				      			 // carregaMoment();
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
     		//Un cop carregat els moments creo les taules que faran falta
     		for(var i=0; i<moments.length; i++){
     			var id = moments[i].replace(" ","").toLowerCase();
     			var taula = $("<table class='table table-striped table-condensed' id='" + id + "'>");
     			var caption = $("<caption>" + moments[i] + "</caption><tbody></tbody>");
     			taula.append(caption)
     			$("#resum").append(taula)

     		}
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
				defaultMoment();
				$('#momentet option[value="' + defaultMomentet + '"]').prop('selected',true);
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
				
					if( quantitat > 0 && producte !=null && momentapat != null){
						//Comprovar si ja existeix un objecte amb aquest producte, opcio i moment apat.
						var existeix = false;
						var posicio;
						for(var i=0; i<comandeta.getLinies().length; i++){
							var p = comandeta.getLinia(i).getProducte();
							var o = comandeta.getLinia(i).getOpcio();
							var m = comandeta.getLinia(i).getMoment();
							var c = comandeta.getLinia(i).getComentari();
							if(p==producte && m==momentapat && o==opcio && c==comentari){
								existeix = true;
								//localitzar la linia (es veu que es correspon amb la posició que occupa a l'array de linies).
								posicio = i;
								break;
							}
						}
						
						if(existeix){
							//afegir un a quantitat	
							var quantitatActual = $("#t" + posicio).children()[1].innerHTML;
							var novaQuantitat = parseInt(quantitatActual) + 1;
							$("#t" + posicio).children()[1].innerHTML = novaQuantitat
							comandeta.getLinia(posicio).setQuantitat(novaQuantitat);
	
						}
						else {
							var liniaNova = new LiniaComanda();
							liniaNova.setProducte(producte);
							liniaNova.setQuantitat(quantitat);
							liniaNova.setComentari(comentari);
							liniaNova.setMomentApat(momentapat);
							liniaNova.setOpcio(opcio)
							comandeta.setLinies(liniaNova);
							
							if (momentapat == "Per emportar") 	taula="peremportar";
							else								var taula = momentapat.toLowerCase();
		
							
							$("#" + taula).show();
							var butoMes = $("<button class='btn btn-info mes'>+</button>");
							var butoMenys = $("<button class='btn btn-danger menys'>-</button>");
							var tdxavi = $('<td></td>');
							tdxavi.append(butoMes);
							tdxavi.append(butoMenys);
							
							$("#" + taula  + "> tbody").append("<tr id='t" + linia + "'>" );
							$("#t" + linia).append(tdxavi);
							if(opcio != ""){
								$("#t" + linia).append("<td>" + quantitat + "</td><td>" + producte + " amb " + opcio + " " + "</td><td>" + comentari + "</td>");
							}
							else{
								$("#t" + linia).append("<td>" + quantitat + "</td><td>" + producte + "</td><td>" + comentari + "</td>");
							}
							linia++;
							
							$(butoMes).click(function (){
								var quantitatActual = $(this).parents("tr").children()[1].innerHTML;
								var novaQuantitat = (parseInt(quantitatActual) + 1);
								$(this).parents("tr").children()[1].innerHTML = novaQuantitat
								var posicio = $(this).parents("tr").attr("id").substring(1);
								comandeta.getLinia(posicio).setQuantitat(novaQuantitat);
							});
							
							$(butoMenys).click(function (){
								var quantitatActual = $(this).parents("tr").children()[1].innerHTML;
								var posicio = $(this).parents("tr").attr("id").substring(1);
	
								if(quantitatActual == 1){
									var tfill = $(this).parents("tr").parents("tbody").children().length;
									if(tfill == 1){
										$(this).parents("tr").parents("tbody").parents("table").css("display","none");
										
									}
									$(this).parents("tr").remove();
									comandeta.esborraLinia(posicio);
									linia--;
	
									//Si comanda queda sense objecte, amagar resum
									var a = comandeta.getLinies().length;
									if(a < 1){
										$("#resum").hide();
									}
								}
								else{
									var novaQuantitat = parseInt(quantitatActual) - 1;
									$(this).parents("tr").children()[1].innerHTML = novaQuantitat
									comandeta.getLinia(posicio).setQuantitat(novaQuantitat);
								}
							})
						}
					}
				netejaModal();
			});
		}
		
		function netejaModal(){
			cat = "";
			quantitat = "";
			producte = "";
			$("#contenido-interno").empty();
			$("#myModal").hide();
		}
		
		$("#anulaComanda").click(function(){
			location.reload(true);
		});
		
		$("#passaComanda").click(function(){
			if(comandeta.getLinies().length < 1){
				alert("Comanda invàlida");
			}
			else{
				var c = JSON.stringify(comandeta)
				
				$.ajax({
					url: "/comandes/passaComanda",
			        contentType: "application/json",
					type: "GET",
					data: {
						'comandeta': c 
					},
	
			        success: function (response) {
			           alert("Comanda afegida");
			           location.reload(true);
			        },
			        error: function (xhr, errmsg, err) {
			        	alert(xhr.status + " " + xhr.responseText);
			        }
				});
			}
		});
		
		function carregaIdComanda(taula){
			$.ajax({
				url: "/comandes/recuperaIdComanda/" + taula,
		        contentType: "application/json",
				type: "GET",
				
		        success: function (response) {
		        	idComanda = response['idComanda'];
		        	if (idComanda != 'error'){
		        		comandeta.setId(idComanda);
	    				carregaLinies(idComanda);
		        	}
		        	else{
		        		alert("Error")
		        	}
		        },
		        error: function (xhr, errmsg, err) {
		        	alert(xhr.status + " " + xhr.responseText);
		        }
			});
		}
		
		function carregaLinies(comanda){
			$.ajax({
				url: "/comandes/recuperarLinies/" + comanda,
		        contentType: "application/json",
				type: "GET",
				
		        success: function (li) {
		        	$("#resum").show();
		        	$.each(li, function() {
		        		var producte = this['producte'];
		        		var opcio = this['opcio'];
		        		var qtat = this['total'];
		        		var moment = this['momentApat'];
		        		var comentari = this['comentari'];
		        		var id = this['id'];
		        		
		        		var liniaNova = new LiniaComanda();
		        		liniaNova.setIdLinia(id);
						liniaNova.setProducte(producte);
						liniaNova.setQuantitat(qtat);
						liniaNova.setComentari(comentari);
						liniaNova.setMomentApat(moment);
						liniaNova.setOpcio(opcio)
						comandeta.setLinies(liniaNova);
		        		
						if (moment == "Per emportar") 	tauleta ="peremportar";
						else								var tauleta = moment.toLowerCase();
						
						$("#" + tauleta).show();
						var butoMes = $("<button class='btn btn-info mes'>+</button>");
						var butoMenys = $("<button class='btn btn-danger menys'>-</button>");

						var tdxavi = $('<td></td>');
						tdxavi.append(butoMes);
						tdxavi.append(butoMenys);
						if(comentari ==  null) comentari = " "
						$("#" + tauleta  + "> tbody").append("<tr id='t" + linia + "'>" );
						$("#t" + linia).append(tdxavi);
						
						if(opcio != ""){
							$("#t" + linia).append("<td>" + parseInt(qtat) + "</td><td>" + producte + " amb " + opcio + " " + "</td><td>" + comentari + "</td>");
						}
						else{
							$("#t" + linia).append("<td>" + parseInt(qtat) + "</td><td>" + producte + "</td><td>" + comentari + "</td>");
						}
						linia++;
						
						$(butoMes).click(function (){
							var quantitatActual = $(this).parents("tr").children()[1].innerHTML;
							var novaQuantitat = (parseInt(quantitatActual) + 1);
							$(this).parents("tr").children()[1].innerHTML = novaQuantitat
							var posicio = $(this).parents("tr").attr("id").substring(1);
							comandeta.getLinia(posicio).setQuantitat(novaQuantitat);
						});
						
						$(butoMenys).click(function (){
							var quantitatActual = $(this).parents("tr").children()[1].innerHTML;
							var posicio = $(this).parents("tr").attr("id").substring(1);

							if(quantitatActual == 1){
								var tfill = $(this).parents("tr").parents("tbody").children().length;
								if(tfill == 1){
									$(this).parents("tr").parents("tbody").parents("table").css("display","none");
									
								}
								$(this).parents("tr").remove();
								comandeta.esborraLinia(posicio);
								linia--;

								//Si comanda queda sense objecte, amagar resum
								var a = comandeta.getLinies().length;
								if(a < 1){
									$("#resum").hide();
								}
							}
							else{
								var novaQuantitat = parseInt(quantitatActual) - 1;
								$(this).parents("tr").children()[1].innerHTML = novaQuantitat
								comandeta.getLinia(posicio).setQuantitat(novaQuantitat);
							}
						})
		        	});
		        },
		        error: function (xhr, errmsg, err) {
		        	alert(xhr.status + " " + xhr.responseText);
		        }
			});
		}
		
		function defaultMoment(){

			switch(cat){
				case "Aperitiu":
					defaultMomentet = "Primer";
				break;
				
				case "Entrants":
					defaultMomentet = "Primer";
				break;
				
				case "Carns":
					defaultMomentet = "Segon";
				break;
				
				case "Postres":
					defaultMomentet = "Postre";
				break;
				
				case "Cafés":
					defaultMomentet = "Café"
				break;
				 
				default:
					defaultMomentet = "QuanSigui";
				break;				
			}
		}
});
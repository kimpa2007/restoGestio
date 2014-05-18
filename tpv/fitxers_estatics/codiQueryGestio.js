$(document).ready(function() { 
    $('.categories').click(function() {
	    $('#productes').empty();
        var cat = $(this).attr('value'); 
        console.log(cat) 
        $.ajax({
        	url : "/gestio/llistarProductes",
        	type : "GET",
        	dataType: "json",
        	data : {
        		categoria : cat,
        	},
        	success : function(productes) {
        		//$('#result').append( 'Server Response: ' + json.server_response);
        		//  var obj = $.parseJSON(json);
        		  $.each(productes, function() {
        		      var id = this['pk'];
        		      var producte = this['fields']['producte'];
        		      var imatge = this['fields']['imatge'];

        		      $('#productes').append("<div  class='col-sm-2'  id='" + id + "'><img src='" + imatge + "'>" +
        		    		  producte + "</div>");

        		  });
        	},
        	error : function(xhr,errmsg,err) {
        		alert(xhr.status + ": " + xhr.responseText);
        	}
        	});
        	return false;
    }); 
}); 
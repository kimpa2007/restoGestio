function Comanda(){
	this.taula;
	this.idC;
	this.linies = new Array();
	
	this.getTaula=function(){
		return this.taula;
	}
	this.setTaula=function(taula){
		this.taula=taula;
	}
	this.setLinies = function (linia){
		this.linies.push(linia);
	}
	this.getLinies = function(){
		return this.linies;
	}
	this.getLinia = function(posicio){
		return this.linies[posicio];
	}
	this.esborraLinia = function(posicio){
		this.linies.splice(posicio,1);
	}
	this.setId = function(idC){
		this.idC = idC;
	}
	this.getId = function(){
		return this.idC;
	}
}

function LiniaComanda(){
	this.producte;
	this.quantitat;
	this.comentari;
	this.momentApat;
	this.opcio;
	this.idLinia;
	
	this.setIdLinia = function(idLinia){
		this.idLinia = idLinia;
	}
	
	this.getLinia = function(){
		return idLinia;
	}
	
	this.getProducte = function(){
		return this.producte;
	}
	
	this.setProducte = function(producte){
		this.producte = producte;
	}
	
	this.getQuantitat = function(){
		return this.quantitat;
	}
	
	this.setQuantitat = function(quantitat){
		this.quantitat = quantitat;
	}
	
	this.getComentari = function(){
		return this.comentari;
	}
	
	this.setComentari = function(comentari){
		this.comentari = comentari;
	}
	
	this.setMomentApat = function(moment){
		this.momentApat = moment;
	}
	
	this.getMoment = function(){
		return this.momentApat;
	}
	
	this.getOpcio = function(){
		return this.opcio;
	}
	this.setOpcio = function(opcio){
		this.opcio = opcio;
	}
}
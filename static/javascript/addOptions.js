document.getElementById('platform').onchange = function() {
	if(document.getElementById('platform').value == 'facebook'){
  
  	mycontainer = document.getElementById('container');
    while (mycontainer.firstChild) {
    mycontainer.removeChild(mycontainer.lastChild);
  	}
   
  	var label1 = document.createElement('label');
  	label1.htmlFor = 'facebook';
    label1.id = 'label1'
  	label1.appendChild(document.createTextNode('Please make sure you are logged in to facebook using brower/app'));
   	container.appendChild(label1);
  	container.appendChild(br);
    
  }
	else if(document.getElementById('platform').value == "twitter"){
  	
    mycontainer = document.getElementById('container');
    while (mycontainer.firstChild) {
    mycontainer.removeChild(mycontainer.lastChild);
  	}
     
     if(document.getElementById('verified')){
    	container.removeChild(verified);
 		  container.removeChild(unverified);
      container.removeChild(label2);
 		  container.removeChild(label3);
      
    }
  
    var checkbox1 = document.createElement('input');
    checkbox1.type = 'checkbox';
    checkbox1.id = 'verified';
    checkbox1.name = 'verified';
    checkbox1.value = 'verified';
    
    var label2 = document.createElement('label')
    label2.htmlFor = 'verified';
    label2.appendChild(document.createTextNode('Verified'));
    
    var checkbox2 = document.createElement('input');
    checkbox2.type = 'checkbox';
    checkbox2.id = 'unverified';
    
    checkbox2.name = 'unverified';
    checkbox2.value = 'unverified';
    
    var label3 = document.createElement('label')
    label3.htmlFor = 'unverified';
    label3.appendChild(document.createTextNode('Unverified'));
    
    container.appendChild(checkbox2);
    container.appendChild(label3);
    container.append(br);
    container.appendChild(checkbox1);
  	container.appendChild(label2);
       
  }
 else if(document.getElementById('platform').value == "instagram"){
 
   	mycontainer = document.getElementById('container');
    while (mycontainer.firstChild) {
    mycontainer.removeChild(mycontainer.lastChild);
  	}
  
    var label4 = document.createElement('label');
    label4.htmlFor = 'instagram';
    label4.appendChild(document.createTextNode('We will generate a few hashtags based on your selected resources'));
    
    container.appendChild(label4);
    container.appendChild(br);
  }
}
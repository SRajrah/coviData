document.getElementById('platform').onchange = function() {
    var br = document.createElement('br');
    mycontainer = document.getElementById('container');
	if(document.getElementById('platform').value == 'facebook'){


    while (mycontainer.firstChild) {
    mycontainer.removeChild(mycontainer.lastChild);
  	}

  	var label1 = document.createElement('label');
  	label1.htmlFor = 'facebook';
    label1.id = 'label1'
  	label1.appendChild(document.createTextNode('Please make sure you are logged in to facebook using brower/app'));
   	mycontainer.appendChild(label1);
  	mycontainer.appendChild(br);

  }
	else if(document.getElementById('platform').value == "twitter"){


    while (mycontainer.firstChild) {
        mycontainer.removeChild(mycontainer.lastChild);
  	}

//     if(document.getElementById('verified')){
//    	container.removeChild(verified);
// 		  container.removeChild(unverified);
//      container.removeChild(label2);
// 		  container.removeChild(label3);
//
//    }

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

    mycontainer.appendChild(checkbox1);
    mycontainer.appendChild(label2);
    mycontainer.appendChild(checkbox2);
  	mycontainer.appendChild(label3);

    }
    else if(document.getElementById('platform').value == "instagram"){


        while (mycontainer.firstChild) {
        mycontainer.removeChild(mycontainer.lastChild);
        }

        var label4 = document.createElement('label');
        label4.htmlFor = 'instagram';
        label4.id = "instaLine"
        label4.appendChild(document.createTextNode('We will generate a few hashtags based on your selected resources'));
        mycontainer.appendChild(label4);
        mycontainer.appendChild(br);

        //======================================================================BED HASH======================================================
            if (document.getElementById('bedBox').checked == true){

                var bedHash = "#" + document.getElementById('cityName').value + document.getElementById('bedBox').value;
                var labelBed = document.createElement('a');
                labelBed.id = "bedLabelId"
                labelBed.htmlFor = 'instagram';
                labelBed.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('bedBox').value
                labelBed.appendChild(document.createTextNode(bedHash));
                mycontainer.appendChild(labelBed);
                mycontainer.appendChild(br);

            }
    
            document.getElementById('bedBox').onchange = function() {
                if(document.getElementById('platform').value == 'instagram'){

                    if(document.getElementById('bedBox').checked == false){
                           mycontainer.removeChild(document.getElementById('bedLabelId'));
                    }
                    else{
                        var bedHash = "#" + document.getElementById('cityName').value + document.getElementById('bedBox').value;
                        var labelBed = document.createElement('a');
                        labelBed.id = "bedLabelId"
                        labelBed.htmlFor = 'instagram';
                        labelBed.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('bedBox').value
                        labelBed.appendChild(document.createTextNode(bedHash));
                        mycontainer.appendChild(labelBed);
                        mycontainer.appendChild(br);

                    }
                }

    }
    //=======================================ICU HASH==========================================================================================
           if (document.getElementById('icuBox').checked == true){

               var icuHash = "#" + document.getElementById('cityName').value + document.getElementById('icuBox').value;
               var labelIcu = document.createElement('a');
               labelIcu.id = "icuLabelId"
               labelIcu.htmlFor = 'instagram';
               labelIcu.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('icuBox').value
               labelIcu.appendChild(document.createTextNode(icuHash));
               mycontainer.appendChild(labelIcu);
               mycontainer.appendChild(br);

           }

          document.getElementById('icuBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('icuBox').checked == false){
                       mycontainer.removeChild(document.getElementById('icuLabelId'));
                }
                else{
                    var icuHash = "#" + document.getElementById('cityName').value + document.getElementById('icuBox').value;
                    var labelIcu = document.createElement('a');
                    labelIcu.id = "icuLabelId"
                    labelIcu.htmlFor = 'instagram';
                    labelIcu.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('icuBox').value
                    labelIcu.appendChild(document.createTextNode(icuHash));
                    mycontainer.appendChild(labelIcu);
                    mycontainer.appendChild(br);

                }

            }



          }
  }
}
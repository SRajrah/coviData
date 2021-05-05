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
    console.log("Here twitter")

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

        document.getElementById('submitButton').disabled = true;
        if (document.getElementById('cityName').value == ''){
            alert("Please add city name.");
            location.reload();
        }

        var label4 = document.createElement('label');
        label4.htmlFor = 'instagram';
        label4.id = "instaLine"
        label4.appendChild(document.createTextNode('We will generate a few hashtags based on your selected resources'));
        mycontainer.appendChild(label4);
        mycontainer.appendChild(br);

        //======================================================================BED HASH==========================
            if (document.getElementById('bedBox').checked == true){

                var bedHash = "#" + document.getElementById('cityName').value + document.getElementById('bedBox').value;
                var labelBed = document.createElement('a');
                labelBed.id = "bedLabelId"
                labelBed.htmlFor = 'instagram';
                labelBed.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('bedBox').value
                labelBed.target = "_blank";
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
                        var br = document.createElement('br');
                        var bedHash = "#" + document.getElementById('cityName').value + "covid" + document.getElementById('bedBox').value;
                        var labelBed = document.createElement('a');
                        labelBed.id = "bedLabelId"
                        labelBed.htmlFor = 'instagram';
                        labelBed.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('bedBox').value
                        labelBed.target = "_blank";
                        labelBed.appendChild(document.createTextNode(bedHash));
                        mycontainer.appendChild(labelBed);
                        mycontainer.appendChild(br);

                    }
                }
    }
    //=======================================ICU HASH==================================================================
           if (document.getElementById('icuBox').checked == true){

               var icuHash = "#" + document.getElementById('cityName').value + document.getElementById('icuBox').value;
               var labelIcu = document.createElement('a');
               labelIcu.id = "icuLabelId"
               labelIcu.htmlFor = 'instagram';
               labelIcu.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('icuBox').value
               labelIcu.target = "_blank";
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
                    labelIcu.target = "_blank";
                    labelIcu.appendChild(document.createTextNode(icuHash));
                    mycontainer.appendChild(labelIcu);
                    mycontainer.appendChild(br);

                }

            }

          }

//  ====================================================================================================================
            if (document.getElementById('oxygenBox').checked == true){
               var oxygenHash = "#" + document.getElementById('cityName').value + document.getElementById('oxygenBox').value;
               var labelOxygen = document.createElement('a');
               labelOxygen.id = "oxygenLabelId"
               labelOxygen.htmlFor = 'instagram';
               labelOxygen.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('oxygenBox').value
               labelOxygen.target = "_blank";
               labelOxygen.appendChild(document.createTextNode(oxygenHash));
               mycontainer.appendChild(labelOxygen);
               mycontainer.appendChild(br);

           }

          document.getElementById('oxygenBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('oxygenBox').checked == false){
                       mycontainer.removeChild(document.getElementById('oxygenLabelId'));
                }
                else{
                    var oxygenHash = "#" + document.getElementById('cityName').value + document.getElementById('oxygenBox').value;
                    var labelOxygen = document.createElement('a');
                    labelOxygen.id = "oxygenLabelId"
                    labelOxygen.htmlFor = 'instagram';
                    labelOxygen.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('oxygenBox').value
                    labelOxygen.target = "_blank";
                    labelOxygen.appendChild(document.createTextNode(oxygenHash));
                    mycontainer.appendChild(labelOxygen);
                    mycontainer.appendChild(br);

                }

            }
          }
//  =================================================================================================================
            if (document.getElementById('ventilatorBox').checked == true){

               var ventilatorHash = "#" + document.getElementById('cityName').value + document.getElementById('ventilatorBox').value;
               var labelVentilator = document.createElement('a');
               labelVentilator.id = "ventilatorLabelId"
               labelVentilator.htmlFor = 'instagram';
               labelVentilator.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('ventilatorBox').value
               labelVentilator.target = "_blank";
               labelVentilator.appendChild(document.createTextNode(ventilatorHash));
               mycontainer.appendChild(labelVentilator);
               mycontainer.appendChild(br);

           }

          document.getElementById('ventilatorBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('ventilatorBox').checked == false){
                       mycontainer.removeChild(document.getElementById('ventilatorLabelId'));
                }
                else{
                    var ventilatorHash = "#" + document.getElementById('cityName').value + document.getElementById('ventilatorBox').value;
                    var labelVentilator = document.createElement('a');
                    labelVentilator.id = "ventilatorLabelId"
                    labelVentilator.htmlFor = 'instagram';
                    labelVentilator.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('ventilatorBox').value
                    labelVentilator.target = "_blank";
                    labelVentilator.appendChild(document.createTextNode(ventilatorHash));
                    mycontainer.appendChild(labelVentilator);
                    mycontainer.appendChild(br);

                }

            }
           }
//  ===========================================================================================================
             if (document.getElementById('testBox').checked == true){

               var testHash = "#" + document.getElementById('cityName').value + document.getElementById('testBox').value;
               var labelTest = document.createElement('a');
               labelTest.id = "testLabelId"
               labelTest.htmlFor = 'instagram';
               labelTest.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('testBox').value
               labelTest.target = "_blank";
               labelTest.appendChild(document.createTextNode(testHash));
               mycontainer.appendChild(labelTest);
               mycontainer.appendChild(br);

           }

          document.getElementById('testBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('testBox').checked == false){
                       mycontainer.removeChild(document.getElementById('testLabelId'));
                }
                else{
                    var testHash = "#" + document.getElementById('cityName').value + document.getElementById('testBox').value;
                    var labelTest = document.createElement('a');
                    labelTest.id = "testLabelId"
                    labelTest.htmlFor = 'instagram';
                    labelTest.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('testBox').value
                    labelTest.target = "_blank";
                    labelTest.appendChild(document.createTextNode(testHash));
                    mycontainer.appendChild(labelTest);
                    mycontainer.appendChild(br);

                }

            }

          }
//   ============================================================================
            if (document.getElementById('fabifluBox').checked == true){

               var fabifluHash = "#" + document.getElementById('cityName').value + document.getElementById('fabifluBox').value;
               var fabifluHash = document.createElement('a');
               labelFabiflu.id = "fabifluId"
               labelFabiflu.htmlFor = 'instagram';
               labelFabiflu.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('fabifluBox').value
               labelFabiflu.target = "_blank";
               labelFabiflu.appendChild(document.createTextNode(fabifluHash));
               mycontainer.appendChild(labelFabiflu);
               mycontainer.appendChild(br);

           }

          document.getElementById('fabifluBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('fabifluBox').checked == false){
                       mycontainer.removeChild(document.getElementById('fabifluId'));
                }
                else{
                    var fabifluHash = "#" + document.getElementById('cityName').value + document.getElementById('fabifluBox').value;
                    var labelFabiflu = document.createElement('a');
                    labelFabiflu.id = "fabifluId"
                    labelFabiflu.htmlFor = 'instagram';
                    labelFabiflu.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('fabifluBox').value
                    labelFabiflu.target = "_blank";
                    labelFabiflu.appendChild(document.createTextNode(fabifluHash));
                    mycontainer.appendChild(labelFabiflu);
                    mycontainer.appendChild(br);

                }

            }

          }


//   ==============================================================================
         if (document.getElementById('remdesivirBox').checked == true){

               var remdesivirHash = "#" + document.getElementById('cityName').value + document.getElementById('remdesivirBox').value;
               var labelRemdesivir = document.createElement('a');
               labelRemdesivir.id = "remdesivirLabelId"
               labelRemdesivir.htmlFor = 'instagram';
               labelRemdesivir.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('remdesivirBox').value
               labelRemdesivir.target = "_blank";
               labelRemdesivir.appendChild(document.createTextNode(remdesivirHash));
               mycontainer.appendChild(labelRemdesivir);
               mycontainer.appendChild(br);

           }

          document.getElementById('remdesivirBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('remdesivirBox').checked == false){
                       mycontainer.removeChild(document.getElementById('remdesivirLabelId'));
                }
                else{
                    var remdesivirHash = "#" + document.getElementById('cityName').value + document.getElementById('remdesivirBox').value;
                    var labelRemdesivir = document.createElement('a');
                    labelRemdesivir.id = "remdesivirLabelId"
                    labelRemdesivir.htmlFor = 'instagram';
                    labelRemdesivir.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('remdesivirBox').value
                    labelRemdesivir.target = "_blank";
                    labelRemdesivir.appendChild(document.createTextNode(remdesivirHash));
                    mycontainer.appendChild(labelRemdesivir);
                    mycontainer.appendChild(br);

                }

            }

          }

//   ==============================================================================
              if (document.getElementById('favipiravirBox').checked == true){

               var favipiravirHash = "#" + document.getElementById('cityName').value + document.getElementById('favipiravirBox').value;
               var labelFavipiravir = document.createElement('a');
               labelFavipiravir.id = "favipiravirLabelId"
               labelFavipiravir.htmlFor = 'instagram';
               labelFavipiravir.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('favipiravirBox').value
               labelFavipiravir.target = "_blank";
               labelFavipiravir.appendChild(document.createTextNode(favipiravirHash));
               mycontainer.appendChild(labelFavipiravir);
               mycontainer.appendChild(br);

           }

          document.getElementById('favipiravirBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('favipiravirBox').checked == false){
                       mycontainer.removeChild(document.getElementById('favipiravirLabelId'));
                }
                else{
                    var favipiravirHash = "#" + document.getElementById('cityName').value + document.getElementById('favipiravirBox').value;
                    var labelFavipiravir = document.createElement('a');
                    labelFavipiravir.id = "favipiravirLabelId"
                    labelFavipiravir.htmlFor = 'instagram';
                    labelFavipiravir.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('favipiravirBox').value
                    labelFavipiravir.target = "_blank";
                    labelFavipiravir.appendChild(document.createTextNode(favipiravirHash));
                    mycontainer.appendChild(labelFavipiravir);
                    mycontainer.appendChild(br);

                }

            }

          }

//   ==============================================================================
           if (document.getElementById('tocilizumabBox').checked == true){

               var tocilizumabHash = "#" + document.getElementById('cityName').value + document.getElementById('tocilizumabBox').value;
               var labelTocilizumab = document.createElement('a');
               labelTocilizumab.id = "tocilizumabLabelId"
               labelTocilizumab.htmlFor = 'instagram';
               labelTocilizumab.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('tocilizumabBox').value
               labelTocilizumab.target = "_blank";
               labelTocilizumab.appendChild(document.createTextNode(tocilizumabHash));
               mycontainer.appendChild(labelTocilizumab);
               mycontainer.appendChild(br);

           }

          document.getElementById('tocilizumabBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('tocilizumabBox').checked == false){
                       mycontainer.removeChild(document.getElementById('tocilizumabLabelId'));
                }
                else{
                    var tocilizumabHash = "#" + document.getElementById('cityName').value + document.getElementById('tocilizumabBox').value;
                    var labelTocilizumab = document.createElement('a');
                    labelTocilizumab.id = "tocilizumabLabelId"
                    labelTocilizumab.htmlFor = 'instagram';
                    labelTocilizumab.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('tocilizumabBox').value
                    labelTocilizumab.target = "_blank";
                    labelTocilizumab.appendChild(document.createTextNode(tocilizumabHash));
                    mycontainer.appendChild(labelTocilizumab);
                    mycontainer.appendChild(br);

                }

            }

          }
//   =============================================================================
           if (document.getElementById('plasmaBox').checked == true){

               var plasmaHash = "#" + document.getElementById('cityName').value + document.getElementById('plasmaBox').value;
               var labelPlasma = document.createElement('a');
               labelPlasma.id = "plasmaLabelId"
               labelPlasma.htmlFor = 'instagram';
               labelPlasma.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('plasmaBox').value
               labelPlasma.target = "_blank";
               labelPlasma.appendChild(document.createTextNode(plasmaHash));
               mycontainer.appendChild(labelPlasma);
               mycontainer.appendChild(br);

           }

          document.getElementById('plasmaBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('plasmaBox').checked == false){
                       mycontainer.removeChild(document.getElementById('plasmaLabelId'));
                }
                else{
                    var plasmaHash = "#" + document.getElementById('cityName').value + document.getElementById('plasmaBox').value;
                    var labelPlasma = document.createElement('a');
                    labelPlasma.id = "plasmaLabelId"
                    labelPlasma.htmlFor = 'instagram';
                    labelPlasma.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('plasmaBox').value
                    labelPlasma.target = "_blank";
                    labelPlasma.appendChild(document.createTextNode(plasmaHash));
                    mycontainer.appendChild(labelPlasma);
                    mycontainer.appendChild(br);

                }

            }

          }
//  ================================================================================
             if (document.getElementById('foodBox').checked == true){

               var foodHash = "#" + document.getElementById('cityName').value + document.getElementById('foodBox').value;
               var labelFood = document.createElement('a');
               labelFood.id = "foodLabelId"
               labelFood.htmlFor = 'instagram';
               labelFood.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('foodBox').value
               labelFood.target = "_blank";
               labelFood.appendChild(document.createTextNode(foodHash));
               mycontainer.appendChild(labelFood);
               mycontainer.appendChild(br);

           }

          document.getElementById('foodBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('foodBox').checked == false){
                       mycontainer.removeChild(document.getElementById('foodLabelId'));
                }
                else{
                    var foodHash = "#" + document.getElementById('cityName').value + document.getElementById('foodBox').value;
                    var labelFood = document.createElement('a');
                    labelFood.id = "foodLabelId"
                    labelFood.htmlFor = 'instagram';
                    labelFood.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('foodBox').value
                    labelFood.target = "_blank";
                    labelFood.appendChild(document.createTextNode(foodHash));
                    mycontainer.appendChild(labelFood);
                    mycontainer.appendChild(br);

                }

            }

          }
//  ===============================================================================

              if (document.getElementById('ambulanceBox').checked == true){

               var ambulanceHash = "#" + document.getElementById('cityName').value + document.getElementById('ambulanceBox').value;
               var labelAmbulance = document.createElement('a');
               labelAmbulance.id = "ambulanceLabelId"
               labelAmbulance.htmlFor = 'instagram';
               labelAmbulance.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('ambulanceBox').value
               labelAmbulance.target = "_blank";
               labelAmbulance.appendChild(document.createTextNode(ambulanceHash));
               mycontainer.appendChild(labelAmbulance);
               mycontainer.appendChild(br);

           }

          document.getElementById('ambulanceBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('ambulanceBox').checked == false){
                       mycontainer.removeChild(document.getElementById('ambulanceLabelId'));
                }
                else{
                    var ambulanceHash = "#" + document.getElementById('cityName').value + document.getElementById('ambulanceBox').value;
                    var labelAmbulance = document.createElement('a');
                    labelAmbulance.id = "ambulanceLabelId"
                    labelAmbulance.htmlFor = 'instagram';
                    labelAmbulance.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('ambulanceBox').value
                    labelAmbulance.target = "_blank";
                    labelAmbulance.appendChild(document.createTextNode(ambulanceHash));
                    mycontainer.appendChild(labelAmbulance);
                    mycontainer.appendChild(br);

                }

            }

          }
//  ================================================================================

              if (document.getElementById('therapyBox').checked == true){

               var therapyHash = "#" + document.getElementById('cityName').value + document.getElementById('therapyBox').value;
               var labelTherapy = document.createElement('a');
               labelTherapy.id = "therapyLabelId"
               labelTherapy.htmlFor = 'instagram';
               labelTherapy.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('therapyBox').value
               labelTherapy.target = "_blank";
               labelTherapy.appendChild(document.createTextNode(therapyHash));
               mycontainer.appendChild(labelTherapy);
               mycontainer.appendChild(br);

           }

          document.getElementById('therapyBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('therapyBox').checked == false){
                       mycontainer.removeChild(document.getElementById('therapyLabelId'));
                }
                else{
                    var therapyHash = "#" + document.getElementById('cityName').value + document.getElementById('therapyBox').value;
                    var labelTherapy = document.createElement('a');
                    labelTherapy.id = "therapyLabelId"
                    labelTherapy.htmlFor = 'instagram';
                    labelTherapy.href = "https://www.instagram.com/explore/tags/" + document.getElementById('cityName').value + document.getElementById('therapyBox').value
                    labelTherapy.target = "_blank";
                    labelTherapy.appendChild(document.createTextNode(therapyHash));
                    mycontainer.appendChild(labelTherapy);
                    mycontainer.appendChild(br);

                }

            }

          }
//  ================================================================================
  }
}
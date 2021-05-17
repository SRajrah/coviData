document.getElementById('platform').onchange = function() {
    var city =document.getElementById('cityName').value;
    var newCity = city.replace(/\s+/g, '');
    document.getElementById('submitButton').disabled = false;
    var br = document.createElement('br');
    mycontainer = document.getElementById('container');

	if(document.getElementById('platform').value == 'facebook'){

    while (mycontainer.firstChild) {
    mycontainer.removeChild(mycontainer.lastChild);
  	}

  	var label1 = document.createElement('label');
  	label1.htmlFor = 'facebook';
    label1.id = 'label1'
    var label2 = document.createElement('label');
  	label2.htmlFor = 'facebook';
    label2.id = 'label2'

  	label1.appendChild(document.createTextNode('Add less resources per search for effective results.'));
   	label2.appendChild(document.createTextNode('Also make sure that you are logged in to facebook using the browser/app.'));
   	mycontainer.appendChild(label1);
   	mycontainer.append(document.createElement('br'));
   	mycontainer.appendChild(label2);
  	mycontainer.append(document.createElement('br'));

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

    var label4 = document.createElement('label');
  	label4.htmlFor = 'facebook';
    label4.id = 'label2'
//    document.querySelector(".platformOptions").innerHTML = String.fromCodePoint(0X1F4A1);
  	label4.appendChild(document.createTextNode('Please make sure to go to the latest tab in twitter.'));

    mycontainer.appendChild(label4);
    mycontainer.append(document.createElement('br'));
    mycontainer.appendChild(checkbox1);
    mycontainer.appendChild(label2);
    mycontainer.appendChild( document.createTextNode( '\u00A0 \u00A0 \u00A0' ) );
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
        label4.appendChild(document.createTextNode('We will generate a few hashtags based on your selected resources. Click the links.'));
        mycontainer.appendChild(label4);
//        mycontainer.append(document.createElement('br'));

        //======================================================================BED HASH==========================
            if (document.getElementById('bedBox').checked == true){
                var br1 = document.createElement('br');
                var bedHash = "#" + newCity + document.getElementById('bedBox').value;
                var labelBed = document.createElement('a');
                labelBed.id = "bedLabelId"
                labelBed.htmlFor = 'instagram';
                labelBed.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('bedBox').value
                labelBed.target = "_blank";
                labelBed.appendChild(document.createTextNode(bedHash));

                mycontainer.appendChild(labelBed);
                mycontainer.appendChild(br1);
                
            }

            document.getElementById('bedBox').onchange = function() {
                if(document.getElementById('platform').value == 'instagram'){

                    if(document.getElementById('bedBox').checked == false){
                           mycontainer.removeChild(document.getElementById('bedLabelId'));
                    }
                    else{
                        var br = document.createElement('br');
                        var bedHash = "#" + newCity + "covid" + document.getElementById('bedBox').value;
                        var labelBed = document.createElement('a');
                        labelBed.id = "bedLabelId"
                        labelBed.htmlFor = 'instagram';
                        labelBed.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('bedBox').value
                        labelBed.target = "_blank";
                        labelBed.appendChild(document.createTextNode(bedHash));
                        mycontainer.appendChild(labelBed);
                        mycontainer.append(document.createElement('br'));

                    }
                }
    }
    //=======================================ICU HASH==================================================================
           if (document.getElementById('icuBox').checked == true){

               var icuHash = "#" + newCity + document.getElementById('icuBox').value;
               var labelIcu = document.createElement('a');
               labelIcu.id = "icuLabelId"
               labelIcu.htmlFor = 'instagram';
               labelIcu.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('icuBox').value
               labelIcu.target = "_blank";
               labelIcu.appendChild(document.createTextNode(icuHash));
               mycontainer.appendChild(labelIcu);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('icuBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('icuBox').checked == false){
                       mycontainer.removeChild(document.getElementById('icuLabelId'));
                }
                else{
                    var icuHash = "#" + newCity + document.getElementById('icuBox').value;
                    var labelIcu = document.createElement('a');
                    labelIcu.id = "icuLabelId"
                    labelIcu.htmlFor = 'instagram';
                    labelIcu.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('icuBox').value
                    labelIcu.target = "_blank";
                    labelIcu.appendChild(document.createTextNode(icuHash));
                    mycontainer.appendChild(labelIcu);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }

//  ====================================================================================================================
            if (document.getElementById('oxygenBox').checked == true){
               var oxygenHash = "#" + newCity + document.getElementById('oxygenBox').value;
               var labelOxygen = document.createElement('a');
               labelOxygen.id = "oxygenLabelId"
               labelOxygen.htmlFor = 'instagram';
               labelOxygen.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('oxygenBox').value
               labelOxygen.target = "_blank";
               labelOxygen.appendChild(document.createTextNode(oxygenHash));
               mycontainer.appendChild(labelOxygen);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('oxygenBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('oxygenBox').checked == false){
                       mycontainer.removeChild(document.getElementById('oxygenLabelId'));
                }
                else{
                    var oxygenHash = "#" + newCity + document.getElementById('oxygenBox').value;
                    var labelOxygen = document.createElement('a');
                    labelOxygen.id = "oxygenLabelId"
                    labelOxygen.htmlFor = 'instagram';
                    labelOxygen.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('oxygenBox').value
                    labelOxygen.target = "_blank";
                    labelOxygen.appendChild(document.createTextNode(oxygenHash));
                    mycontainer.appendChild(labelOxygen);
                    mycontainer.append(document.createElement('br'));

                }

            }
          }
//  =================================================================================================================
            if (document.getElementById('ventilatorBox').checked == true){

               var ventilatorHash = "#" + newCity + document.getElementById('ventilatorBox').value;
               var labelVentilator = document.createElement('a');
               labelVentilator.id = "ventilatorLabelId"
               labelVentilator.htmlFor = 'instagram';
               labelVentilator.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('ventilatorBox').value
               labelVentilator.target = "_blank";
               labelVentilator.appendChild(document.createTextNode(ventilatorHash));
               mycontainer.appendChild(labelVentilator);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('ventilatorBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('ventilatorBox').checked == false){
                       mycontainer.removeChild(document.getElementById('ventilatorLabelId'));
                }
                else{
                    var ventilatorHash = "#" + newCity + document.getElementById('ventilatorBox').value;
                    var labelVentilator = document.createElement('a');
                    labelVentilator.id = "ventilatorLabelId"
                    labelVentilator.htmlFor = 'instagram';
                    labelVentilator.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('ventilatorBox').value
                    labelVentilator.target = "_blank";
                    labelVentilator.appendChild(document.createTextNode(ventilatorHash));
                    mycontainer.appendChild(labelVentilator);
                    mycontainer.append(document.createElement('br'));

                }

            }
           }
//  ===========================================================================================================
             if (document.getElementById('testBox').checked == true){

               var testHash = "#" + newCity + document.getElementById('testBox').value;
               var labelTest = document.createElement('a');
               labelTest.id = "testLabelId"
               labelTest.htmlFor = 'instagram';
               labelTest.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('testBox').value
               labelTest.target = "_blank";
               labelTest.appendChild(document.createTextNode(testHash));
               mycontainer.appendChild(labelTest);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('testBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('testBox').checked == false){
                       mycontainer.removeChild(document.getElementById('testLabelId'));
                }
                else{
                    var testHash = "#" + newCity + document.getElementById('testBox').value;
                    var labelTest = document.createElement('a');
                    labelTest.id = "testLabelId"
                    labelTest.htmlFor = 'instagram';
                    labelTest.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('testBox').value
                    labelTest.target = "_blank";
                    labelTest.appendChild(document.createTextNode(testHash));
                    mycontainer.appendChild(labelTest);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }
//   ============================================================================
            if (document.getElementById('fabifluBox').checked == true){

               var fabifluHash = "#" + newCity + document.getElementById('fabifluBox').value;
               var labelFabiflu = document.createElement('a');
               labelFabiflu.id = "fabifluId";
               labelFabiflu.htmlFor = 'instagram';
               labelFabiflu.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('fabifluBox').value
               labelFabiflu.target = "_blank";
               labelFabiflu.appendChild(document.createTextNode(fabifluHash));
               mycontainer.appendChild(labelFabiflu);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('fabifluBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('fabifluBox').checked == false){
                       mycontainer.removeChild(document.getElementById('fabifluId'));
                }
                else{
                    var fabifluHash = "#" + newCity + document.getElementById('fabifluBox').value;
                    var labelFabiflu = document.createElement('a');
                    labelFabiflu.id = "fabifluId"
                    labelFabiflu.htmlFor = 'instagram';
                    labelFabiflu.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('fabifluBox').value
                    labelFabiflu.target = "_blank";
                    labelFabiflu.appendChild(document.createTextNode(fabifluHash));
                    mycontainer.appendChild(labelFabiflu);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }


//   ==============================================================================
         if (document.getElementById('remdesivirBox').checked == true){

               var remdesivirHash = "#" + newCity + document.getElementById('remdesivirBox').value;
               var labelRemdesivir = document.createElement('a');
               labelRemdesivir.id = "remdesivirLabelId"
               labelRemdesivir.htmlFor = 'instagram';
               labelRemdesivir.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('remdesivirBox').value
               labelRemdesivir.target = "_blank";
               labelRemdesivir.appendChild(document.createTextNode(remdesivirHash));
               mycontainer.appendChild(labelRemdesivir);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('remdesivirBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('remdesivirBox').checked == false){
                       mycontainer.removeChild(document.getElementById('remdesivirLabelId'));
                }
                else{
                    var remdesivirHash = "#" + newCity + document.getElementById('remdesivirBox').value;
                    var labelRemdesivir = document.createElement('a');
                    labelRemdesivir.id = "remdesivirLabelId"
                    labelRemdesivir.htmlFor = 'instagram';
                    labelRemdesivir.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('remdesivirBox').value
                    labelRemdesivir.target = "_blank";
                    labelRemdesivir.appendChild(document.createTextNode(remdesivirHash));
                    mycontainer.appendChild(labelRemdesivir);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }

//   ==============================================================================
              if (document.getElementById('favipiravirBox').checked == true){

               var favipiravirHash = "#" + newCity + document.getElementById('favipiravirBox').value;
               var labelFavipiravir = document.createElement('a');
               labelFavipiravir.id = "favipiravirLabelId"
               labelFavipiravir.htmlFor = 'instagram';
               labelFavipiravir.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('favipiravirBox').value
               labelFavipiravir.target = "_blank";
               labelFavipiravir.appendChild(document.createTextNode(favipiravirHash));
               mycontainer.appendChild(labelFavipiravir);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('favipiravirBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('favipiravirBox').checked == false){
                       mycontainer.removeChild(document.getElementById('favipiravirLabelId'));
                }
                else{
                    var favipiravirHash = "#" + newCity + document.getElementById('favipiravirBox').value;
                    var labelFavipiravir = document.createElement('a');
                    labelFavipiravir.id = "favipiravirLabelId"
                    labelFavipiravir.htmlFor = 'instagram';
                    labelFavipiravir.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('favipiravirBox').value
                    labelFavipiravir.target = "_blank";
                    labelFavipiravir.appendChild(document.createTextNode(favipiravirHash));
                    mycontainer.appendChild(labelFavipiravir);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }

//   ==============================================================================
           if (document.getElementById('tocilizumabBox').checked == true){

               var tocilizumabHash = "#" + newCity + document.getElementById('tocilizumabBox').value;
               var labelTocilizumab = document.createElement('a');
               labelTocilizumab.id = "tocilizumabLabelId"
               labelTocilizumab.htmlFor = 'instagram';
               labelTocilizumab.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('tocilizumabBox').value
               labelTocilizumab.target = "_blank";
               labelTocilizumab.appendChild(document.createTextNode(tocilizumabHash));
               mycontainer.appendChild(labelTocilizumab);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('tocilizumabBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('tocilizumabBox').checked == false){
                       mycontainer.removeChild(document.getElementById('tocilizumabLabelId'));
                }
                else{
                    var tocilizumabHash = "#" + newCity + document.getElementById('tocilizumabBox').value;
                    var labelTocilizumab = document.createElement('a');
                    labelTocilizumab.id = "tocilizumabLabelId"
                    labelTocilizumab.htmlFor = 'instagram';
                    labelTocilizumab.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('tocilizumabBox').value
                    labelTocilizumab.target = "_blank";
                    labelTocilizumab.appendChild(document.createTextNode(tocilizumabHash));
                    mycontainer.appendChild(labelTocilizumab);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }
//   =============================================================================
           if (document.getElementById('plasmaBox').checked == true){

               var plasmaHash = "#" + newCity + document.getElementById('plasmaBox').value;
               var labelPlasma = document.createElement('a');
               labelPlasma.id = "plasmaLabelId"
               labelPlasma.htmlFor = 'instagram';
               labelPlasma.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('plasmaBox').value
               labelPlasma.target = "_blank";
               labelPlasma.appendChild(document.createTextNode(plasmaHash));
               mycontainer.appendChild(labelPlasma);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('plasmaBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('plasmaBox').checked == false){
                       mycontainer.removeChild(document.getElementById('plasmaLabelId'));
                }
                else{
                    var plasmaHash = "#" + newCity + document.getElementById('plasmaBox').value;
                    var labelPlasma = document.createElement('a');
                    labelPlasma.id = "plasmaLabelId"
                    labelPlasma.htmlFor = 'instagram';
                    labelPlasma.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('plasmaBox').value
                    labelPlasma.target = "_blank";
                    labelPlasma.appendChild(document.createTextNode(plasmaHash));
                    mycontainer.appendChild(labelPlasma);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }
//  ================================================================================
             if (document.getElementById('foodBox').checked == true){

               var foodHash = "#" + newCity + document.getElementById('foodBox').value;
               var labelFood = document.createElement('a');
               labelFood.id = "foodLabelId"
               labelFood.htmlFor = 'instagram';
               labelFood.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('foodBox').value
               labelFood.target = "_blank";
               labelFood.appendChild(document.createTextNode(foodHash));
               mycontainer.appendChild(labelFood);
               mycontainer.append(document.createElement('br'));

               var foodHash1 = "#" + newCity + "meals";
               var labelFood1 = document.createElement('a');
               labelFood1.id = "foodLabelId1"
               labelFood1.htmlFor = 'instagram';
               labelFood1.href = "https://www.instagram.com/explore/tags/" + newCity + "meals"
               labelFood1.target = "_blank";
               labelFood1.appendChild(document.createTextNode(foodHash1));
               mycontainer.appendChild(labelFood1);
               mycontainer.append(document.createElement('br'));

               var foodHash2 = "#" + newCity + "tiffin";
               var labelFood2 = document.createElement('a');
               labelFood2.id = "foodLabelId2"
               labelFood2.htmlFor = 'instagram';
               labelFood2.href = "https://www.instagram.com/explore/tags/" + newCity + "tiffin"
               labelFood2.target = "_blank";
               labelFood2.appendChild(document.createTextNode(foodHash2));
               mycontainer.appendChild(labelFood2);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('foodBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('foodBox').checked == false){
                       mycontainer.removeChild(document.getElementById('foodLabelId'));
                       mycontainer.removeChild(document.getElementById('foodLabelId1'));
                       mycontainer.removeChild(document.getElementById('foodLabelId2'));
                }
                else{
                    var foodHash = "#" + newCity + document.getElementById('foodBox').value;
                    var labelFood = document.createElement('a');
                    labelFood.id = "foodLabelId"
                    labelFood.htmlFor = 'instagram';
                    labelFood.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('foodBox').value
                    labelFood.target = "_blank";
                    labelFood.appendChild(document.createTextNode(foodHash));
                    mycontainer.appendChild(labelFood);
                    mycontainer.append(document.createElement('br'));

                    var foodHash1 = "#" + newCity + "meals";
                    var labelFood1 = document.createElement('a');
                    labelFood1.id = "foodLabelId1"
                    labelFood1.htmlFor = 'instagram';
                    labelFood1.href = "https://www.instagram.com/explore/tags/" + newCity + "meals"
                    labelFood1.target = "_blank";
                    labelFood1.appendChild(document.createTextNode(foodHash1));
                    mycontainer.appendChild(labelFood1);
                    mycontainer.append(document.createElement('br'));

                    var foodHash2 = "#" + newCity + "tiffin";
                    var labelFood2 = document.createElement('a');
                    labelFood2.id = "foodLabelId2"
                    labelFood2.htmlFor = 'instagram';
                    labelFood2.href = "https://www.instagram.com/explore/tags/" + newCity + "tiffin"
                    labelFood2.target = "_blank";
                    labelFood2.appendChild(document.createTextNode(foodHash2));
                    mycontainer.appendChild(labelFood2);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }
//  ===============================================================================

              if (document.getElementById('ambulanceBox').checked == true){

               var ambulanceHash = "#" + newCity + document.getElementById('ambulanceBox').value;
               var labelAmbulance = document.createElement('a');
               labelAmbulance.id = "ambulanceLabelId"
               labelAmbulance.htmlFor = 'instagram';
               labelAmbulance.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('ambulanceBox').value
               labelAmbulance.target = "_blank";
               labelAmbulance.appendChild(document.createTextNode(ambulanceHash));
               mycontainer.appendChild(labelAmbulance);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('ambulanceBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('ambulanceBox').checked == false){
                       mycontainer.removeChild(document.getElementById('ambulanceLabelId'));
                }
                else{
                    var ambulanceHash = "#" + newCity + document.getElementById('ambulanceBox').value;
                    var labelAmbulance = document.createElement('a');
                    labelAmbulance.id = "ambulanceLabelId"
                    labelAmbulance.htmlFor = 'instagram';
                    labelAmbulance.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('ambulanceBox').value
                    labelAmbulance.target = "_blank";
                    labelAmbulance.appendChild(document.createTextNode(ambulanceHash));
                    mycontainer.appendChild(labelAmbulance);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }
//  ================================================================================

              if (document.getElementById('therapyBox').checked == true){

               var therapyHash = "#" + newCity + document.getElementById('therapyBox').value;
               var labelTherapy = document.createElement('a');
               labelTherapy.id = "therapyLabelId"
               labelTherapy.htmlFor = 'instagram';
               labelTherapy.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('therapyBox').value
               labelTherapy.target = "_blank";
               labelTherapy.appendChild(document.createTextNode(therapyHash));
               mycontainer.appendChild(labelTherapy);
               mycontainer.append(document.createElement('br'));

           }

          document.getElementById('therapyBox').onchange = function() {

            if(document.getElementById('platform').value == 'instagram'){

                if(document.getElementById('therapyBox').checked == false){
                       mycontainer.removeChild(document.getElementById('therapyLabelId'));
                }
                else{
                    var therapyHash = "#" + newCity + document.getElementById('therapyBox').value;
                    var labelTherapy = document.createElement('a');
                    labelTherapy.id = "therapyLabelId"
                    labelTherapy.htmlFor = 'instagram';
                    labelTherapy.href = "https://www.instagram.com/explore/tags/" + newCity + document.getElementById('therapyBox').value
                    labelTherapy.target = "_blank";
                    labelTherapy.appendChild(document.createTextNode(therapyHash));
                    mycontainer.appendChild(labelTherapy);
                    mycontainer.append(document.createElement('br'));

                }

            }

          }


//  ================================================================================
  }
}
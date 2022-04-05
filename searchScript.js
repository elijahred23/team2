//https://elijahproctor.org/vhpadmin/api/api.php?veteranName=E

function showLoader(){
  $(".loader").show();
  $("#vetResults").hide();
}
function hideLoader(){
  $(".loader").hide();
  $("#vetResults").show();
}

var vetID = null ;


function search(searchData, res){ 
  showLoader();
  let request = {
    url: "https://elijahproctor.org/vhpadmin/api/api.php",
    dataType: "json",
    data: searchData,
    type: "GET",
        success: function() { console.log("Worked"); },
        error: function() { console.log("Fail"); }
  }
 $.ajax(request).done(res);
}

function searchByName(){   
  if($("#veteranName").val() == ""){
    return;
  }
  search({veteranName: $("#veteranName").val()}, veteranSearchResponse);
}
function searchAll(){

  search({all: "yes"}, veteranSearchResponse);
}
function vetInfo(){
  search({getVetByID: vetID}, getVetResponse);
}

const veteranSearchResponse = (res) =>{
    $("#vetResults").empty();
    let vets = res.values.vets;
    if(vets.length == 0){
      $("#vetResults").html("No results");
    }
    for(let i = 0; i < vets.length; i++){
      let vetContainer = document.createElement("div");
      let firstName = document.createElement("span");
      let lastName = document.createElement("span");
      let warName = document.createElement("p");
      let vetIDTemp = vets[i].vetID;
      $(firstName).text(vets[i].firstName);
      $(lastName).text( " " + vets[i].lastName);    
      $(vetContainer).append(firstName,lastName,warName,document.createElement("hr"));
      $("#vetResults").append(vetContainer);
      $(vetContainer).on("click", function(){
        vetID = vetIDTemp;
        vetInfo();
      });
    }    
    hideLoader();
  }

const getVetResponse = vet => {
  $("#vetResults").empty();
  let vetName = document.createElement("p");
  let vetAudio = document.createElement("audio");
  let veteran = vet.values.vet;
  
  vetAudio.src = veteran.audioLocation;
  vetAudio.controls = true;
  
  $(vetName).text(veteran.firstName + " " + veteran.lastName);
  
  $("#vetResults").append(vetName, vetAudio);
  hideLoader();
}

$("#submitVeteranName").on("click", () =>{
 searchByName();
});

$("#veteranName").on("keydown", function(event){
  if(event.keyCode == 13)
    searchByName();
});

$("#searchAllVeterans").on("click", function(){
  searchAll();
});

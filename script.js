//https://elijahproctor.org/vhpadmin/api/api.php?veteranName=E

function search(searchData){    
  if($("#veteranName").val() == ""){
    return;
  }
  let request = {
    url: "https://elijahproctor.org/vhpadmin/api/api.php",
    dataType: "json",
    data: searchData,
    type: "GET",
        success: function() { console.log("Worked"); },
        error: function() { console.log("Fail"); }
  }
  let response = (res) =>{
    console.log(res);
    $("#vetResults").html("");
    let vets = res.values.vets;
    console.log(vets[0]);
    
    if(vets.length == 0){
      $("#vetResults").html("No results");
    }
    
    for(let i = 0; i < vets.length; i++){
      let firstName = document.createElement("span");
      let lastName = document.createElement("span");
      let warName = document.createElement("p");
      $(firstName).text(vets[i].firstName);
      $(lastName).text( " " + vets[i].lastName);
      $("#vetResults").append(firstName,lastName,warName);
    }
  }
 $.ajax(request).done(response);
}

function searchByName(){
  search({veteranName: $("#veteranName").val()});
}
function searchAll(){
  console.log("Search All");
  search({all: true});
}

$("#submitVeteranName").on("click", () =>{
 searchByName();
});

$("#veteranName").on("keydown", function(event){
  if(event.keyCode == 13)
    searchByName();
});
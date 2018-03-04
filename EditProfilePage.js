var app = angular.module('mainApp',[]);

app.controller('Values', function($scope,$http){
  $http.get("10.21.233.121:5000/createProfile/apple")
  .then(function(resp){
    var personalInfo = resp;
  })
  .catch(function(err){
    console.log('FAILURE: ', err);
  })
  .finally(function(){
    console.log('DEFAULT BEHAVIOUR');
  });
});


var FName = "Insert JSON parameter";
document.getElementById("FirstName").value = personalInfo["FName"];

var LName = "Insert JSON parameter";
document.getElementById("LastName").value = personalInfo["LName"];

var Email = "Insert JSON parameter";
document.getElementById("email").value = personalInfo["Email"];

var number = "Insert JSON parameter";
document.getElementById("phoneNumber").value = number;

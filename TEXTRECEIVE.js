var app = angular.module('mainApp',[]);

app.controller('Values', function($scope,$http){
  $http.get("10.21.233.121:5000/createProfile/apple")
  .then(function(resp){
    console.log('SUCCESS: ', resp);
  })
  .catch(function(err){
    console.log('FAILURE: ', err);
  })
  .finally(function(){
    console.log('DEFAULT BEHAVIOUR');
  });
});

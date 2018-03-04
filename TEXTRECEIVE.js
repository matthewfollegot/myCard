var app = angular.module('mainApp',[]);

app.controller('Values', function($scope,$http){
  $http.get("10.21.233.121:5000/newContact/apple");
})

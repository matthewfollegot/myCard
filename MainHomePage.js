(function() {
  'use strict';

  angular.module('navBarDemoBasicUsage', ['ngMaterial'])
      .controller('AppCtrl', AppCtrl);

  function AppCtrl($scope) {
    $scope.currentNavItem = 'contactBook';

    $scope.goto = function(page) {
      console.log("Goto " + page);
    }
  }
})();

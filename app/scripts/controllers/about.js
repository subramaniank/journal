'use strict';

/**
 * @ngdoc function
 * @name journyApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the journyApp
 */
angular.module('journyApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

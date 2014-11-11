'use strict';

/**
 * @ngdoc function
 * @name journyApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the journyApp
 */
angular.module('journyApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

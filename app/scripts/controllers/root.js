'use strict';

/**
 * @ngdoc function
 * @name journyApp.controller:RootCtrl
 * @description
 * # RootCtrl
 * Controller of the journyApp
 */
angular.module('journyApp')
  .controller('RootCtrl',[ '$scope', '$modal', '$log', '$cookies', function ($scope, $modal, $log, $cookies) {

    $scope.currentUser = $cookies.jour_user;

}]);

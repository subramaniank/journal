'use strict';

/**
 * @ngdoc function
 * @name journyApp.controller:HeaderctrlCtrl
 * @description
 * # HeaderctrlCtrl
 * Controller of the journyApp
 */
angular.module('journyApp')
  .controller('HeaderCtrl', ['$scope', 'AuthService', '$modal', '$log', function ($scope, AuthService, $modal, $log) {

    $scope.showLoginForm = function() {

      var modalInstance = $modal.open({
        templateUrl: 'partials/loginModal.html',
        controller: 'LoginCtrl',
        size: 'lg'
      });

      modalInstance.result.then(function (selectedItem) {
          $scope.selected = selectedItem;
        }, function () {
          $log.info('Modal dismissed at: ' + new Date());
        });
    };


  }]);

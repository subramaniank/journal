'use strict';

/**
 * @ngdoc function
 * @name journyApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the journyApp
 */
angular.module('journyApp')
  .controller('LoginCtrl', ['$scope', 'AuthService', function ($scope, AuthService) {

    $scope.credentials = {
      username: '',
      password: '',
    }

    $scope.login = function(credentials) {
        AuthService.login(credentials).then(function (user) {
          // $rootScope.$broadcast(AUTH_EVENTS.loginSuccess);
          // $scope.setCurrentUser(user);
          console.log(user.username);
        }, function (errors) {
          // $rootScope.$broadcast(AUTH_EVENTS.loginFailed);
          console.log(errors);
        });
    };

  }]);

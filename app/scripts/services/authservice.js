'use strict';

/**
 * @ngdoc service
 * @name journyApp.AuthService
 * @description
 * # AuthService
 * Factory in the journyApp.
 */
angular.module('journyApp')
  .factory('AuthService', [ '$http', 'URLS', 'sessionService', '$q', function ($http, URLS, sessionService, $q) {
    // Service logic
    // ...

    var authService = {};

    authService.login = function (credentials) {

      var user = null;
      var errors = null;

      var loginDeferred = $q.defer()
      var loginPromise = loginDeferred.promise;

      var formData = new FormData();
      formData.append('username',credentials.username);
      formData.append('password',credentials.password);

      var httpPromise = $http({
        url: URLS.BASE_URL+URLS.LOGIN_URL,
        data: formData,
        // transformRequest: function(obj) {
        //   var str = [];
        //   for(var p in obj)
        //     str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        //     return str.join("&");
        //   },
        transformRequest: angular.identity,
          method: 'POST',
          headers: {
            'Content-Type': undefined
          }})
          .then(function(res) {
            var data = res.data;
            if(data.status == 0) {
              data = data.data;
              sessionService.create(data.jour_session_key, data.username);
              user = {username:data.username};
              loginDeferred.resolve(user);
            }
            if(data.status == 2) {
              errors = data.data;
              loginDeferred.reject(errors);
            }
          }, function(res) {
            console.log('WTF');
          });

      return loginPromise;
    };

    authService.isAuthenticated = function () {
            if (sessionService.getSessionKey() == undefined || sessionService.getSessionKey() == null) {
                return true;
            } else {
                return false;
            }
    };

    // TODO add authorization

    return authService;

  }]);

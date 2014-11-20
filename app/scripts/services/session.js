'use strict';

/**
 * @ngdoc service
 * @name journyApp.Session
 * @description
 * # Session
 * Service in the journyApp.
 */
angular.module('journyApp')
  .service('sessionService', ['$cookies', function ($cookies) {
    // AngularJS will instantiate a singleton by calling "new" on this function
    this.create = function (sessionId, userId) {
      this.jour_session_key = sessionId;
      this.jour_user = userId;
      $cookies.jour_session_key = sessionId;
      $cookies.jour_user = userId;
    };
    this.destroy = function () {
      this.jour_user = null;
      this.jour_session_key = null;
    };
    return this;
}]);

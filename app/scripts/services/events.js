'use strict';

/**
 * @ngdoc service
 * @name journyApp.events
 * @description
 * # events
 * Constant in the journyApp.
 */
angular.module('journyApp')
  .constant('AUTH_EVENTS', {
    loginSuccess: 'auth-login-success',
    loginFailed: 'auth-login-failed',
    logoutSuccess: 'auth-logout-success',
    sessionTimeout: 'auth-session-timeout',
    notAuthenticated: 'auth-not-authenticated',
    notAuthorized: 'auth-not-authorized'
  });

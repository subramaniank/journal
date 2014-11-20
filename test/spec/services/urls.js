'use strict';

describe('Service: URLS', function () {

  // load the service's module
  beforeEach(module('journyApp'));

  // instantiate service
  var URLS;
  beforeEach(inject(function (_URLS_) {
    URLS = _URLS_;
  }));

  it('should do something', function () {
    expect(!!URLS).toBe(true);
  });

});

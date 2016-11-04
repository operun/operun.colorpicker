if (window.jQuery) {
  define('jquery', [], function() {
    return window.jQuery;
  });
}

require([
  'jquery',
  'bootstrap-colorpicker',
], function($) {
  'use strict';

  $('#cp2').colorpicker();

});

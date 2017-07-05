/*global $, jQuery, alert*/
$(document).ready(function () {
    "use strict";
    var locked = true,
        currentStatusText = "Current Status: ",
        lockedText = "Locked",
        unlockedText = "Unlocked";
    
    function setLocked() {
        if (locked) {
            $('.door-status p').text(currentStatusText + "Locked");
            $('.door-button').removeClass('unlocked');
            $('.door-button').addClass('locked');
        } else {
            $('.door-status p').text(currentStatusText + "Unlocked");
            $('.door-button').removeClass('locked');
            $('.door-button').addClass('unlocked');
        }
        
        locked = !locked;
    }
    setLocked();
    $('.door-button').click(setLocked).bind(this, true);
});

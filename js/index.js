/*global $, jQuery, alert*/
$(document).ready(function () {
    "use strict";
    var locked = false,
        currentStatusText = "Current Status: ",
        lockedText = "<span style='color: red'>Locked</span>",
        unlockedText = "<span style='color: limegreen'>Open</span>";
    
    function setLocked() {
        if (!locked) {
            $('.door-status p').html(currentStatusText + lockedText);
            $('.door-button').removeClass('unlocked');
            $('.door-button').addClass('locked');
            window.open("/open", "hidden-iframe");
        } else {
            $('.door-status p').html(currentStatusText + unlockedText);
            $('.door-button').removeClass('locked');
            $('.door-button').addClass('unlocked');
            window.open("/close", "hidden-iframe");
        }
        
        locked = !locked;
    }
    setLocked();
    $('.door-button').click(setLocked).bind(this, locked);
});

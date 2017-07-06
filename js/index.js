/*global $, jQuery, alert*/
$(document).ready(function () {
    "use strict";
    var locked = true,
        currentStatusText = "Current Status: ",
        lockedText = "<span style='color: red'>Locked</span>",
        unlockedText = "<span style='color: limegreen'>Open</span>";
    
    function toggleLocked() {
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
    $('.door-status p').html(currentStatusText + lockedText);
    $('.door-button').removeClass('unlocked');
    $('.door-button').addClass('locked');
    $('.door-button').click(setLocked).bind(this, locked);
});

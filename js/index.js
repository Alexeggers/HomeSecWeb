/*global $, jQuery, alert*/
$(document).ready(function () {
    "use strict";
    var open = false,
        currentStatusText = "Current Status: ",
        lockedText = "<span style='color: red'>Locked</span>",
        unlockedText = "<span style='color: limegreen'>Open</span>";
    
    function toggleLocked() {
        if (open) {
            $('.door-status p').html(currentStatusText + lockedText);
            $('.door-button').removeClass('unlocked');
            $('.door-button').addClass('locked');
            window.open("/close", "hidden-iframe");
        } else {
            $('.door-status p').html(currentStatusText + unlockedText);
            $('.door-button').removeClass('locked');
            $('.door-button').addClass('unlocked');
            window.open("/open", "hidden-iframe");
        }
        
        open = !open;
    }
    $('.door-status p').html(currentStatusText + lockedText);
    $('.door-button').removeClass('unlocked');
    $('.door-button').addClass('locked');
    $('.door-button').click(toggleLocked);
});

function stopRequest() {
    return $.get('/stop');
}

function eventSourceCreator(url) {
    return $.get(url);
}

$(document).ready(
    function() {
        $('#left').mouseup(stopRequest).mousedown(() => eventSourceCreator('/startbaseclockwise'))
        $('#right').mouseup(stopRequest).mousedown(() => eventSourceCreator('/startbaseanticlockwise'))
        // $('#right').mouseup(stopRequest).mousedown(() => eventSourceCreator('/right'))
        // $('#left').mouseup(stopRequest).mousedown(() => eventSourceCreator('/left'))
    })
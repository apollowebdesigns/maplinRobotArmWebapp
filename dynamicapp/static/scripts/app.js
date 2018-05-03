function stopRequest() {
    return $.get('/stop');
}

function eventSourceCreator(url) {
    return $.get(url);
}

$(document).ready(
    function() {
        $('#left').mouseup(stopRequest).mousedown(() => eventSourceCreator('/baseclockwise'))
        $('#right').mouseup(stopRequest).mousedown(() => eventSourceCreator('/baseanticlockwise'))

        $('#up').mouseup(stopRequest).mousedown(() => eventSourceCreator('/up'))
        $('#down').mouseup(stopRequest).mousedown(() => eventSourceCreator('/down'))

        $('#elbowup').mouseup(stopRequest).mousedown(() => eventSourceCreator('/elbowup'))
        $('#elbowdown').mouseup(stopRequest).mousedown(() => eventSourceCreator('/elbowdown'))

        $('#wristup').mouseup(stopRequest).mousedown(() => eventSourceCreator('/wristup'))
        $('#wristdown').mouseup(stopRequest).mousedown(() => eventSourceCreator('/wristdown'))

        $('#gripopen').mouseup(stopRequest).mousedown(() => eventSourceCreator('/gripopen'))
        $('#gripclose').mouseup(stopRequest).mousedown(() => eventSourceCreator('/gripclose'))

        $('#lighton').mouseup(stopRequest).mousedown(() => eventSourceCreator('/lighton'))
        $('#lightoff').mouseup(stopRequest).mousedown(() => eventSourceCreator('/lightoff'))
    })
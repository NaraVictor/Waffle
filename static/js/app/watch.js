function fetchRelatedVideo( curVideo ) {
    // TODO: use ajax to load partial videos n display them here
    // TODO: create a separate view n fetch video based on:
    // related (author, subject, country), views, latest
}

function countView( video_id, url ) {

    $.getJSON( 'http://gd.geobytes.com/GetCityDetails?callback=?', function ( data ) {

        $.ajax( {
            type: 'POST',
            url: url,
            data: {
                video: video_id,
                country: data[ 'geobytescountry' ],
                state: data[ 'geobytesregion' ],
                city: data[ 'geobytescity' ],
                ip_address: data[ 'geobytesipaddress' ],
                user_agent: `${navigator.userAgent}`,
                platform: `${navigator.platform}`,
                language: `${navigator.language}`,
            },
            dataType: 'json',
        } );
    } );

}
var chatterbotUrl = '{% url "kirabot:kirabotapi" %}';
var csrftoken = Cookies.get( 'csrftoken' );

function csrfSafeMethod ( method )
{
    // these HTTP methods do not require CSRF protection
    return ( /^(GET|HEAD|OPTIONS|TRACE)$/.test( method ) );
}

$.ajaxSetup( {
    beforeSend: function ( xhr, settings )
    {
        if ( !csrfSafeMethod( settings.type ) && !this.crossDomain )
        {
            xhr.setRequestHeader( "X-CSRFToken", csrftoken );
        }
    }
} );

var $chatlog = $( '.js-chat-log' );
var $input = $( '.js-text' );
var $sayButton = $( '.js-say' );

function createRow ( text )
{
    var $row = $( '<li class="list-group-item"></li>' );

    $row.text( text );
    $chatlog.append( $row );
}

function submitInput ()
{
    var inputData = {
        'text': $input.val()
    }

    // Display the user's input on the web page
    createRow( inputData.text );

    var $submit = $.ajax( {
        type: 'POST',
        url: chatterbotUrl,
        data: JSON.stringify( inputData ),
        contentType: 'application/json'
    } );

    $submit.done( function ( statement )
    {
        createRow( statement.text );

        // Clear the input field
        $input.val( '' );

        // Scroll to the bottom of the chat interface
        $chatlog[ 0 ].scrollTop = $chatlog[ 0 ].scrollHeight;
    } );

    $submit.fail( function ()
    {
        // TODO: Handle errors
    } );
}

$sayButton.click( function ()
{
    submitInput();
} );

$input.keydown( function ( event )
{
    // Submit the input when the enter button is pressed
    if ( event.keyCode == 13 )
    {
        submitInput();
    }
} );
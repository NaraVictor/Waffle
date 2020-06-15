

var $chatlog = $( '.js-chat-log' );
var $input = $( '.js-text' );
var $sayButton = $( '.js-say' );

var $kira_img = '/img/kira2.png';
var $kira_msg = '';

var $user_msg;
var $user_img = '/img/Victor.jpg';

var $msg_time = 'time here';

var $kira_template = $( '<div class="d-flex mb-4 justify-content-start">< div class="img_cont_msg" >' +
    '<img src="{% static ' + "'" + $kira_img + "'" + ' %}" class="rounded-circle user_img_msg" ></div > ' +
    '<div class="msg_container">'
    + $kira_msg +
    '<span class="msg_time">' + $msg_time + ' </span></div></div >' );


var $input_template = '<div class="d-flex mb-4 justify-content-end">' +
    '< div class="msg_container_send">'
    + $user_msg +
    '<span class="msg_time_send">' + $msg_time + '</span></div ><div class="img_cont_msg" >' +
    '<img src="{% static ' + "'" + $user_img + "'" + ' %}" class="rounded-circle user_img_msg"></div></div>';


function createRow ( text )
{
    // $user_msg = input;
    var $row = $( '<li class="list-group-item"><div class="d-flex mb-4 justify-content-end">' +
        '< div class="msg_container_send">'
        + text +
        '<span class="msg_time_send">' + $msg_time + '</span></div ><div class="img_cont_msg" >' +
        '<img src="{% static ' + "'" + $user_img + "'" + ' %}" class="rounded-circle user_img_msg"></div></div></li > ' );

    // $row.text( text );
    $chatlog.append( $row );
    // $chatlog.append( data );
}

function submitInput ()
{
    createRow( $input.val() );

    var $submit = $.ajax( {
        type: 'POST',
        url: 'kira/api/',
        data: $input.val(),
        dataType: 'json',
        contentType: 'application/json'
    } );

    $submit.done( function ( statement )
    {
        createRow( statement.text );
        $input.val( '' );

        // Scroll to the bottom of the chat interface
        $chatlog[ 0 ].scrollTop = $chatlog[ 0 ].scrollHeight;
    } );

    $submit.fail( function ()
    {
        alert( 'Error, could not be submitted' );
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

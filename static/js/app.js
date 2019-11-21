$( document ).ready( function ()
{
    // hides kira when page loads
    $( '.kirabot' ).hide();
    $( '#waffing' ).hide();

    $( ".kira" ).click( function ()
    {
        $( '.kirabot' ).toggle( 'slide' );
        $( '.kiratext' ).toggle( 'fade' );
    } );


    //submitting a question/post
    $( "#waf-form" ).on( 'submit', function ( event )
    {
        // var serializedData = $( this ).serialize();
        event.preventDefault();
        waf();
    } );


    $( '#waf' ).keydown( function ( event )
    {
        // Submit the input when the enter button is pressed
        if ( event.keyCode == 13 )
        {
            waf();
        }
    } );

    //dynamic font size setting
    // $( '.card-text' ).each( function ()
    // {
    //     if ( $.trim( this ).length <= 20 )
    //     {
    //         $( this ).css( {
    //             fontSize: 30
    //         } );
    //     }
    //     else if ( $.trim( this ).length > 20 )
    //     {
    //         $( this ).css( {
    //             fontSize: 20
    //         } );

    //     }
    // } );

} );



//waf ajax call
function waf ()
{
    const months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec" ];
    // using an ajax request
    $.ajax( {
        type: 'POST',
        url: 'waf/',
        data: {
            text: $( '#text' ).val(),
            csrfmiddlewaretoken: $( 'input[name=csrfmiddlewaretoken]' ).val()
        },
        dataType: 'json',
        beforeSend: function ()
        {
            $( '#wafpost' ).modal( 'toggle' ).slideUp( 400 );
            $( '#waffing' ).modal( 'toggle' ).slideUp( 400 );

        },
        success: function ( data )
        {
            $( '#text' ).val( '' ); // remove the value from the input

            setTimeout( function ()
            {
                $( '#waffing' ).modal( 'hide' ).slideUp( 400 );
            }, 1500 );


            var current_datetime = new Date( data.data.card_date );
            var dte = months[ current_datetime.getMonth() ] + ". " + current_datetime.getDate() + ", " + + current_datetime.getFullYear()


            $( '#cards' ).prepend(
                '<div class="media m-0 feed bg-white deskcard mb-1">' +
                '<i style="color: yellowgreen;" class="p-2 fas fa-user-alt fa-2x"></i>' +
                '<div class="media-body">' +
                '<div class="pl-3 pr-2">' +
                '<div class="pb-0 pt-2">' +
                '<span class="username">' + data.username + '</span>' +
                '<span class="text-info text-secondary"> - ' + data.handle + '</span>' +
                '</div> <div class= "text-secondary pb-2 small" > @' + dte + '</div>' +
                '<p class="text-justify pb-0 card-text">' + data.data.text + '</p>' +
                '<footer class="text-secondary pt-0 mt-0 pb-3">' +
                '<hr><span class="pr-3"><i class="fa fa-retweet text-info"></i> 25 </span>' +
                '<span class="pr-2"><i class="fa fa-heart text-danger"></i> 525 </span></footer></div> </div > </div >'
            );

        },

        error: function ( xhr, errmsg, err )
        {
            $( '#errors' ).html( "<div class='alert-box alert radius bg-danger text-white' data-alert>Oops! waf not submitted <a href='#' class='close'>&times;</a></div>" ); // add the error to the dom
        },

    } );

}




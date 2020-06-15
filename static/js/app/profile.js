    // profile update validation
    $( "#submitbtn" ).click( function ( e ) {
        e.preventDefault();
        if ( $( "input[name='birthdate']" ).val() == "" ) {
            $( ".errorlist" ).text( 'please set birthdate' );
        } else if ( $( "input[name='username']" ).val() == "" ) {
            $( ".errorlist" ).text( 'username cannot be empty' );
        } else {
            submitInput();
        }
    } );

    // profile update ajax
    function submitInput() {
        $.ajax( {
            url: profile_url, //variable in profile template file -> profile.html
            data: $( "#profile-form" ).serialize(),
            method: 'post',
            dataType: 'json',
            beforeSend: function () {
                $( "#submitbtn" ).text( 'saving...' );
                $( ".errorlist" ).text( '' );
            },
            success: function ( data ) {
                $( ".status" ).text( 'profile saved...' );
                $( "#submitbtn" ).text( 'save' );
            }
        } ).fail( function ( $xhr ) {
            $( ".status" ).text( '' );
            $( ".errorlist" ).text( $xhr.responseJSON.msg );
            $( "#submitbtn" ).text( 'save' );
        } );
    }


    //profile pic upload
    $( "#profilepic" ).click( function () {
        $( '#dpupload' ).click();
    } );


    // checking user uploaded
    $( '#dpupload' ).on( 'change', () => {
        var file = this.files[ 0 ];
        if ( file == null ) {
            alert( 'No file selected!' );
            return false;
        }

        if ( file.type.includes( 'image' ) ) {
            $( ".errorlist" ).text( '' );
            // call croppie library
            //submit image to server
            upload_profile_pic();
        } else {
            $( ".errorlist" ).text( 'please pick an image file' );
        }
    } );


    function readURL( input ) {
        if ( input.files && input.files[ 0 ] ) {
            var reader = new FileReader();
            reader.onload = function ( e ) {
                $( '#profilepic' ).attr( 'src', e.target.result )
            };
            reader.readAsDataURL( input.files[ 0 ] );
        }
    }


    function upload_profile_pic() {
        $.ajax( {
            url: dp_url, //variable in profile template file -> profile.html
            data: {
                csrfmiddlewaretoken: $( 'input[name=csrfmiddlewaretoken]' ).val(),
                profilepic: $( "#dpupload" ),
            },
            method: 'post',
            dataType: 'html',
            success: function ( data ) {
                readURL( $( '#dpupload' ) );
                alert( 'Profile picture updated' );
            }
        } ).fail( function ( $xhr ) {
            $( ".errorlist" ).text( 'An error occured. Please try again' );
        } );
    }
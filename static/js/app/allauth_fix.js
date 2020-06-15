  $( "#frm input" ).each( function () {
      if ( $( this ).attr( 'type' ) != 'checkbox' ) {
          $( this ).addClass( 'form-control' );
      }
  } );

  $( "#frm label" ).each( function () {
      if ( $( this ).attr( 'for' ) != 'id_remember' ) {
          $( this ).addClass( 'd-none' );
      }
  } );

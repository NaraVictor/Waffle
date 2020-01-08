  //submitting a question/post
  $( "#waf-form" ).on( 'submit', function ( event ) {
      // var serializedData = $( this ).serialize();
      event.preventDefault();
      waf();
  } );


  // $( '#waf' ).keydown( function ( event ) {
  //     // Submit the input when the enter button is pressed
  //     if ( event.keyCode == 13 ) {
  //         waf();
  //     }
  // } );



  //waf ajax call
  function waf() {

      if ( $( '#text' ).val() == "" ) {
          return $( '#waf-error' ).html( "You didn't type anything!" );
      }

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
          beforeSend: function () {
              $( '#wafpost' ).modal( 'toggle' ).slideUp( 400 );
              $( '#waffing' ).modal( 'toggle' ).slideUp( 400 );
              $( '#waf-error' ).html( '' );

          },
          success: function ( data ) {
              $( '#text' ).val( '' ); // remove the value from the input

              setTimeout( function () {
                  $( '#waffing' ).modal( 'hide' ).slideUp( 400 );
              }, 1500 );


              var current_datetime = new Date( data.data.card_date );
              var dte = months[ current_datetime.getMonth() ] + ". " + current_datetime.getDate() + ", " + +current_datetime.getFullYear()


              $( '#deskcards' ).prepend(
                  '<div class="media m-0 feed deskcard">' +
                  '<i style="color: yellowgreen;" class="p-2 fas fa-user-alt fa-2x"></i>' +
                  '<div class="media-body">' +
                  '<div class="pl-3 pr-2">' +
                  '<div class="pb-0 pt-2">' +
                  '<span class="username">' + data.first_name + '</span>' +
                  '<span class="text-muted"> - ' + data.username + '</span>' +
                  '</div> <div class= "text-secondary pb-2 small" > @' + dte + '</div>' +
                  '<p class="text-justify pb-0 card-text">' + data.data.text + '</p>' +
                  '<footer class="text-secondary pt-0 mt-0 pb-3">' +
                  '<hr><span class="pr-5 text-muted reply"><i class="fa fa-reply"></i> 25 </span>' +
                  '<span class="pr-2 text-muted like"><i class="fa fa-heart"></i> 525 </span></footer></div> </div > </div >'
              );

          },

          error: function ( xhr, errmsg, err ) {
              $( '#errors' ).html( "<div class='alert-box alert radius bg-danger text-white' data-alert>Oops! waf not submitted <a href='#' class='close'>&times;</a></div>" ); // add the error to the dom
          },

      } );

  }


  // auto counting waf remaining characters
  $( "#text" ).keyup( function () {
      var l = $( "#text" ).val().length;
      var r = 500 - l;

      if ( r != 0 ) {
          $( ".waf-info" ).text( `${r} characters remaining` );
          $( ".waf-info" ).addClass( 'text-primary' );
          $( ".waf-info" ).removeClass( 'text-danger' );

      } else {
          $( ".waf-info" ).text( 'Limit reached' );
          $( ".waf-info" ).addClass( 'text-danger' );
          $( ".waf-info" ).removeClass( 'text-primary' );
      }
  } );


  // reply textbox autoresizing
  $( '#desk-detail' ).on( 'input', '#reply', function () {
      this.style.height = 'auto';
      this.style.height = ( this.scrollHeight ) + 'px';
  } );


  //   cards - detail view
  $magickey = 0;
  $scroll = 0;
  $( ".reply-count" ).click( function () {
      $scroll = window.scrollY;
      $magickey = $( this ).closest( 'div.reactions' ).attr( 'data-magic' );
      detailToggle();
      load_detail( $magickey ); //inside cards.html file
  } );

  $( ".card-menu" ).click( function () {
      $scroll = window.scrollY;
      $magickey = $( this ).attr( 'data-magic' );
      detailToggle();
      load_detail( $magickey ); //inside cards.html file
  } );



  $( "#detailswap" ).on( 'click', '#detail-back', function () {
      //   the on() allows the event to be tied to dynamic elements through the parent
      detailToggle();
      window.scrollTo( 0, $scroll );
  } );


  function detailToggle() {
      $( "#deskcards" ).toggleClass( 'd-none' );
      $( "#desk-card-detail" ).toggleClass( 'd-none' );
  }


  //replying
  $( "#detailswap" ).on( 'keydown', '#reply', function ( event ) {
      // Submit the input when the enter button is pressed
      if ( event.keyCode == 13 ) {
          reply( $magickey ); //inside card_detail.html file
      }
  } );

 
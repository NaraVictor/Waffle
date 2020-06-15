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

      if ( $( '#waf_text' ).val() == "" ) {
          return $( '#waf-error' ).html( "You didn't type anything!" );
      }

      const months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec" ];
      // using an ajax request
      $.ajax( {
          type: 'POST',
          url: 'waf/',
          data: {
              text: $( '#waf_text' ).val(),
              csrfmiddlewaretoken: $( 'input[name=csrfmiddlewaretoken]' ).val()
          },
          dataType: 'json',
          beforeSend: function () {
              $( '#wafpost' ).modal( 'toggle' ).slideUp( 400 );
              $( '#waffing' ).modal( 'toggle' ).slideUp( 400 );
              $( '#waf-error' ).html( '' );

          },
          success: function ( data ) {
              $( '#waf_text' ).val( '' ); // remove the value from the input

              setTimeout( function () {
                  $( '#waffing' ).modal( 'hide' ).slideUp( 400 );
              }, 500 );


              var current_datetime = new Date( data.data.card_date );
              var dte = months[ current_datetime.getMonth() ] + ". " + current_datetime.getDate() + ", " + +current_datetime.getFullYear()


              $( '#deskcards' ).prepend(
                  `<div class="media m-0 deskcard py-3">
                    <input type="hidden" id="${data.data.id}vote" value="{{vote}}">

                    <img src="/static/img/profile_pics/default.jpg" class="ml-2 rounded-circle z-depth-0 mt-1" alt="profile pic"
                        height="30">
                    <div class="media-body">

                        <div class="pl-3 pr-2">
                            <div class="py-2">
                                <span class="username">${data.first_name}</span>
                                <div>
                                    <span class="text-muted">${data.username} ~ </span>
                                    <small class="text-muted"> Now </small>
                                </div>
                            </div>

                            <div class="card-menu" data-magic="${data.data.id}">
                                <p class="py-2 card-text">${data.data.text}</p>
                            </div>

                            <footer>
                                <hr>
                                <div class="reactions" data-magic="${data.data.id}">
                                    <span class="pr-5 mr-2 text-muted"><i class="reply-count fa fa-reply"></i>
                                        <span class="pl-1 cards-count" id="${data.data.id}count">0</span>
                                    </span>
                                    <!-- <span class="pr-5 mr-3 text-muted"><i class="upvotes fas fa-arrow-up"></i>
                                        <span class="pl-1 cards-upvote" id="${data.data.id}upvote">
                                            {{upvotes}}
                                        </span>
                                    </span>
                                    <span class="text-muted">
                                        <i class="downvotes fas fa-arrow-down"></i>
                                        <span class="pl-1 cards-downvote" id="${data.data.id}downvote">
                                            {{downvotes}}
                                        </span>
                                    </span> -->
                                </div>
                            </footer>
                        </div>
                    </div>
                </div>`

              );

          },

          error: function ( xhr, errmsg, err ) {
              $( '#errors' ).html( "<div class='alert-box alert radius bg-danger text-white' data-alert>Oops! waf not submitted <a href='#' class='close'>&times;</a></div>" ); // add the error to the dom
          },

      } );

  }


  // auto counting waf remaining characters
  $( "#waf_text" ).keyup( function () {
      let l = $( "#waf_text" ).val().length;
      let r = 500 - l;

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
  $( "#deskcards" ).on( 'click', '.reply-count', function () {
      $scroll = window.scrollY;
      $magickey = $( this ).closest( 'div.reactions' ).attr( 'data-magic' );
      detailToggle();
      load_detail( $magickey ); //inside cards.html file
  } );

  $( "#deskcards" ).on( 'click', '.card-menu', function () {
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
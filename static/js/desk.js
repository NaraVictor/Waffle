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

  // main cards vote buttons click
  //upvote click
  //   $( ".upvotes" ).click( function () {
  //       card = $( this ).closest( 'div.reactions' ).attr( 'data-magic' );
  //       vote( 'up', card, "", false );
  //   } );

  //   //downvote click
  //   $( ".downvotes" ).click( function () {
  //       card = $( this ).closest( 'div.reactions' ).attr( 'data-magic' );
  //       vote( 'down', card, "", false );
  //   } );



  //voting
  //   function vote( v_type, card_id, url, paint_detailed ) {
  //       console.log( 'vote function called' );

  //       if ( url == "" ) url = '/desk/vote/'; //look for a way to make this url dynamic

  //       $.ajax( {
  //           type: 'POST',
  //           url: url,
  //           dataType: 'json',
  //           data: {
  //               'card': card_id,
  //               'voteType': v_type,
  //           },
  //           success: function ( a ) {
  //               vote_painter( card_id, a.vote, a.upvotes, a.downvotes, paint_detailed );
  //           }
  //       } );
  //   }

  //refreshes upvotes and downvotes figures & color indications
  //   function vote_painter( card, vote_type, upvote, downvote, paint_detailed ) {
  //       //when paint_detailed is set to true, detailed views are also painted
  //       console.log( 'painter called' );

  //       //update voting reaction numbers
  //       $( `#${ card }upvote` ).text( upvote );
  //       $( `#${ card }downvote` ).text( downvote );

  //       if ( paint_detailed ) { //if paint_detailed is set to true
  //           $( "#d-upvote" ).text( upvote );
  //           $( "#d-downvote" ).text( downvote );
  //           $( `#d-vote` ).val( vote_type ); //update vote cast type data on detailed view
  //       }

  //       //update vote cast type data on main card
  //       $( `#${ card }vote` ).val( vote_type );


  //update coloring
  //       switch ( parseInt( vote_type ) ) {
  //           case 0: //no vote
  //               if ( paint_detailed ) {
  //                   $( "#d-upvote" ).prev( 'i' ).removeClass( 'upvote-cast' );
  //                   $( "#d-downvote" ).prev( 'i' ).removeClass( 'downvote-cast' );
  //               }
  //               $( `#${ card }upvote` ).prev( 'i' ).removeClass( 'upvote-cast' );
  //               $( `#${ card }downvote` ).prev( 'i' ).removeClass( 'downvote-cast' );
  //               break;
  //           case 1: //up vote
  //               if ( paint_detailed ) {
  //                   $( "#d-upvote" ).prev( 'i' ).addClass( 'upvote-cast' );
  //                   $( "#d-downvote" ).prev( 'i' ).removeClass( 'downvote-cast' );
  //               }
  //               $( `#${ card }upvote` ).prev( 'i' ).addClass( 'upvote-cast' );
  //               $( `#${ card }downvote` ).prev( 'i' ).removeClass( 'downvote-cast' );
  //               break;
  //           case 2: //down vote
  //               if ( paint_detailed ) {
  //                   $( "#d-upvote" ).prev( 'i' ).removeClass( 'upvote-cast' );
  //                   $( "#d-downvote" ).prev( 'i' ).addClass( 'downvote-cast' );
  //               }
  //               $( `#${ card }upvote` ).prev( 'i' ).removeClass( 'upvote-cast' );
  //               $( `#${ card }downvote` ).prev( 'i' ).addClass( 'downvote-cast' );
  //               break;
  //           default: //shockwave :)
  //               console.log( `this is abnormal` );
  //               break;
  //       }
  //   }
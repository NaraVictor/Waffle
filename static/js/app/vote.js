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

// $(document).ready(function(){
    // add to cart 
    $('.add_to_cart').on('click',function(e){
        e.preventDefault();
        
        food_id =$(this).attr('data-id');
        food_url =$(this).attr('data-url');

        data={
            food_id:food_id,
        }

        $.ajax({
            type:'GET',
            url: food_url,
            data:data,
            success: function (response_data) {
                if (response_data.status == 'login_required'){
                    swal(response_data.message, '', 'info').then(function(){
                        window.location = '/accounts/login/';
                    })
                }else if(response_data.status == 'Failed'){
                    swal({
                        title: response_data.message,
                        icon: "error",
                        button: "Ok!"
                      });
    
    
                }else{
                //reload er age cart e total item show korbe
                $('#cart_counter').html(response_data.cart_counter['cart_count'])
                // reload er age // plece the cart item quantity on load 
                $('#qty-'+food_id).html(response_data.qty)
                console.log(response_data);
                }



            }
        })
    })

    
// })



// plece the cart item quantity on load 
$('.item_qty').each(function(){
    var the_id = $(this).attr('id')
    var qty = $(this).attr('data-qty')
    $('#'+the_id).html(qty)
})


 // decrease  cart 
 $('.decrease_cart').on('click',function(e){
    e.preventDefault();
    
    food_id =$(this).attr('data-id');
    food_url =$(this).attr('data-url');

    data={
        food_id:food_id,
    }

    $.ajax({
        type:'GET',
        url: food_url,
        data:data,
        success: function (response_data) {
    

            if (response_data.status == 'login_required'){
                swal(response_data.message, '', 'info').then(function(){
                    window.location = '/accounts/login/';
                })
            }else if(response_data.status == 'Failed'){
                swal({
                    title: response_data.message,
                    icon: "error",
                    button: "Ok!"
                  });


            }else{
                console.log(response_data);
                //reload er age cart e total item show korbe
                $('#cart_counter').html(response_data.cart_counter['cart_count'])
                // reload er age // plece the cart item quantity on load 
                $('#qty-'+food_id).html(response_data.qty)
            }


        }
    })
})



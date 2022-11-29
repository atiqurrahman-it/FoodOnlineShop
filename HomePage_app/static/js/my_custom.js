
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
                

                // apply cart amount 
                subtotal=response_data.cart_amount['subtotal']
                tax=response_data.cart_amount['tax']
                grand_total=response_data.cart_amount['grand_total']
                appplyCartAmount(subtotal,tax,grand_total)


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
    cart_id=$(this).attr('id');

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
 
                
                // apply cart amount 
                subtotal=response_data.cart_amount['subtotal']
                tax=response_data.cart_amount['tax']
                grand_total=response_data.cart_amount['grand_total']
                appplyCartAmount(subtotal,tax,grand_total)


                // consol er error jeno na oi ei jonno  if user orlam 
                if(window.location.pathname == '/cart/'){ 
                RemoveCartItem(response_data.qty,cart_id)
                checkEmptyCart()
                }
            }


        }
    })
})


// delete item from cart 

$('.delete_cart').on('click',function(e){
    e.preventDefault();
    
    cart_id =$(this).attr('data-id');
    cart_url =$(this).attr('data-url');

    data={
        cart_id:cart_id,
    }

    $.ajax({
        type:'GET',
        url: cart_url,
        data:data,
        success: function (response_data) {

            if(response_data.status == 'Failed'){
                swal({
                    title: response_data.message,
                    icon: "error",
                    button: "Ok!"
                  });
            }
            else{
                //success
                $('#cart_counter').html(response_data.cart_counter['cart_count'])
                swal({
                    title: response_data.message,
                    icon: "success",
                    button: "Ok!"
                  });

                 // apply cart amount 
                 subtotal=response_data.cart_amount['subtotal']
                 tax=response_data.cart_amount['tax']
                 grand_total=response_data.cart_amount['grand_total']
                 appplyCartAmount(subtotal,tax,grand_total)
                  
                RemoveCartItem(0,cart_id)
                checkEmptyCart()
            }
        }
        
    })
})


//delete show item in your cart 
function RemoveCartItem(cartItemQty,cart_id){
    if(cartItemQty <= 0){
        // remove the cart item element
    document.getElementById('cart-item-'+cart_id).remove()
    }
}

// Check if the cart is empty
    function checkEmptyCart(){
        var cart_counter = document.getElementById('cart_counter').innerHTML
        if(cart_counter == 0){
            document.getElementById("empty-cart").style.display = "block";
        }
    }


//applt cart amount 
function appplyCartAmount(subtotal,tax,grand_total){
    $('#subtotal').html(subtotal)
    $('#total').html(grand_total)
    $('#tax').html(tax)

}


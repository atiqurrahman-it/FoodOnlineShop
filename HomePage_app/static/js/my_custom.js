

$(document).ready(function(){
    $('.add_to_cart').on('click',function(e){
        e.preventDefault();
        food_id=$(this).attr('data-id');
        food_url=$(this).attr('data-url');

        data={
            food_id:food_id,
        }

      
        $.ajax({
            type:'GET',
            url: food_url,
            data:data,
            success: function (response_data) {
                // alert(response_data);
                console.log(response_data);
            }
        })

    })

    
})
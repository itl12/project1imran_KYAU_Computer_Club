$(document).ready(function(){

    const $input = $('input[type=file][accept="image/*"]');
    
    
    const submit_row = $('.submit-row');
    if(submit_row){ compressImage($input, 1920, 1080, 0.8); }; 
    


    
})
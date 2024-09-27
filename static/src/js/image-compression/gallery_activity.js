$(document).ready(function(){

    const form = $('#activity_gallery_form');
    form.attr({'enctype': 'multipart/form-data'});

    const html = '<input style="margin:20px 40px;" type="file" name="image" accept="image/*" id="" multiple>';

    $('#activity_gallery_form .module.aligned').append(html);

    const input = $('input[type=file][accept="image/*"]');




    const submit_row = $('submit-row');
    if(submit_row){ compressImage(input, 1920, 1080, 0.5); };

    

});
$(document).ready(function(){

    let owl = $('#home-carousel');

    owl.owlCarousel({
        loop: true,
        autoHeight: true,
        margin: 0,
        nav : false,
        dots: true,



        smartSpeed: 450,
        autoplay: true,
        autoplayTimeout: 5000,
        animateOut : 'fadeOut',


        
        responsive : {
            0: {
                items: 1
            }
        }

    });

    $('#next').on('click', function(){
        owl.trigger('next.owl.carousel');
    })
    $('#prev').on('click', function(){
        owl.trigger('prev.owl.carousel');
    })

    $('#home-carousel .owl-dots').addClass('absolute bottom-[5px] md:bottom-[15px] left-[50%] translate-x-[-50%]');
    $('#home-carousel .owl-dots .owl-dot span').addClass('h-1 px-4');
    if($(window).width() < 500){
        $('.owl-dots').hide();
    }


})
$( document ).ready(function() {
    $('.avatar-box').css('height', $('.avatar-box').width());
    $('.team .row').css('max-height', $('.team .col-xs-6').height()*2+ 20);
    $('.prev, .next').css('height', $('.team').height());
    var wwidth = $(window).width();
    for(var i = 1; i <= $('.team').length; i+= 1){
        console.log(i);
        $('.team:nth-of-type('+ i +')').css('left', (wwidth - $('.team:nth-of-type('+ i +')').width())/2 + wwidth * (i-1));
    }
});
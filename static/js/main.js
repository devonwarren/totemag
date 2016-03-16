
$(document).ready(function() {

    
    if ($("#side-ad").length) {
        var $sdiv = $("#side-ad");
        var top = $("#side-ad").position().top;
        var height = $('#side-ad').height();

        if ($(window).width() < 600) {
            $sdiv.hide();
        } else {
            $(window).scroll(function() {
                if ($(window).scrollTop() > top && $(window).scrollTop() < top + height) {
                    $sdiv.css('margin-top', $(window).scrollTop() - top + "px");
                }
            });
        }

    }
   

    $( "#subscription" ).remodal();

     $( "#subscribe" ).click(function() {
        $( "#subscription" ).remodal();
     });

     $("#navOpen").click(function() {
       $("body").toggleClass("sidebarOpen");
     });

     $("#shadow").click(function() {
       $("body").removeClass("sidebarOpen");
     });
    
     $('#goto_bazaar').on('change', function() {
        if (this.value != '') {
            location.href = "#shop-" + this.value;
        }
     });


});


function toggleSub(t) {
    $(t).parent().toggleClass("open");
}

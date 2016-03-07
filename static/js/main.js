
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
   

    $( "#subscription" ).dialog({
        autoOpen: true,
        show: {
            effect: "blind",
            duration: 1000
        },
        hide: {
            effect: "fade",
            duration: 1000
        }
    });

     $( "#subscribe" ).click(function() {
        $( "#subscription" ).dialog( "open" );
     });

     $(".navOpen").click(function() {
       $("body").removeClass("contactOpen");
       $("body").toggleClass("sidebarOpen");
     });

     $(".contactOpen").click(function() {
       $("body").removeClass("sidebarOpen");
       $("body").toggleClass("contactOpen");
     });

     function toggleSub(t) {
        $(t).parent().toggleClass("open");
     }
     $('#goto_bazaar').on('change', function() {
        if (this.value != '') {
            location.href = "#shop-" + this.value;
        }
     });


});

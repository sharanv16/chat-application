$(function(){
        $('a#test').bind('click', function(){
            $.getJSON('/run',
            function(data){
            console.log("test")
        })
        return false
    })
})
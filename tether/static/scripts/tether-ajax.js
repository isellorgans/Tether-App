$('#p1').click(function(){
    var player1;
    player1 = $(this).attr("data-player1");
    $.get('/tether/match/', {player1_id: player1}, function (data) {
        $('#p1').html(data);
    });
});

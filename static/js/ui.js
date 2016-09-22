/**
 * Created by sergejandreev on 21.09.16.
 */


$(document).ready(function () {

    //Chart init
    var chart = new Chartist.Bar('#chart', {
        labels: [],
        series: [[]]
    },{
        height: '400px',
        seriesBarDistance: 40,
        divisor: 4,
        axisY: {
            labelInterpolationFnc: function(value) {
                return value
            },
            scaleMinSpace: 15
        }
    });

    //get data from server
    function data_from_server() {
        $.get({
            url: "/get_data/"+$("#id_region").val(),
            success: function (data) {
                var value = [];
                var label = [];
                var obj = $.parseJSON(data);

                for(var key in obj){
                    label.push(key);
                    value.push(obj[key])
                }

                chart.update({
                    labels: label,
                    series: [value]
                })

            },
            statusCode: {
                404: function() {
                    alert("Данного региона не существует" );
                },
                500: function () {
                    alert("Извините ошибка сервера, перезагрузите страницу и попробуйте снова.");
                }
            }
        });
    }

    data_from_server();

    //Handle on change region
    $("#id_region").on("change", function () {
        data_from_server();
    })


});

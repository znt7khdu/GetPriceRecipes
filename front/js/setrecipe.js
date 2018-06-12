function setrecipe() {

//HTMLを初期化
$("table tbody").html("");

//HTMLを生成
$.getJSON("json/CookpadData.json", function(data){
    var count = 0;
    $(data.CookpadData).each(function(){
        $("#data_list").append("<tr id=\"data_id" + count + "\"></tr>");
        $("#data_list #data_id" + count).append("<td>" + this.Food + "</td>");
        $("#data_list #data_id" + count).append("<td>" + this.Amount + "</td>");
        count++;
    })
})
}

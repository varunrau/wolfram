$(document).ready(function() {
    $('#search-form').click(function(e) {
        // e.preventDefault();
        var posting = $.post("/query-async", {"value": "" + $('.text-thing').val()});
        posting.done(function(data) {
            $('.table-wrapper').empty();
            var content = "<div class='output'>"
            content += "<table class='table table-bordered'>";
            content += "<caption style='padding: 10px;'>Your problem has been solved!</caption>"
            content + "<thead><th></th><th>Field</th><th>Value</th></thead><tbody>"
            for (var field in data) {
                if (data[field] == null) {
                    continue;
                }
                content += "<tr class='row'><td>" + field + "</td><td>" + data[field] + "</td></tr>";
            }
            content += "</tbody></table></div>";
            $('.table-wrapper').append(content);
            $('.table-wrapper').removeClass("hide");
        });
    });
});

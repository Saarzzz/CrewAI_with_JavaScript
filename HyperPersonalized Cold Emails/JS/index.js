$(document).ready(function() {
  $("#researchForm").submit(function(event) {
      event.preventDefault();

      const prospect = $("#prospect").val();
      const reason = $("#reason").val();

      const data = { prospect, reason };

      $.ajax({
          url: "http://127.0.0.1:3001/api/crewA",
          method: "POST",
          contentType: "application/json",
          data: JSON.stringify(data),
          success: function(response) {
              $("#results").text(nl2br(JSON.stringify(response, null, 2)));
          },
          error: function(error) {
              $("#results").text("Error: " + error.responseText);
          }
      });
  });
});

function nl2br (str, is_xhtml) {   
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';    
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1'+ breakTag +'$2');
}

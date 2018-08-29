// function to save to database
    function saveMarkerInfo(){
        console.log("in function saveMarkerInfo");
        // one way to get the element of the title:
        // var marker = document.getElementById('addMarker');
        // var name = marker.dataset.title; 
        // console.log("this is the name:");
        // console.log(name);

        var marker_title = $("#addMarker").data("title");
        // doesn't give value
        // console.log(" this is the title:");
        // console.log(marker_title);

        var marker_position = $("#addMarker").data("position");
        // console.log("marker_position is");
        // console.log(marker_position);

// make a query getting the pinpoint from database
// get all info from the pinpoint form
// update the info in thedatabase using pinpoint id 

        ///////////////////how to do without for loop
        // for ( let i=0; i<markers.length; i++){
            // console.log("in for loop");
            var name = marker_title;
            // var latlng = marker_position.getPosition().toString();
            var start = document.getElementById("start").value;
            var end = document.getElementById("end").value;
            var rating = document.getElementById("rating").value;
            var description = document.getElementById("description").value;

            var if_exists = true; // true= if editing the pinpoint, false= if addig a new pinpoint
            var place = {"name": name, "start": start, "end":end, "rating": rating, "description":description, "if_exists":if_exists}; 
          
            
            // // $.post("/add-pinpoint", {"name": name}, resultFunc);
            $.post("/add-pinpoint", place, resultFunc);
            // console.log("marker.title: "+ name);
           
     }

     function resultFunc(result){
          console.log("in resultFunc");
          alert(result);
    }
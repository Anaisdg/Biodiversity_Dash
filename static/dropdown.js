
// STEP ONE:
// Create sample selector populated by data from /names route from app.py using
// AJAX requests

// Define the url
var url = '/names';

// Make an asynchronous call to get the data
Plotly.d3.json(url, function(error, names){
  console.log(names);
  select_elem = document.getElementById("selDataset")
  if(select_elem){
      for(var i = 0; i < names.length; i++) {
          var option = document.createElement('option');
          option.innerHTML = names[i];
          option.value = names[i];
          select_elem.appendChild(option);
        };
      };
    });

// Create a function that allows you to change the option and creates urls for future data calls
function optionChanged(sel){
  console.log('Option Changed Called');
  var value = sel;
  var url2 = '/metadata/' + value;
  var url3 = '/wfreq/'  + value;
  var url4 = '/samples/' + value;
    console.log(url4);

    // STEP TWO

    // Create a PIE chart that uses data from routes /samples/<sample> and /otu to display the top 10 samples.

    Plotly.d3.json(url3, function (error, pieData) {

            var pie_labels = pieData['otu_id']

            var pie_values = pieData['sample_values']

            var data = [{
                values: pie_values,
                labels: pie_labels,
                type: "pie"
            }];

            var layout = {
                height: 500,
                width: 700,
                title: "Biodiversity Pie Chart",
            };
            Plotly.newPlot("plot1", data, layout);

        });


    // Plotly.d3.json(url2, function (error, metaData) {
    //       console.log(metaData);
    //       Plotly.d3.select("tbody")
    //           .html("")
    //           .selectAll("tr")
    //           .data(metaData)
    //           .enter()
    //           .append("tr")
    //           .html(function (d) {
    //               return `<td>${d.t0}</td><td>${d.t1}</td>`
    //           });
    //   });


// bracket below connect to top dont delete
}




//  function make_drop_down(sample_names, element_id){
//   select_elem = document.getElementById(element_id)
//   if(select_elem){
//       for(var i = 0; i < list_of_names.length; i++) {
//           var option = document.createElement('option');
//           option.innerHTML = sample_names[i];
//           option.value = sample_names[i];
//           select_elem.appendChild(option);
//         }
//       }
//     };
//
// make_drop_down(data,"selDataset")

// var url = "/names";
//
// function buildPlot() {
//     Plotly.d3.json(url, function(error, response) {
//
//         console.log(response);
//       };
//     };
//
// buildPlot()

//
// function build_dropdown(base_url){
//   console.log('build_dropdown working' )
//   var url = base_url + "/names"
//
//   d3.json(url, function(error, response) {
//         if (error) return console.warn(error);
//
//         select_elem = document.getElementById('#selSamples')
//         if(select_elem){
//             for(var i = 0; i < response.length; i++) {
//                 var option = document.createElement('option');
//                 option.innerHTML = response[i];
//                 option.value = response[i];
//                 select_elem.appendChild('option');
//               };
//             };
//           });
//
// };
//
// build_dropdown(base_url);
